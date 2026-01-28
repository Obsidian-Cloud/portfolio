import { viewData } from "../Presenter/screen_view_model.js"

// screen_presenter.js port
export const screenPresenterPort = {
    updateView: function() {
        console.log("The view is updating...");
    }
};
