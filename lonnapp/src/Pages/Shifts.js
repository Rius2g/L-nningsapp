import React from 'react';

function Shifts() {
  return (
    <div className='shifts'>
      <h1>Shifts</h1>
    </div>
  );
}


/*
json format
{
  Date: int date
  Start: int start hour
  End: int end hour
  Hours: int hours
  IsSaturday: bool
  IsSunday: bool
}
*/
export default Shifts;