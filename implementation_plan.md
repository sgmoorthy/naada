# DeepRaaga PyPI Publication Plan

This implementation plan outlines the restructuring of the DeepRaaga repository into a well-architected Python monorepo. This structure will isolate the frontend from the Python backend packages, allowing us to successfully publish the Python components—starting with `deepraaga-core` and `deepraaga-api`—to PyPI.

## User Review Required

> [!IMPORTANT]
> - Breaking Paths: Relocating `app.py`, `model/`, `data/`, and frontend assets to dedicated subfolders will impact existing local development scripts or CI/CD pipelines (e.g. GitHub Actions for deploying the Vite frontend). Are we okay updating continuous integration scripts in this pass?
> - `data/` Separation: Datasets (`DeepRaaga-Dataset`) will be physically separated from code files (`melakarta_init.py`). File paths for local testing will need to be adjusted.
> - Package Boundary Confirmation: Please confirm the strict boundaries between packages (e.g. `music21` stays in `preprocess`, `torch` stays in `models`). 

## Proposed Changes

We will refactor the mixed workspace into a separated Python Monorepo alongside isolated frontend and data directories.

### Folder Restructuring

```text
DeepRaaga/
├── packages/
│   ├── deepraaga-core/
│   │   ├── pyproject.toml
│   │   ├── src/
│   │   │   └── deepraaga_core/
│   │   │       ├── __init__.py
│   │   │       ├── domain/        # e.g., abstracted from melakarta_init.py
│   │   │       └── base.py        # Base schema definitions
│   ├── deepraaga-preprocess/
│   │   ├── pyproject.toml
│   │   ├── src/
│   │   │   └── deepraaga_preprocess/
│   │   │       ├── data_processor.py  # from model/data_processor.py
│   │   │       └── preprocess_raga.py # from model/preprocess_raga.py
│   ├── deepraaga-models/
│   │   ├── pyproject.toml
│   │   ├── src/
│   │   │   └── deepraaga_models/
│   │   │       ├── __init__.py
│   │   │       ├── model.py           # from model/model.py
│   │   │       └── train.py           # from model/train.py & train_model.py
│   └── deepraaga-api/
│       ├── pyproject.toml
│       ├── src/
│       │   └── deepraaga_api/
│       │       ├── __init__.py
│       │       ├── serve.py           # from app.py
│       │       └── cli.py             # CLI application entrypoint
├── frontend/                          # all React/Vite src/, public/ index.html, package.json
├── datasets/                          # datasets like DeepRaaga-Dataset
└── model-artifacts/                   # Trained weights (.pth files), model results and logs
```

### Exact Package Boundaries

1. **`deepraaga-core`**: The foundational library.
   - **Scope**: Raga domain models, note abstractions, arohana/avarohana rules, gamaka metadata.
   - **Dependencies**: Minimal (pure Python as much as possible).

2. **`deepraaga-preprocess`**: The data ingestion layer.
   - **Scope**: MIDI/MusicXML ingestion, sequence conversion, vocabulary builders.
   - **Dependencies**: `deepraaga-core`, `music21`, `librosa`, `numpy`.

3. **`deepraaga-models`**: Neural network generation backend.
   - **Scope**: LSTM/Transformer model architectures, training loops, inference wrappers.
   - **Dependencies**: `deepraaga-core`, `torch`, `numpy`.

4. **`deepraaga-api`**: The REST service layer.
   - **Scope**: Web server endpoints to connect frontend interactions to model generation.
   - **Dependencies**: `deepraaga-core`, `Flask`, `Flask-CORS`.
   - **Extras**: `[models]` extra can pull in `deepraaga-models` and `torch` to enable live model generation capabilities.

### Proposed `pyproject.toml` (Examples)

**`packages/deepraaga-core/pyproject.toml`**
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "deepraaga-core"
version = "0.1.0"
description = "Core domain models and abstractions for Carnatic music AI."
readme = "README.md"
requires-python = ">=3.8"
authors = [
    { name = "Surya G", email = "author@example.com" }
]
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
]
dependencies = []
```

**`packages/deepraaga-api/pyproject.toml`**
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "deepraaga-api"
version = "0.1.0"
description = "Flask-based API serving endpoints for DeepRaaga music generation."
readme = "README.md"
requires-python = ">=3.8"
dependencies = [
    "deepraaga-core",
    "flask",
    "flask-cors"
]

[project.optional-dependencies]
models = ["deepraaga-models", "torch", "numpy"]

[project.scripts]
deepraaga-api = "deepraaga_api.cli:main"
```

### CLI Entry Points

In `deepraaga_api/cli.py`, we will add a clean CLI entry point allowing users to spin up the API quickly:
```python
import argparse
from deepraaga_api.serve import app

def main():
    parser = argparse.ArgumentParser(description="Run the DeepRaaga API Server")
    parser.add_argument("--port", type=int, default=8000, help="Port to run the API on")
    parser.add_argument("--host", type=str, default="localhost", help="Host address")
    args = parser.parse_args()
    
    app.run(host=args.host, port=args.port, debug=True)
```

### Release Checklist (TestPyPI -> PyPI)

1. **Sanity Check**: Ensure all nested `__init__.py` files exist and modules load correctly via local relative pip installation (`pip install -e packages/deepraaga-core`).
2. **Build Distribution**:
   - `python -m build` inside the respective package directory to generate source distributions (`sdist`) and wheels (`whl`).
3. **TestPyPI Validation**:
   - `twine upload --repository testpypi dist/*`
   - Test installation locally from TestPyPI: `pip install --index-url https://test.pypi.org/simple/ deepraaga-core`
4. **PyPI Production Release**:
   - `twine upload dist/*`
5. **Git Tagging**: Tag the specific release hash (e.g., `git tag v0.1.0-core` and `git push --tags`).
6. **Documentation Update**: Add installation strings (`pip install deepraaga-core`) to main `README.md`.

## Open Questions

- We currently rely on local paths (e.g., `os.path.join('data', 'processed', 'vocab.pkl')`) in `app.py`. Do we want to build a configuration file or environment variables handling system for locating dataset and model artifacts elegantly post-restructure?
- Do you want to proceed with doing all folders manually or starting directly with just `deepraaga-core` and `deepraaga-api` codebase extraction while putting UI into `/frontend`?

## Verification Plan

### Automated Tests
- Build all packages using `build` module.
- Validate the built wheel payload lengths and contents to ensure they don't contain extraneous data or node_modules.

### Manual Verification
- Start the API using `deepraaga-api --port 8000` CLI command.
- Hit the endpoint using `test_api.py` (which will move alongside) to verify the fallback functionality works when models aren't loaded.
