import React from 'react';



const Shifts = ({Shift, removeshift}) => {

    return (
        <div id={Shift.id} key={Shift.id + Shift.date} name="Shift" value={Shift.id}>
            {Shift.date}
            {' '}
            {Shift.start}
            {'-'}
            {Shift.end}
        </div>
    );
};

export default Shifts;