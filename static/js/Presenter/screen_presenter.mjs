var webViewRef = null;
export function setWebView(w) {
    webViewRef = w;
}
;
// bring data from controller through `DataPort` interface.
export var screenPresenter = {
    port: function (responseData) {
        console.log("Data passed to screen_presenter.mjs: ");
        console.log(responseData);
    }
};
// initialize the 'web view' update through the `FuncPort` interface.
export function portFunc() {
    if (!webViewRef)
        throw new Error("web view not provided");
    webViewRef.port();
}
;
