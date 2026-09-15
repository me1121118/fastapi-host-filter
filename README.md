# fastapi-host-filter

[![PyPI version](https://img.shields.io/badge/pypi-v0.1.0-blue.svg)](https://pypi.org/project/fastapi-host-filter/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

FastAPI & Starlette middleware to prevent HTTP Host Header Poisoning attacks with wildcard subdomain support.

---

## 🚀 Features

- 🛡️ **Host Header Poisoning Guard**: Rejects spoofed `Host` headers with standard HTTP 400 Bad Request.
- 🌐 **Wildcard Matching**: Supports `*.example.com` domain wildcards.
- ⚡ **Port Agnostic**: Strips port numbers before comparing hostnames.

---

## 📦 Installation

```bash
pip install fastapi-host-filter
```

---

## 🛠️ Quickstart

```python
from fastapi import FastAPI
from fastapi_host_filter import TrustedHostMiddleware

app = FastAPI()
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["example.com", "*.example.com", "localhost"])

@app.get("/")
def home():
    return {"status": "ok"}
```

---

## ☕ Support My Studies / Buy Me a Coffee

I am an independent developer and student building open-source developer productivity tools. If this middleware secured your domain headers, please consider supporting my studies:

- ☕ **Buy Me a Coffee:** [ko-fi.com/me1121118](https://ko-fi.com/)
- ⭐ **Star this repository** on GitHub!

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
