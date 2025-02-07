import { useCallback, useEffect, useRef } from "react";

const worker = new Worker("/src/pyodideWorker.js");

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
  const activeIds = useRef<Set<string>>(new Set());

  useEffect(() => {
    worker.postMessage({ type: "initialise" });
  }, []);

  const runImportScript = useCallback(
    async (id: string, script: string, fileList: FileList) => {
      const w = await initializedWorker;
      if (!activeIds.current.has(id)) {
        w.postMessage({ type: "import", id, script, fileList });
        activeIds.current.add(id);
      }

      return new Promise((resolve, reject) => {
        w.addEventListener("message", function listener(event) {
          if (event.data.id !== id) return;
          w.removeEventListener("message", listener);
          if (event.data.type === "importDone") resolve(event.data.table);
          if (event.data.type === "importFailed") reject(event.data.error);
          activeIds.current.delete(id);
        });
      });
    },
    [],
  );

  return { runImportScript };
}
