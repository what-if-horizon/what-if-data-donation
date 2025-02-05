import { useEffect, useRef, useState } from "react";

// eslint-disable-next-line import/no-webpack-loader-syntax
import script from "!!raw-loader!./framework/processing/py/port/platform_tables/facebook.py";

type Table = Record<string, string | number | boolean>[];

export default function APP() {
  const [tables, setTables] = useState<Table[] | null>(null);
  const [error, setError] = useState<Error | null>(null);
  const [fileInput, setFileInput] = useState<FileList | null>(null);
  const { runImportScript } = usePyodideWorker();
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (!fileInput) return;
    runImportScript(script, fileInput[0])
      .then((tables) => setTables(tables as Table[]))
      .catch(setError);
  }, [fileInput, runImportScript]);
  console.log(fileInput);

  return (
    <div>
      <FileInputForm fileInput={fileInput} setFileInput={setFileInput} />
    </div>
  );
}

function FileInputForm({
  fileInput,
  setFileInput,
}: {
  fileInput: FileList | null;
  setFileInput: (fileInput: FileList) => void;
}) {
  return (
    <form
      onSubmit={(e) => {
        e.preventDefault();
        if (fileInput) {
          setFileInput(fileInput);
        }
      }}
    >
      <input
        type="file"
        onChange={(e) => {
          if (e.target.files) {
            setFileInput(e.target.files);
          }
        }}
      />
      <button type="submit">Upload</button>
    </form>
  );
}

function usePyodideWorker() {
  const [worker, setWorker] = useState<Promise<Worker>>(new Promise(() => {})); // Initial pending promise
  const messageId = useRef(0);

  useEffect(() => {
    const newWorker = new Worker("devPyodideWorker.js");

    const initializedWorker = new Promise<Worker>((resolve) => {
      newWorker.onmessage = (event) => {
        if (event.data.eventType === "initialiseDone") {
          console.log("initialiseDone");
          resolve(newWorker);
        }
      };
    });

    setWorker(initializedWorker);
    newWorker.postMessage({ eventType: "initialise" });

    return () => {
      initializedWorker.then((worker) => worker.terminate());
    };
  }, []);

  async function runImportScript(script: string, file: File) {
    const w = await worker;
    const id = messageId.current++;

    w.postMessage({ eventType: "import", id, script });

    return new Promise((resolve, reject) => {
      w.addEventListener("message", function listener(event) {
        if (event.data.id !== id) return;
        w.removeEventListener("message", listener);
        if (event.data.type === "importDone") resolve(event.data.table);
        if (event.data.type === "importError") reject(event.data.error);
      });
    });
  }

  return { runImportScript };
}
