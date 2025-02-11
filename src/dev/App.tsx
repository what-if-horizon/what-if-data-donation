import { useEffect, useMemo, useRef, useState } from "react";
import usePyodideWorker from "./usePyodideWorker";

import { FileTree, PreviewFile, RenderRaw } from "./DataViewer";
import { FileInputMultiple } from "../framework/visualisation/react/ui/prompts/file_input_multiple";
import { FileInput } from "../framework/visualisation/react/ui/prompts/file_input";
import { Page } from "../framework/visualisation/react/ui/pages/templates/page";
import { Payload } from "../framework/types/commands";
import { ParsedData } from "./ParsedData";
import {
  IconLabelButton,
  PrimaryButton,
} from "../framework/visualisation/react/ui/elements/button";
import BackSvg from "../assets/images/back.svg";

// TODO: try to get these dynamicaly with import.meta.glob but without reloading the page
import fb_script from "../framework/processing/py/port/donation_flows/facebook_flow.py?raw";
import insta_script from "../framework/processing/py/port/donation_flows/instagram_flow.py?raw";
const scripts: Record<string, string> = {
  "../framework/processing/py/port/donation_flows/facebook_flow.py": fb_script,
  "../framework/processing/py/port/donation_flows/instagram_flow.py":
    insta_script,
};

// const scripts = import.meta.glob(
//   "../framework/processing/py/port/donation_flows/*.py",
// );

interface Script {
  name: string;
  file: string;
  content: string;
}

export default function App({ devScript }: { devScript: string }) {
  const [fileInput, setFileInput] = useState<File | null>(null);
  const [tab, setTab] = useState<"Raw data" | "Parsed data">("Parsed data");
  const [script, setScript] = useState<Script | null>(null);

  if (!fileInput)
    return (
      <DevInputForm
        fileInput={fileInput}
        setFileInput={setFileInput}
        script={script}
        setScript={setScript}
      />
    );

  function render() {
    if (!fileInput) return null;
    if (tab === "Raw data") return <RawData fileInput={fileInput} />;
    if (tab === "Parsed data") {
      const scriptContent = scripts[script?.file || ""];
      if (!script) return <div>loading script...</div>;
      return <ParsedData script={scriptContent} fileInput={fileInput} />;
    }
  }

  return (
    <div>
      <div className="flex  gap-3 mt-6 w-full items-center px-6 ">
        <PrimaryButton
          color={tab === "Raw data" ? "bg-primary text-white" : "bg-grey3"}
          onClick={() => setTab("Raw data")}
          label="Raw data"
        />
        <PrimaryButton
          color={tab === "Parsed data" ? "bg-primary text-white" : "bg-grey3"}
          onClick={() => setTab("Parsed data")}
          label="Parsed data"
        />
        <div className="ml-auto">
          <IconLabelButton
            onClick={() => setFileInput(null)}
            icon={BackSvg}
            label="Select script and data"
          />
        </div>
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

function ShowFile({
  file,
  setSelected,
}: {
  file: PreviewFile;
  setSelected: (file: PreviewFile | null) => void;
}) {
  const [type, setType] = useState<string | null>(null);
  return (
    <div className="flex flex-col gap-6 mt-6 px-6">
      <div className="ml-auto">
        <IconLabelButton
          onClick={() => setSelected(null)}
          icon={BackSvg}
          label="Go back to files"
        />
      </div>
      <RenderRaw file={file} />
    </div>
  );
}

function DevInputForm({
  fileInput,
  setFileInput,
  script,
  setScript,
}: {
  fileInput: File | File[] | null;
  setFileInput: (fileInput: File) => void;
  script: Script | null;
  setScript: (script: Script) => void;
}) {
  function resolve(payload: Payload) {
    if (payload.__type__ === "PayloadFile") setFileInput(payload.value);
  }

  const scriptFiles = useMemo(() => {
    return Object.keys(scripts).map((script) => {
      return {
        name: script.replace(/^.*[\\\/]/, "").replace(".py", ""),
        file: script,
      };
    });
  }, []);

  async function loadScript(name: string, file: string) {
    // const content = await import(file).then((module) => module.default);
    setScript({
      name,
      file,
      content: scripts[file],
    });
  }

  function chooseScript() {
    return (
      <div className="flex flex-col gap-3">
        <h3 className="text-lg font-bold">Choose an import script to test</h3>
        <div className="flex gap-3 items-center ">
          {scriptFiles.map(({ name, file }) => {
            return (
              <PrimaryButton
                color={
                  script?.name === name ? "bg-primary text-white" : "bg-grey3"
                }
                onClick={() => loadScript(name, file)}
                key={file}
                label={name.replaceAll("_", " ")}
              />
            );
          })}
        </div>
      </div>
    );
  }

  function chooseFile() {
    if (!script) return null;
    return (
      <div className="flex flex-col gap-3">
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

  if (!fileInput) {
    return (
      <div
        className={
          "flex flex-col gap-12 mx-auto w-[1000px] max-w-full p-6 mt-12"
        }
      >
        {chooseScript()}
        {chooseFile()}
      </div>
    );
  }

  return null;
}
