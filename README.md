# Safetensors Metadata Editor

A simple command-line tool to **read, add, update, or delete metadata** from `.safetensors` checkpoint files.  
This is useful when you want to inspect or modify the metadata stored in model files without touching the tensor weights.

---

## 📦 Installation

Clone or copy this repository and install the required dependency:

```bash
pip install safetensors torch
```

Make the script executable (optional):

```bash
chmod +x safetensors_metadata_editor.py
```

## 📖 Quick Reference

| Action                     | Command Example |
|-----------------------------|-----------------|
| **Print metadata**          | `python safetensors_metadata_editor.py model.safetensors --print` |
| **Add / update metadata**   | `python safetensors_metadata_editor.py model.safetensors --set key=value` |
| **Set multiple values**     | `python safetensors_metadata_editor.py model.safetensors --set tag=exp1 --set owner=Alice` |
| **Delete metadata key**     | `python safetensors_metadata_editor.py model.safetensors --delete workflow` |
| **Save to new file**        | `python safetensors_metadata_editor.py model.safetensors --set owner=Bob --out new_model.safetensors` |

---

## 🚀 Usage

### Print metadata

View all metadata stored in a `.safetensors` file:

```bash
python safetensors_metadata_editor.py model.safetensors --print
```

---

### Add or update metadata

Set one or more `KEY=VALUE` pairs:

```bash
python safetensors_metadata_editor.py model.safetensors \
    --set description="Fine-tuned on dataset XYZ" \
    --set tag=experiment123
```

---

### Delete metadata

Remove one or more keys:

```bash
python safetensors_metadata_editor.py model.safetensors --delete workflow
```

---

### Save to a new file

By default, the script overwrites the input file. To write to a new file instead, use `--out`:

```bash
python safetensors_metadata_editor.py model.safetensors \
    --set owner="Alice" \
    --out new_model.safetensors
```

---

## ⚠️ Notes

* Metadata is limited to **string key → string value** pairs.
* Use `--out` if you want to keep the original file unchanged.
* Deleting or modifying metadata does **not** affect the tensors themselves.

---

## 📖 Example

```bash
# View existing metadata
python safetensors_metadata_editor.py model.safetensors --print

# Remove the "workflow" tag and save to a new file
python safetensors_metadata_editor.py model.safetensors --delete workflow --out model_clean.safetensors

# Add an experiment tag
python safetensors_metadata_editor.py model_clean.safetensors --set experiment="run_42"
```

---

## 🔑 License

MIT

