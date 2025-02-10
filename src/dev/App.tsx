import { useEffect, useRef, useState } from "react";
import usePyodideWorker from "./usePyodideWorker";

// eslint-disable-next-line import/no-webpack-loader-syntax
import script from "../framework/processing/py/port/platform_tables/facebook.py?raw";
import { FileTree, PreviewFile, RenderRaw } from "./DataViewer";
import { FileInputMultiple } from "../framework/visualisation/react/ui/prompts/file_input_multiple";
import { FileInput } from "../framework/visualisation/react/ui/prompts/file_input";
import { Page } from "../framework/visualisation/react/ui/pages/templates/page";
import { Payload } from "../framework/types/commands";

type Table = Record<string, string | number | boolean>[];

export default function App() {
  const [fileInput, setFileInput] = useState<File | null>(null);
  const [tab, setTab] = useState<"Raw data" | "Parsed data">("Raw data");

  if (!fileInput)
    return <FileInputForm fileInput={fileInput} setFileInput={setFileInput} />;

  function render() {
    if (!fileInput) return null;
    if (tab === "Raw data") return <RawData fileInput={fileInput} />;
    if (tab === "Parsed data") return <ParsedData fileInput={fileInput} />;
  }

  return (
    <div>
      <div className="flex flex gap-3 mt-6 w-full items-center px-6 ">
        <button
          onClick={() => setTab("Raw data")}
          className={`${tab === "Raw data" ? "bg-primary text-white" : ""} border rounded p-1 px-3`}
        >
          Raw data
        </button>
        <button
          onClick={() => setTab("Parsed data")}
          className={`${tab === "Parsed data" ? "bg-primary text-white" : ""} border rounded p-1 px-3`}
        >
          Parsed Data
        </button>
        <button
          onClick={() => setFileInput(null)}
          className="border bg-primary text-white rounded px-3 p-1 ml-auto  items-center flex gap-1"
        >
          {" Go back to file upload"}
        </button>
      </div>
      {render()}
    </div>
  );
}

function RawData({ fileInput }: { fileInput: File }) {
  const [selected, setSelected] = useState<PreviewFile | null>(null);

  if (selected) return <ShowFile file={selected} setSelected={setSelected} />;

  return (
    <FileTree
      files={fileInput}
      selectedFile={selected}
      setSelectedFile={setSelected}
    />
  );
}

function ParsedData({ fileInput }: { fileInput: File }) {
  const [tables, setTables] = useState<Table[] | null>(null);
  const [error, setError] = useState<string>("");
  const { runImportScript } = usePyodideWorker();

  useEffect(() => {
    if (!fileInput) return;
    runImportScript("data", script, fileInput)
      .then((tables) => setTables(tables as Table[]))
      .catch(setError);
  }, [fileInput, runImportScript]);

  console.log(tables);
  console.log(error);

  if (error)
    return (
      <div>
        <pre>{error}</pre>
      </div>
    );

  return null;
}

function ShowFile({
  file,
  setSelected,
}: {
  file: PreviewFile;
  setSelected: (file: PreviewFile | null) => void;
}) {
  const [type, setType] = useState<string | null>(null);
  return (
    <div className="flex flex-col gap-6 mt-6">
      <button
        onClick={() => setSelected(null)}
        className="border bg-primary text-white rounded px-3 p-1 mx-auto items-center flex gap-1"
      >
        {" Go back to files"}
      </button>
      <RenderRaw file={file} />
    </div>
  );
}

function FileInputForm({
  fileInput,
  setFileInput,
}: {
  fileInput: File | File[] | null;
  setFileInput: (fileInput: File) => void;
}) {
  function resolve(payload: Payload) {
    if (payload.__type__ === "PayloadFile") setFileInput(payload.value);
  }

  if (!fileInput) {
    return (
      <div className={"mx-auto w-[1000px] max-w-full p-6"}>
        <Page
          body={
            <FileInput
              resolve={resolve}
              description={""}
              extensions={""}
              locale={"en"}
            />
          }
        />
      </div>
    );
  }

  return null;
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
