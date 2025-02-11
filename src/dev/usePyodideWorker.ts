import { useCallback, useEffect, useRef, useState } from "react";
import hash from "object-hash";
import { PropsUIPromptConsentForm } from "../framework/types/prompts";

const worker = new Worker("/src/dev/pyodideWorker.js");

export type ParsedTable = Record<string, string | number | boolean>[];
export type ImportResult = {
  error: string | null;
  consentForm: PropsUIPromptConsentForm | null;
  prints: string[];
};

const initializedWorker = new Promise<Worker>((resolve) => {
  worker.onmessage = (event) => {
    if (event.data.type === "initialise" && event.data.status === "done") {
      resolve(worker);
    }
  };
});

window.addEventListener("beforeunload", () => {
  worker.terminate();
});

export default function usePyodideWorker() {
  const activeIds = useRef<Set<string>>(new Set());
  const [initializing, setInitializing] = useState(true);

  useEffect(() => {
    worker.postMessage({ type: "initialise" });
    initializedWorker.then(() => setInitializing(false));
  }, []);

  const runImportScript = useCallback(
    async (script: string, fileInput: File[] | File): Promise<ImportResult> => {
      const id = hash({ script, fileInput });
      const w = await initializedWorker;
      if (!activeIds.current.has(id)) {
        w.postMessage({
          type: "import",
          id,
          script,
          fileInput,
        });
        activeIds.current.add(id);
      }

      return new Promise((resolve) => {
        w.addEventListener("message", function listener(event) {
          if (event.data.id !== id) return;
          if (event.data.type !== "import") return;

          w.removeEventListener("message", listener);
          resolve({
            consentForm: event.data.consentForm,
            prints: event.data.prints,
            error: event.data.error,
          });
          activeIds.current.delete(id);
        });
      });
    },
    [],
  );

  return { runImportScript, initializing };
}
