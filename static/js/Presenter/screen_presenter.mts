import type { FuncPort } from "../Presenter/interface.mjs";

let webViewRef: FuncPort | null = null;

export function setWebView(w: FuncPort) {
    webViewRef = w;
};
// bring data from controller through `DataPort` interface.
export const screenPresenter = {
    port(data: object) {
        console.log(data);
    }
};









// initialize the 'web view' update through the `FuncPort` interface.
export function portFunc() {
    if (!webViewRef) throw new Error("web view not provided")

    webViewRef.port();
};