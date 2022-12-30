import React, { useState, useEffect } from 'react';
import ShiftList from '../components/ShiftList';
import ShiftForm from '../components/ShiftForm';
import '../Shiftpage.css';

function App() {
  const [ shiftsList, setShiftList ] = useState([]);

  useEffect(() =>  {
    fetch('http://127.0.0.1:5000/api/items/')
    .then(response => response.json())
    .then(data => setShiftList(data.items));
  }, []);


  const addShift = (workDate, day, startTime, endTime) => {
  const newShiftList = shiftsList.concat({ id: shiftsList.length+1, date: workDate, workday: day, start: startTime, end: endTime })
  setShiftList(newShiftList);

    fetch('http://127.0.0.1:5000/api/items/', {
       method: 'POST', 
       headers: {
         'Content-Type': 'application/json'
       },
       body: JSON.stringify({
        id: shiftsList.length+1,
        date: workDate,
        workday: day,
        start: startTime,
        end: endTime
       })
   });
  };

  function handleDelete(DelShift) {
    const newList = shiftsList.filter((shift) => shift.id !== DelShift.id);

    setShiftList(newList);

    fetch('http://127.0.0.1:5000/api/items/' + DelShift.id, {
         method: 'DELETE', 
         headers: {
           'Content-Type': 'application/json'
         },
         body: JSON.stringify({
          id: DelShift.id
         })
     });
  }

  const ClearAll = () => { //delete all
    shiftsList.map(todo => {
        fetch('http://127.0.0.1:5000/api/items/', {
         method: 'DELETE', 
         headers: {
           'Content-Type': 'application/json'
         },
         body: null
     });
     return null;
      });
      setShiftList([]); //tacky but works so it deletes all without refreshing
  };


  
 return (
   <div className="App">
     <h1>
      Shifts page
      </h1>
      
      <ShiftForm addShift={addShift} direction="row" 
      spacing={100}
      margin={100} 
      alignItems="center" 
      justifyContent="center"/>
      <ShiftList ShiftList={shiftsList} handleDelete={handleDelete} clearAll={ClearAll} 
      direction="row" 
      spacing={2} 
      alignItems="center" 
      justifyContent="center"/>
   </div>
 );
}
 
export default App;