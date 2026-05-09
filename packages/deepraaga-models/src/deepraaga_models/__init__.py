"""DeepRaaga Models - Neural network generation backend for DeepRaaga."""

from deepraaga_models.model import DeepRagaModel
from deepraaga_models.train import RagaDataset, train_model, main as train_main

__version__ = "0.1.0"
__all__ = ["DeepRagaModel", "RagaDataset", "train_model", "train_main"]
