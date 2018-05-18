import React from "react";
// import Ionicon from "react-ionicons";
import PropTypes from "prop-types";
import formStyles from "shared/formStyles.scss"
import FacebookLogin from "react-facebook-login";

export const SignupForm = (props, context) => (
  <div className={formStyles.formComponent}>
    <h3 className={formStyles.signupHeader}>
      Sign up to see photos and videos from your friends.
    </h3>
    <FacebookLogin
        appId="584586631905809"
        autoLoad={false}
        fields="name,email,picture"
        cssClass={formStyles.facebookLink}
        icon="fa-facebook-official"
        callback={props.handleFacebookLogin}
    />
    <span className={formStyles.divider}>or</span>
    <form className={formStyles.form}>
      <input type="email"
             placeholder={context.t("Email")}
             className={formStyles.textInput} />
      <input type="text"
             placeholder="Full Name"
             className={formStyles.textInput} />
      <input
        type="username"
        placeholder={context.t("Username")}
        className={formStyles.textInput}
      />
      <input
        type="password"
        placeholder={context.t("Password")}
        className={formStyles.textInput}
      />
      <input type="submit"
             value="Sign up"
             className={formStyles.button} />
    </form>
    <p className={formStyles.terms}>
      By signing up, you agree to our <span>Terms & Privacy Policy</span>.
    </p>
  </div>
);

SignupForm.propTypes = {
    emailValue: PropTypes.string.isRequired,
    fullnameValue: PropTypes.string.isRequired,
    usernameValue: PropTypes.string.isRequired,
    passwordValue: PropTypes.string.isRequired,
    handleInputChange: PropTypes.func.isRequired,
    handleSubmit: PropTypes.func.isRequired,
    handleFacebookLogin: PropTypes.func.isRequired
};

SignupForm.contextTypes= {
 t: PropTypes.func.isRequired
};

export default SignupForm;
