# Changelog

All notable changes to **naada** are documented here.

This project adheres to [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and [Semantic Versioning](https://semver.org/).

---

## [Unreleased]

### Planned
- Raga grammar validation layer with strict Arohana/Avarohana enforcement
- Gamaka microtonal notation in annotation CSVs
- Tala rhythmic awareness (Adi Tala 8-beat cycle constraint)

---

## [0.1.0] — 2026-04-21

### Added
- **LSTM + Multi-head Attention model** (`model/model.py`) — `DeepRagaModel` with embedding, 2-layer LSTM, 4-head attention, and cross-entropy generation
- **Data pipeline** (`model/data_processor.py`) — MIDI → NoteSequence vocabulary extraction and sequence generation via `music21`
- **Training loop** (`model/train.py`) — full train/val split, Adam optimizer, 80/20 cross-validation
- **Flask REST API** (`app.py`) — `/api/generate` endpoint with temperature-controlled sampling
- **72 Melakarta Registry** (`data/melakarta_init.py`) — standardized `midi/`, `musicxml/`, `annotations/` scaffold for all 72 parent ragas; `manifest.json` auto-generated
- **React SPA** — glassmorphic UI with MUI 5, Raga generator, Raga encyclopedia (`CarnaticRagaInfo`), audio visualizer
- **Technical Blog** — 7 inaugural posts covering AI Carnatic, PM vision, democratizing music education, future of Tala, code internals, contributing guide, and Music-as-Code philosophy
- **GitHub Actions** — `deploy.yml` for automated GitHub Pages deployment, `python-ci.yml` for backend CI, `frontend-ci.yml` for frontend CI
- **PyPI package** — `naada` package published with `pyproject.toml`; entry points `naada-serve` and `naada-init-dataset`
- **GitHub community files** — `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, PR template, issue templates for ML engineers and musicians

### Philosophy
- Established the **Music-as-Code** paradigm: Ragas as functional constraint schemas, compositions as versionable artifacts, pedagogy as CI/CD

[Unreleased]: https://github.com/sgmoorthy/naada/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/sgmoorthy/naada/releases/tag/v0.1.0
