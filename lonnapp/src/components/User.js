import React from 'react';

const User = ({User}) => {
    return (
        <div id={User.id + User.name} key={User.id} name="User" value={User.id}>
            {User.name}
            {' '}
            {User.payrate}
            {' '}
            {User.taxrate}
        </div>
    );
};

export default User;