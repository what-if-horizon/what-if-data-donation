import React, { useEffect, useMemo, useState } from "react";
import { OK } from "zod";
import JSZip from "jszip";

interface File {
  content: any;
  type: string;
  message?: string;
}

interface Props {
  files: FileList | null;
}

export function FileTree({ files }: Props) {
  if (!files) return null;
  const [fileTree, setFileTree] = useState<FileTree[] | null>(null);

  useEffect(() => {
    createFileTree(files).then((fileTree) => {
      setFileTree(fileTree);
    });
  }, [files]);

  if (!fileTree) return null;

  return (
    <div className="border">
      {fileTree.map((file) => {
        return (
          <div key={file.fullname} style={{ marginLeft: file.level * 30 }}>
            {file.name}
          </div>
        );
      })}
    </div>
  );
}

interface FileTree {
  name: string;
  level: number;
  dir: string;
  fullname: string;
  isFile: boolean;
}

async function createFileTree(files: FileList) {
  const fileTree: FileTree[] = [];

  for (let i = 0; i < files.length; i++) {
    const file = files[i];
    const type = file.type;

    if (type === "application/zip") {
      const zip = new JSZip();
      const zipFile = await zip.loadAsync(file);
      const orderedFiles = Object.keys(zipFile.files).sort((a, b) => {
        const aLevel = a.split("/").length;
        const bLevel = b.split("/").length;
        return aLevel - bLevel || a.localeCompare(b);
      });
      console.log(zipFile.files);

      let lastDir = "";
      for (const relativePath of orderedFiles) {
        const paths = relativePath.split("/");
        const folders = paths.slice(1, paths.length - 1);
        const dir = folders.join("/");
        const file = paths[paths.length - 1];

        if (dir !== lastDir) {
          fileTree.push({
            name: dir,
            level: folders.length,
            dir,
            fullname: dir,
            isFile: false,
          });
          lastDir = dir;
        }

        fileTree.push({
          name: file,
          level: folders.length + 1,
          dir: dir,
          fullname: relativePath,
          isFile: true,
        });
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

function recursiveFileTree(
  parentMap: Record<string, FileTree[]>,
  dir: string,
): FileTree[] {
  const files = parentMap[dir].sort((a, b) => a.name.localeCompare(b.name));
  if (!files) return [];
  return files.map((file) => {
    return {
      ...file,
      children: recursiveFileTree(parentMap, file.dir),
    };
  });
}

const DataViewer = (file: File) => {
  const [showRaw, setShowRaw] = useState(false);

  if (!file?.content) return null;

  return (
    <div>
      <div className="flex">
        <button
          content={showRaw ? "Hide raw data" : "Show raw data"}
          onClick={() => setShowRaw(!showRaw)}
        />
        {file.message ? file.message : null}
      </div>

      {showRaw ? (
        <div>
          <RenderRaw {...file} />
        </div>
      ) : null}
      <br />
    </div>
  );
};

const RenderRaw = (file: File) => {
  if (!file?.content) return null;
  switch (file.type) {
    case "json":
      return (
        <>
          <pre>{JSON.stringify(file.content, null, 2)}</pre>
        </>
      );
    case "html":
      return (
        <>
          <pre>{file.content}</pre>
        </>
      );
    case "csv":
      return (
        <>
          <pre>{file.content}</pre>
        </>
      );
    default:
      return null;
  }
};

export default DataViewer;
