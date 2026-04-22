# Contributing to naada 🎵

Thank you for being part of the naada community. We're building the world's first open-source Carnatic music AI framework — and we need **three types of contributors**:

| Role | What you bring | Where to start |
|---|---|---|
| 🎼 **Musicologist** | MIDI recordings, notation, Gamaka labels | `data/` — add to the Melakarta registry |
| 🤖 **ML Engineer** | Model improvements, training pipelines, new architectures | `model/` — improve the LSTM/Attention core |
| ⚛️ **Frontend Developer** | React components, UX, accessibility | `src/` — enhance the SPA |

---

## 🚀 Getting Started

### 1. Fork & Clone
```bash
git fork https://github.com/sgmoorthy/naada
git clone https://github.com/<your-username>/naada.git
cd naada
```

### 2. Set Up Python Backend
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .\.venv\Scripts\activate
pip install -e ".[dev]"     # installs naada + dev extras (ruff, pytest, black)
pre-commit install          # sets up linting hooks
```

### 3. Set Up React Frontend
```bash
npm install
npm run dev                 # → http://localhost:3000
```

---

## 🌿 Branch Naming Convention

| Type | Pattern | Example |
|---|---|---|
| New feature | `feature/<name>` | `feature/tala-rhythmic-layer` |
| Bug fix | `fix/<name>` | `fix/gamaka-annotation-parser` |
| Dataset contribution | `data/<raga-name>` | `data/bhairavi-midi-set` |
| Documentation | `docs/<topic>` | `docs/melakarta-guide` |

---

## ✅ Before Submitting a PR

### Python changes
```bash
ruff check model/ data/ app.py     # linting
black model/ data/ app.py          # formatting
pytest test/ -v                    # run tests
```

### Frontend changes
```bash
npm run build                      # must succeed with zero errors
```

### Dataset contributions
- MIDI files go in `data/DeepRaaga-Dataset/Melakarta/<ID>_<Name>/midi/`
- MusicXML in `musicxml/`, annotation CSVs in `annotations/`
- Verify the Arohana/Avarohana rules are strictly respected
- Run `python data/melakarta_init.py` to validate the structure

---

## 📋 PR Process

1. Fill out the [PR template](.github/PULL_REQUEST_TEMPLATE.md) completely
2. Reference any related issues (`Closes #42`)
3. CI must pass (Python CI + Frontend CI)
4. Request review from a maintainer
5. Squash-merge after approval

---

## 🙏 Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). Be excellent to each other.

---

## 💬 Questions?

Open a [GitHub Discussion](https://github.com/sgmoorthy/naada/discussions) — we respond within 48 hours.
