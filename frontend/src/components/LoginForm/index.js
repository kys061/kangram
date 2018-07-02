import { connect } from "react-redux";
import Container from "./container";
import { actionCreators as userActions } from "redux/module/user";

// Add all the actions for:
// Log in
// Sign up
// Recover Password
// Check username
// Check password

const mapDispatchToProps = (dispatch, ownProps) => {
  return {
    facebookLogin: access_token => {
      dispatch(userActions.facebookLogin(access_token));
    },
    usernameLogin: (email, password) => {
      dispatch(userActions.usernameLogin(email, password));
    }
  };
};


export default connect(null, mapDispatchToProps)(Container);
