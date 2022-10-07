import React, { useState, useEffect } from 'react';
import ShiftList from '../components/ShiftList';
import ShiftForm from '../components/ShiftForm';
import '../Shiftpage.css';
import data from '../Shiftdata.json'

function App() {
  const [ shiftsList, setShiftList ] = useState(data);

  /*useEffect(() =>  {
    fetch('http://127.0.0.1:5000/api/items/')
    .then(response => response.json())
    .then(data => setShiftList(data.items));
  }, []); */

  const handleToggle = (id) => {
    let mapped = shiftsList.map(task => {
      return task.id === Number(id) ? { ...task, done: !task.done } : { ...task};
    });
    setShiftList(mapped);
  }

  const handleFilter = () => { //delete certain
    let filtered = shiftsList.filter(task => {
      return !task.done;
    });
    let difference = shiftsList.filter(x => !filtered.includes(x));
    difference.map(task => {
      fetch('http://127.0.0.1:5000/api/items/' + task.id, {
       method: 'DELETE', 
       headers: {
         'Content-Type': 'application/json'
       },
       body: null
   });
   return null;
    })
    setShiftList(filtered);
  }

  const addShift = (workDate, startTime, EndTime) => { //POST
    const newShiftList = [...shiftsList, {"id": shiftsList.length+1, "date": workDate, "start": startTime, "end": EndTime}];
    setShiftList(newShiftList)
  };

  const ClearAll = () => { //delete all
    shiftsList.map(todo => {
        fetch('http://127.0.0.1:5000/api/items/' + todo.id, {
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
      spacing={2} 
      alignItems="center" 
      justifyContent="center"/>
      <ShiftList ShiftList={shiftsList} handleToggle={handleToggle} handleFilter={handleFilter} clearAll={ClearAll} 
      direction="row" 
      spacing={2} 
      alignItems="center" 
      justifyContent="center"/>
   </div>
 );
}
 
export default App;