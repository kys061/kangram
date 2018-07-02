import React, { Component } from "react";
import PropTypes from "prop-types"
import SignupForm from "./presenter";


class Container extends Component {
    state = {
        email: "",
        fullname: "",
        username: "",
        password: ""
    };

    static propTypes = {
        facebookLogin: PropTypes.func.isRequired,
        createAccount: PropTypes.func.isRequired
    };

    render() {
        const {email, fullname, username, password} = this.state;
        return <SignupForm
            emailValue={email}
            fullnameValue={fullname}
            usernameValue={username}
            passwordValue={password}
            handleInputChange={this._handleInputChange}
            handleSubmit={this._handleSubmit}
            handleFacebookLogin={this._handleFacebookLogin}
        />;

    }
    _handleInputChange = event => {
        const { target : {value, name}} = event;
        this.setState({
            [name]: value
        })
        // const { target: { value, name } } = event;
        // this.setState({
        //     [name]: value   // name means state.username or state.password
        // })
    };

    _handleSubmit = event => {
        const {email, fullname, username, password} = this.state;
        const { createAccount } = this.props;
        event.preventDefault();
        // will add action after submit
        createAccount(username, password, email, fullname);
    };

    _handleFacebookLogin = response => {
        //response is from real facebook
        const { facebookLogin } = this.props;
        facebookLogin(response.accessToken);
        // console.log(response);
    }
}

export default Container;
