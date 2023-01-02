import React from 'react';



const Rules = ({Rule }) => {

    return (
        <div id={Rule.id} key={Rule.id} name="Rule" value={Rule.id}>
            {Rule.date}
            {' '}
            {Rule.start}
            {'-'}
            {Rule.end}
        </div>
    );
};

export default Rules;