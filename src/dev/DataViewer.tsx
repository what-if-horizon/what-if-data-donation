import React, { useEffect, useMemo, useRef, useState } from "react";
import JSZip from "jszip";

export interface PreviewFile {
  content: any;
  name: string;
  message?: string;
}

interface Props {
  files: File | File[];
  selectedFile: PreviewFile | null;
  setSelectedFile: (file: PreviewFile) => void;
}

export function FileTree({ files, selectedFile, setSelectedFile }: Props) {
  const [fileTree, setFileTree] = useState<FileTree[] | null>(null);
  const [search, setSearch] = useState("");
  const fileCache = useRef<Record<string, PreviewFile>>({});
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const f = Array.isArray(files) ? files : [files];
    fileCache.current = {};
    createFileTree(f).then((fileTree) => {
      setFileTree(fileTree);
      if (fileTree.length === 1) onSelect(fileTree[0].fullname);
    });
  }, [files]);

  async function onSelect(fullname: string) {
    // currently only supports single file upload
    const file = Array.isArray(files) ? files[0] : files;
    if (!fileCache.current[fullname]) {
      const content = await readFile(file, fullname);
      fileCache.current[fullname] = { content, name: fullname };
    }
    setSelectedFile(fileCache.current[fullname]);
  }

  if (!fileTree) return null;

  return (
    <div>
      <div className="p-3 rounded mx-auto mt-6 w-[800px] mx-w-full">
        <div className="flex items-center gap-1      ">
          <input
            type="text"
            placeholder="search"
            className="border  rounded  p-1  w-full"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />
          {search ? (
            <button
              onClick={() => setSearch("")}
              className="border bg-primary text-white rounded px-3 p-1 ml-auto mr-6 items-center flex gap-1"
            >
              {"Clear"}
            </button>
          ) : null}
        </div>
        <div className="h-3" />
        {fileTree.map((file) => {
          if (file.name.startsWith(".")) return null;
          if (search && !file.fullname.includes(search)) return null;
          const cl = file.isFile
            ? "underline font-bold cursor-pointer"
            : " text-primary mt-2 cursor-zoom-in ";
          return (
            <div
              key={file.fullname}
              style={{ marginLeft: (file.level - 1) * 20 }}
              className={`${cl}`}
              onClick={() => {
                if (!file.isFile) {
                  setSearch(file.dir);
                } else {
                  setLoading(true);
                  onSelect(file.fullname).finally(() => setLoading(false));
                }
              }}
            >
              <span>{file.name + (file.isFile ? "" : "/")}</span>
            </div>
          );
        })}
      </div>
    </div>
  );
}

function inferFileType(filename: string) {
  if (filename.endsWith(".json")) return "json";
  // if (filename.endsWith(".html")) return "html";
  // if (filename.endsWith(".csv")) return "csv";
  return "txt";
}

interface FileTree {
  name: string;
  level: number;
  dir: string;
  fullname: string;
  isFile: boolean;
}

async function createFileTree(files: File[]) {
  const fileTree: FileTree[] = [];

  for (let i = 0; i < files.length; i++) {
    const file = files[i];
    const type = file.type;

    if (type === "application/zip") {
      const zip = new JSZip();
      const zipFile = await zip.loadAsync(file);
      const filesArray = Object.entries(zipFile.files)
        .map(([name, file]) => ({
          name,
          file,
        }))
        .sort((a, b) => {
          const aLevel = a.name.split("/").length;
          const bLevel = b.name.split("/").length;
          return a.name.localeCompare(b.name) || aLevel - bLevel;
        });

      let seenPath = new Set<string>();
      for (const { file, name } of filesArray) {
        const relativePath = name;
        const paths = relativePath.split("/");

        for (let i = 1; i < paths.length; i++) {
          const path = paths.slice(1, i + 1).join("/");

          const isLast = i === paths.length - 1;
          const isDir = file.dir;
          const isFile = isLast && !isDir;

          if (!seenPath.has(path)) {
            fileTree.push({
              name: paths[i],
              level: i + 1,
              dir: path,
              fullname: isFile ? name : path,
              isFile,
            });
            seenPath.add(path);
          }
        }
      }
    } else {
      fileTree.push({
        name: file.name,
        level: 0,
        dir: "",
        fullname: file.name,
        isFile: true,
      });
    }
  }
  return fileTree;
}

export function RenderRaw({ file }: { file: PreviewFile }) {
  const typeDict = useRef<Record<string, string | null>>({});
  const [type, setType] = useState<string | null>(null);
  const [showAll, setShowAll] = useState(false);
  let abbreviated = false;

  useEffect(() => {
    if (typeDict.current[file.name] === undefined) {
      typeDict.current[file.name] = inferFileType(file.name);
    }
    setShowAll(false);
    changeType(typeDict.current?.[file.name] || "txt");
  }, [file]);

  if (!file?.content) return null;

  function changeType(type: string) {
    typeDict.current[file.name] = type;
    setType(type);
  }

  function shorten(text: string) {
    const n = 10000;
    if (text.length > n && !showAll) {
      abbreviated = true;
      return text.slice(0, n) + "...";
    }
    return text;
  }

  function renderType() {
    if (type === "json") {
      return (
        <pre>{shorten(JSON.stringify(JSON.parse(file.content), null, 2))}</pre>
      );
    }
    if (type === "html") {
      return <pre>{shorten(file.content)}</pre>;
    }
    if (type === "csv") {
      return <pre>{file.content}</pre>;
    }
    return <pre>{shorten(file.content)}</pre>;
  }

  const fileWithoutRoot = file.name.split("/").slice(1).join("/");

  return (
    <div className="flex flex-col gap-6">
      <div className="mx-auto text-primary font-bold">{fileWithoutRoot}</div>
      <div className="mx-auto flex gap-3 select-none">
        <RadioTypeItem type="json" currentType={type} onChange={changeType} />
        {/* <RadioTypeItem type="html" currentType={type} onChange={changeType} />
        <RadioTypeItem type="csv" currentType={type} onChange={changeType} /> */}
        <RadioTypeItem type="txt" currentType={type} onChange={changeType} />
      </div>
      <div className="max-w-full overflow-auto">
        <div className="p-3">{renderType()}</div>
      </div>
      {abbreviated ? (
        <button
          onClick={() => setShowAll(true)}
          className="bg-primary text-white py-1 px-2 w-max rounded mx-auto"
        >
          Show full document
        </button>
      ) : null}
    </div>
  );
}

function RadioTypeItem({
  type,
  currentType,
  onChange,
}: {
  type: string;
  currentType: string | null;
  onChange: (type: string) => void;
}) {
  const cl = currentType === type ? "bg-primary text-white" : "bg-white";
  return (
    <button
      onClick={() => onChange(type)}
      className={`${cl} w-20 rounded border`}
    >
      {type}
    </button>
  );
}

async function readFile(file: File, path: string) {
  if (file.type === "application/zip") {
    const zip = new JSZip();
    return zip.loadAsync(file).then((zf) => {
      return zf.file(path)?.async("text");
    });
  }

  // If file is not zipped, use FileReader API, but return as promise
  // for consistency
  var reader = new FileReader();
  return new Promise((resolve, reject) => {
    reader.onerror = () => {
      reader.abort();
      reject(new DOMException("Problem parsing input file."));
    };

    reader.onload = () => {
      resolve(reader.result);
    };
    reader.readAsText(file);
  });
}
