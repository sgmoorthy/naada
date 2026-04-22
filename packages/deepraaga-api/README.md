# deepraaga-api

Flask-based API serving endpoints for DeepRaaga music generation. Extracted from the original [DeepRaaga](https://github.com/sgmoorthy/DeepRaaga) project.

## Installation

You can install the API layer via pip. To ensure that the underlying neural network models are available for generation, you should install it with the `models` optional dependencies:

```bash
pip install deepraaga-api[models]
```

## Overview

The `deepraaga-api` package provides a RESTful interface over the DeepRaaga machine learning backend. It allows external applications (like React frontends) to easily query and generate sequential notes based on learned Carnatic representations.

## Usage

You can start the API directly using the bundled CLI tool:

```bash
deepraaga-api --port 8000
```

This will spin up a local Flask server running on `http://localhost:8000`.

### REST Endpoints

#### `GET /`
Returns the status of the DeepRaaga API.

#### `POST /api/generate`
Generates a sequence of notes.
- **Request Body:**
  ```json
  {
      "raga": "mayamalavagowla",
      "duration": 30,
      "temperature": 1.0
  }
  ```
- **Response:**
  ```json
  {
      "notes": ["C4", "D4", "E4", "F4", "G4"],
      "raga": "mayamalavagowla"
  }
  ```

## Programmatic Usage

You can also import the Flask app directly to mount it in another WSGI server (like Gunicorn):

```python
from deepraaga_api.serve import app

if __name__ == '__main__':
    app.run(port=8080)
```

## License

This project is licensed under the MIT License.
