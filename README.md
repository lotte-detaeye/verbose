# Verbose
Work-in-progress NLP project focused on identifying and annotating common tendencies, biased expressions and non-idiomatic language in my own writing:
- Hedging expressions (e.g., "It seems", "might", "I believe")
- Use of 'he' as universal pronoun
- Non-canonical word order (e.g., "There came a man")

The annotations will be used for fine-tuning or rule-based evaluation in spaCy.

## File Structure

- `annotations.jsonl`: file with sample annotations in **Doccano’s JSONL format**
- `convert_doccano_to_spacy.py`: script to convert to spaCy format and visualize results

## Installation

```bash
pip install spacy
```
