import React from 'react';

const Shifts = ({Shift}) => {
    return (
        <div id={Shift.id} key={Shift.id + Shift.date} name="Shift" value={Shift.id} 
        direction="row" spacing={3} alignItems="center" justifyContent="center">
            {Shift.date}
            {' '}
            {Shift.start}
            {'-'}
            {Shift.end}
        </div>
    );
};

export default Shifts;