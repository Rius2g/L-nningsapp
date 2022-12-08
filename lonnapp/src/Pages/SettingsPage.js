import React, { useState, useEffect } from 'react';
import User from '../components/User';

function Settings() {

  const [ payRate, setPayRate ] = useState();

  useEffect(() =>  {
    fetch('http://127.0.0.1:5000/api/items/')
    .then(response => response.json())
    .then(data => setPayRate(data));
  }, []);



  return (
    <div className='settings'>
      <h1>Settings</h1>
    </div>
  );
}

export default Settings;