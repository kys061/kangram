import React from "react";
// import Ionicon from "react-ionicons";
import PropTypes from "prop-types";
import formStyles from "shared/formStyles.scss"
import FacebookLogin from "react-facebook-login";

export const LoginForm = (props, context) => (
  <div className={formStyles.formComponent}>
    <form className={formStyles.form} onSubmit={props.handleSubmit}>
      <input
          type="text"
          placeholder={context.t("Username")}
          className={formStyles.textInput}
          value={props.usernameValue}
          name="username"
          onChange={props.handleInputChange}
      />
      <input
        type="password"
        placeholder={context.t("Password")}
        className={formStyles.textInput}
        value={props.passwordValue}
        name="password"
        onChange={props.handleInputChange}
      />
      <input type="submit" value={context.t("Log In")} className={formStyles.button} />
    </form>
    <span className={formStyles.divider}>or</span>
    <FacebookLogin
        appId="584586631905809"
        autoLoad={false}
        fields="name,email,picture"
        cssClass={formStyles.facebookLink}
        icon="fa-facebook-official"
        callback={props.handleFacebookLogin}
    />
    <span className={formStyles.forgotLink}>Forgot password?</span>
  </div>
);

LoginForm.propTypes = {
    usernameValue: PropTypes.string.isRequired,
    passwordValue: PropTypes.string.isRequired,
    handleInputChange: PropTypes.func.isRequired,
    handleSubmit: PropTypes.func.isRequired,
    handleFacebookLogin: PropTypes.func.isRequired
};

LoginForm.contextTypes = {
 t: PropTypes.func.isRequired
};

export default LoginForm;
