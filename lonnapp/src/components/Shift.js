import React from 'react';

const Shifts = ({Shift, handleToggle}) => {
    return (
        <div date={Shift.id} key={Shift.id + Shift.name} name="Shift" value={Shift.id}>
            {Shift.name}
        </div>
    );
};

export default Shifts;