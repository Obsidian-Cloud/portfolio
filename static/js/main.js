import { screenPresenterPort } from "./View/web_view.js";
import { controllerPort, screenPresenter } from "./Presenter/screen_presenter.js";
import { controller } from "./Controller/controller.js";


controller(controllerPort);
const presenter = screenPresenter(screenPresenterPort);
presenter.runLogic();