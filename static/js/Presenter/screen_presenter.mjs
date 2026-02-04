// screen_presenter.mjs
import { setViewData } from "./screen_view_model.mjs";

var webViewRef = null;
export function setWebView(w) {
    webViewRef = w;
}
;
// bring data from controller through `DataPort` interface.
export var screenPresenter = {
    port: function (responseData) {
        console.log("Data passed to screen_presenter.mjs: ");
        // execute main presenter functionality
        executePresenter(responseData);
    }
};
// initialize the 'web view' update through the `FuncPort` interface.
export function portFunc() {
    if (!webViewRef)
        throw new Error("web view not provided");
    webViewRef.port();
}
;


function executePresenter(responseData) {
    const finalRemap = formatData(responseData);
    // calls 'setter' function in screen_view_model.mjs to update data structure
    setViewData(finalRemap);
    // calls 'interface' function on web_view.mjs to retrieve the data structure
    portFunc();
};


// format the incoming responseData
function formatData(responseData) {
    // if 'delete', otherwise insert or update
    if (responseData.action === 'delete') {
        // set blueprint
        const requestRemap = {'action': 'None', 'payload': {'ids': []}};
        const remappedPayload = {};
        // for each key in the `requestRemap` set the appropriate value
        // from the responseData
        Object.keys(requestRemap.payload).forEach(key => {
            remappedPayload[key] = responseData.payload[key];
        });

        const finalRemap = {
            action: responseData.action,
            payload: remappedPayload
        };

        return finalRemap
    }


    
    const requestRemap = {'action': 'None', 'payload': {'id': 'None', 'name': 'None', 'note': 'None', 'level': 'None', 'active': 'None', 'updated': 'None'}};
    // build localised date
    responseData.payload.updated = new Date(responseData.payload.updated).toLocaleString();
    // remap payload values to `requestRemap` structure
    const remappedPayload = {};

    Object.keys(requestRemap.payload).forEach(key => {
        remappedPayload[key] = responseData.payload[key] !== undefined ? responseData.payload[key] : 'None';
    });

    const finalRemap = {
        action: responseData.action,
        payload: remappedPayload
    };

    return finalRemap
}