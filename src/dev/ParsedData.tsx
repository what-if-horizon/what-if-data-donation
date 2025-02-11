import { useEffect, useState } from "react";
import { Payload, PayloadDonate } from "../framework/types/commands";
import {
  PropsUIPromptConsentForm,
  PropsUIPromptConsentFormTable,
} from "../framework/types/prompts";
import { ConsentForm } from "../framework/visualisation/react/ui/prompts/consent_form";
import { Loader } from "../framework/visualisation/react/ui/visualization_plugin/ui/loader";
import usePyodideWorker, { ImportResult } from "./usePyodideWorker";

export function ParsedData({
  fileInput,
  script,
}: {
  fileInput: File;
  script: string;
}) {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<ImportResult>({
    consentForm: null,
    prints: [],
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
    if (!result.consentForm)
      return <pre className="text-delete">No data generated</pre>;
    return <MockConsentForm {...result.consentForm} />;
  }

  return (
    <div className="mt-9 p-6 grid grid-cols-1 gap-12 lg:grid-cols-[1fr,2fr] lg:gap-6">
      <PrintLines prints={result.prints} />
      {render()}
    </div>
  );
}

function MockConsentForm(consentFormProps: PropsUIPromptConsentForm) {
  const locale = "en";

  function fakeResolve(payload: Payload) {
    if (payload.__type__ === "PayloadDonate") {
      alert("You donated!!! jeeeyy!!! (add more usefull stats here)");
    } else {
      alert("Y u no donate :(");
    }
  }

  return (
    <div className="flex flex-col w-full">
      <ConsentForm
        {...consentFormProps}
        locale={locale}
        resolve={fakeResolve}
      />
    </div>
  );
}

function PrintLines({ prints }: { prints: string[] }) {
  const lines = prints.map((line) => {
    if (line.trim().length === 0) return null;
    return (
      <pre
        key={line}
        className="list-item p-1 my-1 rounded text-tertiary whitespace-pre-wrap break-words max-w-full  bg-white/5"
      >
        {line}
      </pre>
    );
  });

  return (
    <div className="bg-grey1 text-white p-3 rounded overflow-auto  ">
      <h4 className="text-lg font-bold mb-4">Print console</h4>
      <div className=" flex flex-col">{lines}</div>
    </div>
  );
}
