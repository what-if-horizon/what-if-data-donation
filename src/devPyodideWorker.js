let initialized = false;

onmessage = (event) => {
  const { type } = event.data;
  switch (type) {
    case "initialise":
      if (!initialized) initialise();
      initialized = true;
      break;

    case "import":
      const { script, id, fileList } = event.data;
      runImport(id, script, fileList);
      break;

    default:
      console.log("[ProcessingWorker] Received unsupported event: ", type);
  }
};

async function initialise() {
  await loadPyodide();
  await loadPackages();
  await installPortPackage();
  self.postMessage({ type: "initialiseDone" });
}

async function runImport(id, script, fileList) {
  const dir = `/data_${id}`;

  writeToWORKERFS(dir, fileList);

  try {
    const scriptWithIO = `import os\nos.chdir("${dir}")\n${script}`;
    pyodide.runPython(scriptWithIO);
    const tables = self.pyodide.globals.get("tables");
    self.postMessage({ type: "importDone", id, tables });
  } catch (e) {
    self.postMessage({ type: "importFailed", id, error: e.message });
  } finally {
    rmFromWORKERFS(dir);
  }
}

async function runScript(script) {
  console.log("kutpyghon");
  pyodide.runPython("x = 5");
  pyodide.runPython("print(x)");

  const scriptWithIO = `import os\nos.chdir("${dir}")\n${script}`;
  pyodide.runPython(scriptWithIO);

  const tables = self.pyodide.globals.get("tables");
}

function writeToWORKERFS(dir, fileList) {
  const path = self.pyodide.FS.analyzePath(dir);

  pyodide.runPython(`import os; print(os.listdir('/'))`);

  if (!path.exists) self.pyodide.FS.mkdir(dir);

  self.pyodide.FS.mount(
    self.pyodide.FS.filesystems.WORKERFS,
    { files: fileList },
    dir,
  );

  pyodide.runPython(`import os; print(os.listdir('/${dir}'))`);
}
function rmFromWORKERFS(dir) {
  try {
    self.pyodide.FS.unmount(dir);
    // self.pyodide.FS.unlink(dir);
    pyodide.runPython(`import os; print(os.listdir('/'))`);
    pyodide.runPython(`import os; print(os.listdir('/${dir}'))`);
  } catch (e) {
    console.log(e);
  }
}

async function loadPyodide() {
  const pyodideModule = await import(
    "https://cdn.jsdelivr.net/pyodide/v0.26.0/full/pyodide.mjs"
  );
  self.pyodide = await pyodideModule.loadPyodide();
}

async function loadPackages() {
  console.log("[ProcessingWorker] loading packages");
  await self.pyodide.loadPackage(["micropip", "numpy", "pandas"]);

  // can also install anything on pypi with wheels
  return await self.pyodide.runPythonAsync(`
     import micropip
     await micropip.install("jsonpath-ng")
  `);
}

async function installPortPackage() {
  console.log("[ProcessingWorker] load port package");
  return await self.pyodide.runPythonAsync(`
    import micropip
    await micropip.install("/port-0.0.0-py3-none-any.whl", deps=False)
    import port
  `);
}
