"""DeepRaaga Preprocess - Data ingestion layer for DeepRaaga."""

from deepraaga_preprocess.data_processor import DataProcessor
from deepraaga_preprocess.preprocess_raga import (
    load_raga_data,
    swara_to_midi,
    convert_pattern_to_midi,
    create_raga_features,
    preprocess_ragas,
)

__version__ = "0.1.0"
__all__ = [
    "DataProcessor",
    "load_raga_data",
    "swara_to_midi",
    "convert_pattern_to_midi",
    "create_raga_features",
    "preprocess_ragas",
]
