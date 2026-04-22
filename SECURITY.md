# Security Policy

## Supported Versions

| Version | Supported |
|---|---|
| 0.1.x | ✅ Active |

## Reporting a Vulnerability

**Please do NOT open a public GitHub issue for security vulnerabilities.**

Instead, report security issues via **GitHub's private security advisory** feature:

1. Navigate to [https://github.com/sgmoorthy/naada/security/advisories](https://github.com/sgmoorthy/naada/security/advisories)
2. Click **"New draft security advisory"**
3. Provide a clear description of the vulnerability and steps to reproduce

Alternatively, email **sgmoorthy@gmail.com** with subject `[SECURITY] naada vulnerability`.

## Response Timeline

- **Acknowledgment:** Within 48 hours
- **Initial assessment:** Within 5 business days
- **Fix & disclosure:** Coordinated with reporter; target within 30 days

## Scope

### In scope
- Flask API endpoints (`app.py`) — injection, authentication bypass
- Model loading (`model/model.py`) — unsafe deserialization of `.pth`/`.pkl` files
- Data pipeline — path traversal in MIDI file processing

### Out of scope
- Vulnerabilities in third-party dependencies (report upstream: PyTorch, music21, librosa)
- The React frontend's client-side rendering (no sensitive data stored)

## Safe Handling of Model Weights

naada uses `torch.load()` to load `.pth` model weights. **Never load model files from untrusted sources** — pickle-based formats can execute arbitrary code. Always download model weights from the official [GitHub Releases](https://github.com/sgmoorthy/naada/releases) page.
