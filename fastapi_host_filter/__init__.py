import fnmatch
from typing import Sequence
from starlette.types import ASGIApp, Receive, Scope, Send
from starlette.responses import Response

class TrustedHostMiddleware:
    """
    Middleware that ensures the HTTP Host header matches a list of allowed patterns.
    """

    def __init__(self, app: ASGIApp, allowed_hosts: Sequence[str] = ("*",)):
        self.app = app
        self.allowed_hosts = list(allowed_hosts)
        self.allow_all = "*" in self.allowed_hosts

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] not in ("http", "websocket") or self.allow_all:
            await self.app(scope, receive, send)
            return

        headers = dict(scope.get("headers", []))
        host_header = headers.get(b"host", b"").decode("latin1")

        # Strip port number
        hostname = host_header.split(":")[0].lower() if host_header else ""

        is_valid = any(fnmatch.fnmatch(hostname, pattern.lower()) for pattern in self.allowed_hosts)

        if not is_valid:
            res = Response(content=b'{"error": "Invalid Host Header"}', status_code=400, media_type="application/json")
            await res(scope, receive, send)
            return

        await self.app(scope, receive, send)
