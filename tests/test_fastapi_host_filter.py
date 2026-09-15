import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi_host_filter import TrustedHostMiddleware

def test_trusted_host():
    app = FastAPI()
    app.add_middleware(TrustedHostMiddleware, allowed_hosts=["api.example.com", "*.local"])

    @app.get("/")
    def index():
        return {"ok": True}

    client = TestClient(app)

    # Valid exact host
    assert client.get("/", headers={"Host": "api.example.com"}).status_code == 200

    # Valid wildcard host
    assert client.get("/", headers={"Host": "sub.local:8000"}).status_code == 200

    # Invalid host -> 400
    assert client.get("/", headers={"Host": "attacker.com"}).status_code == 400
