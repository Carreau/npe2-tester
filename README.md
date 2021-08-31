# npe2-tester

Example plugin implementing the new plugin manifest

## Installation

```
git clone https://github.com/tlambert03/npe2-tester.git
cd npe2-tester
pip install -e .
```

## Usage

To use this plugin, you'll need to have the main branch of [`npe2`](https://github.com/tlambert03/npe2) installed ... and the `npe2-support` branch of napari installed from [`tlambert03/napari@npe2-support`](https://github.com/tlambert03/napari/tree/npe2-support)

The plugin manifest is declared in [`napari.yaml`](https://github.com/tlambert03/npe2-tester/blob/main/npe2_tester/napari.yaml)

The main entry point where the plugin gets activated is [`_activate.py`](https://github.com/tlambert03/npe2-tester/blob/main/npe2_tester/_activate.py)


