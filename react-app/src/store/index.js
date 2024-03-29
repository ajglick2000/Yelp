import { createStore, combineReducers, applyMiddleware, compose } from "redux";
import thunk from "redux-thunk";
import session from "./session";
import listingsReducer from "./listing";
import reviewsReducer from "./review";
import messagesReducer from "./message";
import conversationsReducer from "./conversation";

const rootReducer = combineReducers({
    session,
    listings: listingsReducer,
    reviews: reviewsReducer,
    messages: messagesReducer,
    conversations: conversationsReducer,
});

let enhancer;

if (process.env.NODE_ENV === "production") {
    enhancer = applyMiddleware(thunk);
} else {
    const logger = require("redux-logger").default;
    const composeEnhancers =
        window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
    enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = (preloadedState) => {
    return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;
