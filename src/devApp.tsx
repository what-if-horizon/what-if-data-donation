import { useEffect, useRef, useState } from "react";
import usePyodideWorker from "./usePyodideWorker";

// eslint-disable-next-line import/no-webpack-loader-syntax
import script from "./framework/processing/py/port/platform_tables/facebook.py?raw";

type Table = Record<string, string | number | boolean>[];

export default function APP() {
  const [tables, setTables] = useState<Table[] | null>(null);
  const [error, setError] = useState<string>("");
  const [fileInput, setFileInput] = useState<FileList | null>(null);
  const { runImportScript } = usePyodideWorker();

  useEffect(() => {
    if (!fileInput) return;
    runImportScript(script, fileInput)
      .then((tables) => setTables(tables as Table[]))
      .catch(setError);
  }, [fileInput, runImportScript]);

  return (
    <div>
      <FileInputForm fileInput={fileInput} setFileInput={setFileInput} />
      {error && <div>{error}</div>}
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

// function usePyodideWorker() {
//   const [worker, setWorker] = useState<Promise<Worker>>(new Promise(() => {})); // Initial pending promise
//   const messageId = useRef(0);
//   const workerRef = useRef<Worker | null>(null);
//   const isMounted = useRef(true);

//   useEffect(() => {
//     console.log("rerender");
//     if (workerRef.current) return;

//     workerRef.current = new Worker("/src/devPyodideWorker.js");

//     const initializedWorker = new Promise<Worker>((resolve) => {
//       newWorker.onmessage = (event) => {
//         if (event.data.type === "initialiseDone") {
//           console.log("initialiseDone");
//           resolve(newWorker);
//         }
//       };
//     });

//     setWorker(initializedWorker);
//     if (workerRef.current === null)
//       newWorker.postMessage({ type: "initialise" });

//     return () => {
//       initializedWorker.then((worker) => worker.terminate());
//     };
//   }, []);

//   async function isInitialized() {}

//   async function runImportScript(script: string, file: File) {
//     console.log("run import");
//     const w = await worker;
//     const id = messageId.current++;

//     w.postMessage({ type: "import", id, script });

//     return new Promise((resolve, reject) => {
//       w.addEventListener("message", function listener(event) {
//         if (event.data.id !== id) return;
//         w.removeEventListener("message", listener);
//         if (event.data.type === "importDone") resolve(event.data.table);
//         if (event.data.type === "importError") reject(event.data.error);
//       });
//     });
//   }

//   return { runImportScript };
// }
