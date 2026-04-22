# deepraaga-core

Core domain models and abstractions for Carnatic music AI. Extracted from the original [DeepRaaga](https://github.com/sgmoorthy/DeepRaaga) project.

## Installation

You can install the package directly via pip:

```bash
pip install deepraaga-core
```

## Overview

The `deepraaga-core` package provides the foundational data structures and base models for representing Carnatic music constructs. This acts as the base dependency for all other `deepraaga-*` packages in the ecosystem, ensuring a standardized representation of Ragas, Swaras, and machine learning model configurations.

## Usage

You can use the base abstractions to build out your own model architectures tailored for Carnatic music:

```python
from deepraaga_core.base import BaseModel, VGGModel

# Define a configuration for your architecture
config = {
    'input_shape': (224, 224, 3),
    'num_classes': 72 # e.g. for the 72 Melakarta ragas
}

# Initialize the core model abstraction
model = VGGModel(config)

# Access standard base methods
model.build_model()
```

## License

This project is licensed under the MIT License.
