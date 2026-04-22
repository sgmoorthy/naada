# deepraaga-models

Neural network generation backend for DeepRaaga. Extracted from the original [DeepRaaga](https://github.com/sgmoorthy/DeepRaaga) project.

## Installation

```bash
pip install deepraaga-models
```

## Overview

The `deepraaga-models` package holds the PyTorch implementations for Carnatic music sequence generation. It provides Recurrent Neural Network (LSTM/GRU) architectures tailored to understand and generate sequential note distributions for various Ragas.

## Usage

This package provides a ready-to-use PyTorch dataset layout (`RagaDataset`) and model architecture (`DeepRagaModel`).

### Model Initialization

```python
import torch
from deepraaga_models.model import DeepRagaModel

vocab_size = 128
embedding_dim = 64
hidden_size = 256
num_layers = 2

# Initialize the model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = DeepRagaModel(vocab_size, embedding_dim, hidden_size, num_layers).to(device)

# Provide a sequence tensor (batch_size, sequence_length)
input_seq = torch.LongTensor([[60, 62, 64, 65, 67]]).to(device)
output, hidden = model(input_seq)
```

### Training

You can utilize the built-in training scripts for rapid experimentation:

```python
from deepraaga_models.train import train_model

# Requires torch DataLoaders
# train_model(model, train_loader, val_loader, num_epochs=50, device=device, vocab_size=vocab_size)
```

## License

This project is licensed under the MIT License.
