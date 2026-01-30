import { webView } from "./View/web_view.mjs";
import { setPresenter } from "./Controller/controller.mjs";
import { screenPresenter, setWebView } from "./Presenter/screen_presenter.mjs";

setWebView(webView);
setPresenter(screenPresenter);
