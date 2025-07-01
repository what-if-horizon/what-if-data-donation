let pyScript;

onmessage = (event) => {
  const { eventType, path } = event.data;
  switch (eventType) {
    case "initialise":
      initialise(path).then(() => {
        self.postMessage({ eventType: "initialiseDone" });
      });
      break;

    case "firstRunCycle":
      pyScript = self.pyodide.runPython(
        `port.start(${event.data.sessionId}, "${event.data.platform || ""}")`,
      );
      runCycle(null);
      break;

    case "nextRunCycle":
      const { response } = event.data;
      unwrap(response).then((userInput) => {
        runCycle(userInput);
      });
      break;

    default:
      console.log("[ProcessingWorker] Received unsupported event: ", eventType);
  }
};

function runCycle(payload) {
  console.log("[ProcessingWorker] runCycle " + JSON.stringify(payload));
  try {
    scriptEvent = pyScript.send(payload);
    self.postMessage({
      eventType: "runCycleDone",
      scriptEvent: scriptEvent.toJs({
        create_proxies: false,
        dict_converter: Object.fromEntries,
      }),
    });
  } catch (error) {
    self.postMessage({
      eventType: "runCycleDone",
      scriptEvent: generateErrorMessage(error.toString()),
    });
  }
}

function unwrap(response) {
  console.log(
    "[ProcessingWorker] unwrap response: " + JSON.stringify(response.payload),
  );
  const directoryName = "/file-input";
  return new Promise((resolve) => {
    switch (response.payload.__type__) {
      case "PayloadFile":
        const file = response.payload.value;
        copyFileToPyFS([file], directoryName);
        resolve({
          __type__: "PayloadString",
          value: `${directoryName}/${file.name}`,
        });
        break;

      case "PayloadFileArray":
        const filePaths = [];
        const files = response.payload.value;
        for (const file of files) {
          filePaths.push(`${directoryName}/${file.name}`);
        }
        copyFileToPyFS(files, directoryName);
        resolve({ __type__: "PayloadStringArray", value: filePaths });
        break;

      default:
        resolve(response.payload);
    }
  });
}

function copyFileToPyFS(files, directoryName) {
  const pathStats = self.pyodide.FS.analyzePath(directoryName);
  if (!pathStats.exists) {
    self.pyodide.FS.mkdir(directoryName);
  } else {
    self.pyodide.FS.unmount(directoryName);
  }
  self.pyodide.FS.mount(
    self.pyodide.FS.filesystems.WORKERFS,
    {
      files: files,
    },
    directoryName,
  );
}

function initialise(path) {
  console.log("[ProcessingWorker] initialise");
  return startPyodide()
    .then((pyodide) => {
      self.pyodide = pyodide;
      return loadPackages();
    })
    .then(() => {
      return installPortPackage(path);
    });
}

function startPyodide() {
  importScripts("https://cdn.jsdelivr.net/pyodide/v0.24.0/full/pyodide.js");

  console.log("[ProcessingWorker] loading Pyodide");
  return loadPyodide({
    indexURL: "https://cdn.jsdelivr.net/pyodide/v0.24.0/full/",
  });
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

function installPortPackage(path) {
  console.log("[ProcessingWorker] load port package");
  return self.pyodide.runPythonAsync(`
    import micropip
    await micropip.install("${path}port-0.0.0-py3-none-any.whl", deps=False)
    import port
  `);
}

function generateErrorMessage(stacktrace) {
  return {
    __type__: "CommandUIRender",
    page: {
      __type__: "PropsUIPageError",
      stacktrace: stacktrace,
    },
  };
}
