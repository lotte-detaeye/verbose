import json
import spacy
from spacy.tokens import DocBin
import sys

def convert(jsonl_path, output_path):
    nlp = spacy.blank("en")
    db = DocBin()

    with open(jsonl_path, 'r', encoding='utf-8') as f:
        for line in f:
            record = json.loads(line)
            text = record["text"]
            doc = nlp.make_doc(text)
            ents = []
            for start, end, label in record.get("labels", []):
                span = doc.char_span(start, end, label=label)
                if span is None:
                    print(f"Skipping span: ({start}, {end}, {label}) in: {text}")
                    continue
                ents.append(span)
            doc.ents = ents
            db.add(doc)

    db.to_disk(output_path)
    print(f"Saved {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_doccano_to_spacy.py <input.jsonl> <output.spacy>")
    else:
        convert(sys.argv[1], sys.argv[2])
