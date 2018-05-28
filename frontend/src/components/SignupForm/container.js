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
        facebookLogin: PropTypes.func.isRequired
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
        const { target : {name, value}} = event;
        this.setState({
            [name]: value
        })
    };

    _handleSubmit = event => {
        event.preventDefault();
        // will add action after submit
    };

    _handleFacebookLogin = response => {
        //response is from real facebook
        const { facebookLogin } = this.props;
        facebookLogin(response.accessToken);
        // console.log(response);
    }
}

export default Container;
