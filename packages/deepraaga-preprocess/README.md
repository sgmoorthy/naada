# deepraaga-preprocess

Data ingestion layer for DeepRaaga. Extracted from the original [DeepRaaga](https://github.com/sgmoorthy/DeepRaaga) project.

## Installation

```bash
pip install deepraaga-preprocess
```

## Overview

The `deepraaga-preprocess` module handles the ingestion and transformation of Carnatic music data. This includes parsing MIDI files and abstract sequence processing to map musical notes and swaras into sequences readable by machine learning models.

## Usage

You can use the `DataProcessor` to easily convert a directory of MIDI files into `numpy` feature sequences ready for training:

```python
import os
from deepraaga_preprocess.data_processor import DataProcessor

processor = DataProcessor(sequence_length=100)

# Process a directory of raw MIDI files and output training numpy arrays
processor.process_dataset(midi_dir='data/raw_midi', output_dir='data/processed')

# Load the resulting vocabulary mapping later
processor.load_vocab('data/processed/vocab.pkl')
```

## Features

- **MIDI Feature Extraction:** Parses incoming MIDI structures using `music21` and resolves them to sequential sequences.
- **Dynamic Vocabulary:** Dynamically builds note-to-integer mappings.
- **Raga Abstraction:** Support for processing Carnatic arohanam and avarohanam notation (via `preprocess_raga.py`).

## License

This project is licensed under the MIT License.
