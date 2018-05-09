import { connect } from 'react-redux';
import Container from './container';
const MapStateToProps = (state, ownProps) => {

    const { user } = state;
    return {
        isLoggedIn: user.isLoggedIn
    };
};

export default connect(MapStateToProps)(Container);
