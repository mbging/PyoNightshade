# PyoNightshade
## Pyodide + Web Worker + Matplotlib + Cartopy

A sample project to setup Pyodide with built in packages and a Web Worker, visible at https://pyo-nightshade.vercel.app/.

Below is a brief explaination of the code breakdown.

### plot\.py

A modified Cartopy Nightshade [sample](https://scitools.org.uk/cartopy/docs/latest/gallery/lines_and_polygons/nightshade.html#sphx-glr-gallery-lines-and-polygons-nightshade-py).

If running in Pyodide:
- the drawing is exported to a base 64 string to be loaded as an image in the main thread of the browser
- the `AGG` Matplotlib backend is used when running in a Web Worker (see the [open issue](https://github.com/pyodide/matplotlib-pyodide/issues/6) as of the creation of this project)

If running in a regular Python environment, the drawing is displayed using the default Matplotlib backend.

### worker.js
1. Import Pyodide
1. Initialize Pyodide
1. Load packages
1. Import the Python code as a module
1. Render images at intervals

### index.html
Provide a placeholder to display the data coming from the Worker event.

## Running Python locally
From a shell:
```bash
# Create a Python virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.dev.txt
python plot.py
```
The javascript and html code can be tested after running ```python3 -m http.server``` and visiting ```http://localhost:8000```.