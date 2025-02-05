let pyScript;

onmessage = (event) => {
  const { type } = event.data;
  switch (type) {
    case "initialise":
      initialise().then(() => {
        self.postMessage({ type: "initialiseDone" });
      });
      break;

    case "import":
      const { script, id, file } = event.data;

      try {
        self.pyodide.runPython(`
         import js
         from js import file
          ${script}
      `);

        const tables = self.pyodide.globals.get("tables");
        self.postMessage({ type: "importDone", id, tables });
      } catch (error) {
        self.postMessage({ type: "importFailed", id, error });
      }
      break;

    default:
      console.log("[ProcessingWorker] Received unsupported event: ", type);
  }
};

function initialise() {
  console.log("[ProcessingWorker] initialise");
  return startPyodide()
    .then((pyodide) => {
      self.pyodide = pyodide;
      return loadPackages();
    })
    .then(() => {
      return installPortPackage();
    });
}

function startPyodide() {
  importScripts("https://cdn.jsdelivr.net/pyodide/v0.24.0/full/pyodide.js");

  console.log("[ProcessingWorker] loading Pyodide");
  return loadPyodide({
    indexURL: "https://cdn.jsdelivr.net/pyodide/v0.24.0/full/",
  });
}

function loadPackages() {
  console.log("[ProcessingWorker] loading packages");
  return self.pyodide.loadPackage(["micropip", "numpy", "pandas"]);
}

function installPortPackage() {
  console.log("[ProcessingWorker] load port package");
  return self.pyodide.runPythonAsync(`
    import micropip
    await micropip.install("../../port-0.0.0-py3-none-any.whl", deps=False)
    import port
  `);
}
