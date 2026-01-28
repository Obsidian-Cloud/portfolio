// screen_presenter.js
import { viewData } from "./screen_view_model.js";

//
function appendObject(data) {
    Object.keys(data).forEach(key => {
        viewData.key = data.key;
    });
};







/**
 * @interface
 * Receives `userInput` from `controller.js` through port.
 */
export const controllerPort = {
    /**
     * @abstract
     * 
     */
    portData: function(data) {
        console.log("Screen presenter has the data.");
        appendObject(data)
        screenPresenter()
    }
};


let response = "False"
/**
 * @interface
 * Initiates execution of `updateView()` in `web_view.js` through port.
 */
// port function to web_view.js
export function screenPresenter(port) {
    /**
     * @abstract
     * @returns {object} - Abstract function.
     */
    if (response == "True") {
        // do something if response == true
    
    } else {
            return {
        runLogic: function () {
            port.updateView();
        }
    }};
};