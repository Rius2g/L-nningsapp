import React from 'react';

const Shifts = ({Shift}) => {
    return (
        <div date={Shift.id} key={Shift.id + Shift.date} name="Shift" value={Shift.id} 
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