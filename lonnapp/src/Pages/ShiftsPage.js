import React, { useState, useEffect } from 'react';
import ToDoList from '../TodoList';
import TodoForm from '../Form';
import '../Shiftpage.css';

function App() {
  const [ toDoList, setToDoList ] = useState([]);

  useEffect(() =>  {
    fetch('http://127.0.0.1:5000/api/items/')
    .then(response => response.json())
    .then(data => setToDoList(data.items));
  }, []);

  const handleToggle = (id) => {
    let mapped = toDoList.map(task => {
      return task.id === Number(id) ? { ...task, done: !task.done } : { ...task};
    });
    setToDoList(mapped);
  }

  const handleFilter = () => { //delete certain
    let filtered = toDoList.filter(task => {
      return !task.done;
    });
    let difference = toDoList.filter(x => !filtered.includes(x));
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
    setToDoList(filtered);
  }

  const addTask = (userInput) => { //POST
    fetch('http://127.0.0.1:5000/api/items/', {
       method: 'POST', 
       headers: {
         'Content-Type': 'application/json'
       },
       body: JSON.stringify({
        name: userInput,
        done: false,
        Id: toDoList.length+1
       })
   });
   fetch('http://127.0.0.1:5000/api/items') //get updated list so it displays without refreshing
    .then(response => response.json())
    .then(data => setToDoList(data.items));
  };

  const ClearAll = () => { //delete all
    toDoList.map(todo => {
        fetch('http://127.0.0.1:5000/api/items/' + todo.id, {
         method: 'DELETE', 
         headers: {
           'Content-Type': 'application/json'
         },
         body: null
     });
     return null;
      });
      setToDoList([]); //tacky but works so it deletes all without refreshing
  };
  
 return (
   <div className="App">
     <h1>
      Shifts page
      </h1>
      {/* <TodoForm addTask={addTask} direction="row" 
      spacing={2} 
      alignItems="center" 
      justifyContent="center"/> */}
      <ToDoList toDoList={toDoList} handleToggle={handleToggle} handleFilter={handleFilter} clearAll={ClearAll} 
      direction="row" 
      spacing={2} 
      alignItems="center" 
      justifyContent="center"/>
   </div>
 );
}
 
export default App;