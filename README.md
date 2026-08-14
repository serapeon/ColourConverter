# 🎨 ColourConverter 🖼️

Colourises black-and-white/greyscale photos using a pretrained deep-learning
model, run from a Jupyter notebook.

## Getting Started

### Run the Notebook

1. **Clone the repository**
   ```bash
   git clone git@github.com:serapeon/ColourConverter.git
   cd ColourConverter
   ```

2. **Set up the environment** (conda, Python 3.12)
   ```bash
   conda create -n open-cv python=3.12
   conda activate open-cv
   pip install opencv-python torch numpy
   ```

3. **Open `Colour.ipynb`** in Jupyter/VS Code, select the `open-cv` kernel, and
   run both cells top to bottom.

## How to Use

1. Set `image_path` in the first cell to the photo you want to colourise.
2. Run the notebook — it shows the original greyscale photo next to the
   AI-colourised result.
3. Tune `MAX_DIM` in the colourisation cell if you want sharper colour detail
   (slower) or faster results (coarser colour) — see the comment above it for
   the measured tradeoff.

## Features

- AI colourisation via a pretrained PyTorch model (`siggraph17`, from
  [richzhang/colorization](https://github.com/richzhang/colorization)),
  vendored locally in `colorizers/`
- Configurable resize (`MAX_DIM`) trading off speed vs. colour detail, instead
  of a hardcoded resolution
- Guards against a missing/unreadable image file crashing the whole kernel,
  and against re-running the colourisation cell with a stale/missing image
- PEP 257 (Google-style) docstrings throughout `colorizers/`

## Project Structure

```
Colour.ipynb            # notebook: load photo -> AI colourise -> display
colorizers/              # vendored PyTorch port of richzhang/colorization
├── __init__.py
├── base_color.py        # shared L/ab normalisation helpers
├── eccv16.py             # earlier model (superseded by siggraph17, kept for reference)
└── siggraph17.py         # active colourisation model
```

*(Note: `colorizers/` and the file names inside it keep the American spelling
from the upstream [richzhang/colorization](https://github.com/richzhang/colorization)
repo they're vendored from — only this README's prose uses British spelling.)*

## Development Notes

Built iteratively with Claude Code: migrated off OpenCV's Caffe DNN loader
after OpenCV 5 removed Caffe support entirely, ported to a PyTorch model with
the same original weights, then upgraded models again after finding the first
one gave washed-out/yellow-tinted results on a lot of photos. Along the way,
also fixed a kernel-crashing bug (a missing image file being passed straight
into OpenCV's native code) and diagnosed why certain blurry source photos
colourise worse than sharp ones.

Used two custom agents along the way, each modelled on an existing Java
counterpart from another project: a `python-code-reviewer` agent, which
caught a dead duplicate computation in `siggraph17.py` (removed, output is
byte-identical but faster) and a notebook cell-ordering bug (fixed with a
guard); and a `python-docstring-writer` agent, which added the docstrings
in `colorizers/`. The built-in `/security-review` command was also run
against the full set of changes — no security issues were found.

Built with Python, OpenCV & PyTorch | [github.com/serapeon](https://github.com/serapeon)

## Licence

This project is licensed under the [MIT Licence](LICENSE). You are free to
use, modify, and distribute this code, provided the original copyright notice
is retained.
