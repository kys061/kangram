import React, { Component } from "react";
import PropTypes from "prop-types"
import LoginForm from "./presenter";


class Container extends Component {
    state = {
        username: '',
        password: ''
    };

    static propTypes = {
        facebookLogin: PropTypes.func.isRequired,
        usernameLogin: PropTypes.func.isRequired
    };

    render() {
        const { username, password } = this.state;
        return <LoginForm
            usernameValue={username}
            passwordValue={password}
            handleInputChange={this._handleInputChange}
            handleSubmit={this._handleSubmit}
            handleFacebookLogin={this._handleFacebookLogin}
        />;
    }

    _handleInputChange = event => {
        const { target: { value, name } } = event;
        this.setState({
            [name]: value   // name means state.username or state.password
        })
    };

    _handleSubmit = event => {
        const { usernameLogin } = this.props;
        const { username, password } = this.state;
        event.preventDefault();
        // will add redux action after submit
        usernameLogin(username, password)
    };

    _handleFacebookLogin = response => {
        //response is from real facebook
        const { facebookLogin } = this.props;
        facebookLogin(response.accessToken);
        // console.log(response);
    }

}

export default Container;
