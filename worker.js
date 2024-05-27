self.importScripts("https://cdn.jsdelivr.net/pyodide/v0.25.1/full/pyodide.js");

async function renderPlot() {
  console.log("Rendering...");
  const imgStr = self.pkg.render();
  postMessage(imgStr);
}

async function setup() {
  postMessage("log_Loading Pyodide...");
  self.pyodide = await loadPyodide();
  postMessage("log_Loading packages...");
  await self.pyodide.loadPackage(["matplotlib", "cartopy"]);
  postMessage("log_Loading Python code...");
  await self.pyodide.runPythonAsync(`
    from pyodide.http import pyfetch
    response = await pyfetch("plot.py")
    with open("plot.py", "wb") as f:
        f.write(await response.bytes())
    `);
  self.pkg = self.pyodide.pyimport("plot");
  postMessage("log_Done! Waiting for first image...");

  setInterval(renderPlot, 1);
}

self.onmessage = function (event) {
  if (event.data === "start") {
    setup();
  }
};
