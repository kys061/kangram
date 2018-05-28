// imports

// actions
const SAVE_TOKEN = "SAVE_TOKEN";

// action creators : function for action
function saveToken(token) {
  return {
    type: SAVE_TOKEN,
    token
  };
}

// API actions
function facebookLogin(access_token) {
  return function(dispatch) {
    fetch("/users/login/facebook/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        access_token
      })
    })
      .then(response => response.json())
      .then(json => {
        if (json.token) {
          localStorage.setItem("jwt", json.token);
          dispatch(saveToken(json.token));
        }
        console.log(json)
      })
      .catch(err => console.log(err));
  };
}

// initial state
const initialState = {
  isLoggedIn: false
};

// reducer

function reducer(state = initialState, action) {
  switch (action.type) {
    case SAVE_TOKEN:
      return applySetToken(state, action);
    default:
      return state;
  }
}

// reducer functions: functions that is started as real

function applySetToken(state, action) {
  const { token } = action;
  return {
    ...state,
    isLoggedIn: true,
    token: token
  };
}


// exports
const actionCreators = {
  facebookLogin
};

export { actionCreators };


// export reducer by default

export default reducer;
