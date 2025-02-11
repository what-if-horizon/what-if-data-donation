import { useEffect, useState } from "react";
import { Loader } from "../framework/visualisation/react/ui/visualization_plugin/ui/loader";
import usePyodideWorker, {
  ImportResult,
  ParsedTable,
} from "./usePyodideWorker";

export function ParsedData({
  fileInput,
  script,
}: {
  fileInput: File;
  script: string;
}) {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<ImportResult>({
    tables: [] as ParsedTable[],
    prints: [] as string[],
    error: null,
  });
  const { runImportScript } = usePyodideWorker();

  useEffect(() => {
    if (!fileInput) return;
    setLoading(true);
    runImportScript(script, fileInput)
      .then(setResult)
      .finally(() => setLoading(false));
  }, [fileInput, script, runImportScript]);

  function render() {
    if (loading) return <Loader />;
    if (result.error) return <pre className="text-delete">{result.error}</pre>;
    return <div>tables here</div>;
  }

  return (
    <div className="mt-9 p-6 flex flex-col gap-12">
      <PrintLines prints={result.prints} />
      {render()}
    </div>
  );
}

function PrintLines({ prints }: { prints: string[] }) {
  const lines = prints.map((line) => {
    if (line.trim().length === 0) return null;
    return (
      <li key={line} className="list-item">
        {line}
      </li>
    );
  });

  return (
    <div className="bg-black text-white p-3 rounded">
      <h4 className="text-lg font-bold mb-4">
        You can use print() for debugging
      </h4>
      <ul className="list-disc list-inside">{lines}</ul>
    </div>
  );
}
