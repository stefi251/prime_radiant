# prime_radiant

A one-line summary of what this project does.

## Quick start

### 1. Develop in JupyterLab
```bash
cd ~/projects/prime_radiant
./start-lab.sh
```

This opens JupyterLab with Marimo’s sidebar plugin (snippets, AI, reactive tests). Edit your code in `src/prime_radiant/`, write tests in `tests/`, and explore notebooks as usual.

### 2. Run the Marimo Reactive Demo
```bash
source .venv/bin/activate          # if not already activated
marimo run notebooks/interactive_demo.py
```

This launches a standalone Marimo app in your browser. You get:
- A slider that auto-recalculates dependent cells.
- An interactive scatter plot with click-to-select.
- An AI Q&A prompt powered by Marimo.
