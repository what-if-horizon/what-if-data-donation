import { useCallback, useEffect, useRef } from "react";

const worker = new Worker("/src/devPyodideWorker.js");

const initializedWorker = new Promise<Worker>((resolve) => {
  worker.onmessage = (event) => {
    if (event.data.type === "initialiseDone") {
      resolve(worker);
    }
  };
});

window.addEventListener("beforeunload", () => {
  worker.terminate();
});

export default function usePyodideWorker() {
  const messageId = useRef(0);

  useEffect(() => {
    worker.postMessage({ type: "initialise" });
  }, []);

  const runImportScript = useCallback(
    async (script: string, fileList: FileList) => {
      const w = await initializedWorker;
      const id = messageId.current++;

      w.postMessage({ type: "import", id, script, fileList });

      return new Promise((resolve, reject) => {
        w.addEventListener("message", function listener(event) {
          if (event.data.id !== id) return;
          w.removeEventListener("message", listener);
          if (event.data.type === "importDone") resolve(event.data.table);
          if (event.data.type === "importFailed") reject(event.data.error);
          reject("invalid response type: " + event.data.type);
        });
      });
    },
    [],
  );

  return { runImportScript };
}
