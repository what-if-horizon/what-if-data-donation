let initialized = false;

onmessage = (event) => {
  const { type } = event.data;
  switch (type) {
    case "initialise":
      if (!initialized) initialise();
      initialized = true;
      break;

    case "import":
      const { script, id, fileInput } = event.data;
      runImport(id, script, fileInput);
      break;

    default:
      console.log("[ProcessingWorker] Received unsupported event: ", type);
  }
};

async function initialise() {
  await loadPyodide();
  await loadPackages();
  await installPortPackage();
  self.postMessage({ type: "initialise", status: "done" });
}

async function runImport(id, script, fileInput) {
  const dir = `/${id}`;
  files = Array.isArray(fileInput) ? fileInput : [fileInput];
  writeToWORKERFS(dir, files);

  const { error, consentForm, prints } = await runImportScript(
    dir,
    script,
    files,
  );

  self.postMessage({
    type: "import",
    status: "done",
    id,
    error,
    consentForm,
    prints,
  });
  rmFromWORKERFS(dir);
}

async function runImportScript(dir, script, fileInput) {
  const prints = [];
  try {
    // pass print function and filenames to python
    PRINTFUN = (text) => prints.push(text);
    FILENAMES = files.map((f) => `${f.name}`);
    namespace = pyodide.toPy({ FILENAMES, PRINTFUN });

    scriptLines = [
      "from sys import stdout",
      "import json",
      "import requests",
      "from os import chdir",
      "stdout.write = PRINTFUN",
      `chdir("${dir}")`,
      script,
      "DONATION_FLOW = create_donation_flow(FILENAMES)",
      "DONATION_FLOW_DICT = DONATION_FLOW.toDict()",
    ];
    await pyodide.runPythonAsync(scriptLines.join("\n\n"), {
      globals: namespace,
    });

    const consentForm = namespace.get("DONATION_FLOW_DICT").toJs({
      create_proxies: false,
      dict_converter: Object.fromEntries,
    });

    return { error: null, consentForm, prints };
  } catch (e) {
    return { error: e.message, consentForm: null, prints };
  }
}

function writeToWORKERFS(dir, files) {
  const path = self.pyodide.FS.analyzePath(dir);
  if (!path.exists) self.pyodide.FS.mkdir(dir);

  self.pyodide.FS.mount(self.pyodide.FS.filesystems.WORKERFS, { files }, dir);
}

function rmFromWORKERFS(dir) {
  self.pyodide.FS.unmount(dir);
}

async function loadPyodide() {
  const pyodideModule = await import(
    "https://cdn.jsdelivr.net/pyodide/v0.26.0/full/pyodide.mjs"
  );
  self.pyodide = await pyodideModule.loadPyodide();
}

async function loadPackages() {
  console.log("[ProcessingWorker] loading packages");
  await self.pyodide.loadPackage(["micropip", "numpy", "pandas","requests"]);

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
