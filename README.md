# Verbose
Work-in-progress NLP project focused on identifying and annotating common tendencies and non-idiomatic language in my own writing:
- Hedging expressions (e.g., "It seems", "might", "I believe")
- Non-canonical word order (e.g., "There came a man")

The annotations will be used for fine-tuning or rule-based evaluation in spaCy.

## File Structure

- `annotations.jsonl`: JSONL file with sample annotations
- `process_annotations.py`: script to load and visualize annotations using spaCy

## Installation

```bash
pip install spacy
```
