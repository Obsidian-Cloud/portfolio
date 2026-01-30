import type { DataPort } from "./interface.mjs";

let data: object = {"name": "Keith"};
let presenterRef: DataPort | null = null;

export function setPresenter(p: DataPort) {
    presenterRef = p;
};













// send data to the 'screen presenter' through the `DataPort` interface.
export function portData() {
    if (!presenterRef) throw new Error("controller not provided")

    presenterRef.port(data);
};
