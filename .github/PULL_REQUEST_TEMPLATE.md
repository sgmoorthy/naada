## Description

<!-- What does this PR change and why? Be concise but complete. -->

## Type of Change

- [ ] 🐛 Bug fix
- [ ] ✨ New feature (Raga, model improvement, new UI component)
- [ ] 🎼 Dataset contribution (MIDI/MusicXML/annotations)
- [ ] 📖 Documentation / blog post
- [ ] 🔧 Chore (CI, dependencies, config)
- [ ] 🚀 Performance improvement

## Related Issues

Closes # <!-- issue number -->

---

## Testing

### Python changes
- [ ] `ruff check model/ data/ app.py` passes with zero errors
- [ ] `pytest test/ -v` passes locally
- [ ] Added tests for new functionality in `test/`

### Frontend changes
- [ ] `npm run build` succeeds with zero errors
- [ ] Changes visually verified at `npm run dev`

### Dataset contributions
- [ ] MIDI files placed in correct Melakarta namespace (`data/DeepRaaga-Dataset/Melakarta/<ID>_<Name>/midi/`)
- [ ] Arohana/Avarohana rules of the Raga are strictly respected
- [ ] `python data/melakarta_init.py` runs without errors

---

## Checklist

- [ ] My changes follow the **Music-as-Code** philosophy
- [ ] I have updated `CHANGELOG.md` under `[Unreleased]`
- [ ] I have read [CONTRIBUTING.md](../CONTRIBUTING.md)
- [ ] My branch is named according to the convention (`feature/`, `fix/`, `data/`, `docs/`)

---

## Screenshots / Audio Samples

<!-- If your change affects the UI or dataset, add a screenshot or link to a sample audio file -->
