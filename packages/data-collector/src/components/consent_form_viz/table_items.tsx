import { useMemo } from "react";
import TextBundle from "@eyra/feldspar";
import { Translator } from "@eyra/feldspar";
import { TableWithContext } from "./types";
import UndoSvg from "./assets/images/undo.svg";

interface Props {
  table: TableWithContext;
  searchedTable: TableWithContext;
  handleUndo: () => void;
  locale: string;
}

export const TableItems = ({
  table,
  searchedTable,
  handleUndo,
  locale,
}: Props): JSX.Element => {
  const text = useMemo(() => getTranslations(locale), [locale]);

  const deleted = table.deletedRowCount;
  const n = table.body.rows.length;
  const searched = searchedTable.body.rows.length;
  const total = table.originalBody.rows.length - table.deletedRowCount;

  const nLabel = n.toLocaleString(locale, { useGrouping: true });
  const totalLabel = total.toLocaleString(locale, { useGrouping: true });
  const searchLabel = searched.toLocaleString(locale, { useGrouping: true });
  const deletedLabel =
    deleted.toLocaleString("en", { useGrouping: true }) + " " + text.deleted;

  function rowsLabel(): string {
    if (n === 0) return text.noData;
    if (searched < n) return searchLabel + " / " + nLabel + " " + text.rows;
    return nLabel + " " + text.rows;
  }

  return (
    <div className="flex  min-w-[200px] gap-1">
      <div className="flex items-center">{tableIcon}</div>
      <div
        key={`${totalLabel}_${deleted}`}
        className="flex flex-wrap items-center px-2  gap-x-2 animate-fadeIn text-title7 md:text-title6 font-label"
      >
        <div className={n > 0 ? "" : "hidden"}>
          {table.head.cells.length} {text.columns},
        </div>
        <div key={totalLabel} className="animate-fadeIn">
          {rowsLabel()}
          {deleted > 0 ? "," : ""}
        </div>

        <div className={`flex text-grey2 ${deleted > 0 ? "" : "hidden"}`}>
          {deletedLabel}
          <img
            src={UndoSvg}
            className="w-5 h-5 -translate-y-[2px] md:-translate-y-0 -translate-x-[3px] ml-2"
            onClick={handleUndo}
          />
        </div>
      </div>
    </div>
  );
};

const tableIcon = (
  <svg
    className="h-9"
    viewBox="4 4 18 18"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <rect x="9" y="9" width="4" height="2" fill="#4272EF" />
    <rect x="9" y="13" width="4" height="2" fill="#4272EF" />
    <rect x="9" y="17" width="4" height="2" fill="#4272EF" />
    <rect x="15" y="9" width="4" height="2" fill="#4272EF" />
    <rect x="15" y="13" width="4" height="2" fill="#4272EF" />
    <rect x="15" y="17" width="4" height="2" fill="#4272EF" />
    <rect x="4" y="4" width="15" height="3" fill="#4272EF" />
    <rect x="4" y="9" width="3" height="10" fill="#4272EF" />
  </svg>
);

function getTranslations(locale: string): Record<string, string> {
  const translated: Record<string, string> = {};
  for (const [key, value] of Object.entries(translations)) {
    translated[key] = Translator.translate(value, locale);
  }
  return translated;
}

const translations = {
  columns: new TextBundle()
    .add("en", "columns")
    .add("nl", "kolommen")
    .add("es", "columnas"),

  rows: new TextBundle()
    .add("en", "rows")
    .add("nl", "rijen")
    .add("es", "filas"),

  noData: new TextBundle()
    .add("en", "no data")
    .add("nl", "geen data")
    .add("es", "sin datos"),

  deleted: new TextBundle()
    .add("en", "deleted")
    .add("nl", "verwijderd")
    .add("es", "eliminado"),
};
