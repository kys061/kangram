import { combineReducers, createStore, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import users from "redux/module/users";

const middlewares = [thunk];

const reducer = combineReducers({
  users
});

let store = initialState =>
    createStore(reducer, applyMiddleware(...middlewares));

export default store();
