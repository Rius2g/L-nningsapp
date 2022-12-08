import { Stack } from '@mui/material';
import { flexbox } from '@mui/system';
import React, { useState, useEffect } from 'react';
import UserDisplay from '../components/UserList';

function Settings() {

  const [ payRate, setPayRate ] = useState(10);
  const [ taxRate, setTaxRate ] = useState(5);

  // useEffect(() =>  {
  //   fetch('http://127.0.0.1:5000/api/items/')
  //   .then(response => response.json())
  //   .then(data => setPayRate(data));
  // }, []);



  return (
    <div className='settings'>
      <Stack>
      <h1 alignItems="center" direction="row" justifyContent="center">Settings</h1>

      <UserDisplay payrate={payRate} taxrate={taxRate} direction="row"
      spacing={10}
      margin={10} 
      alignItems="center" 
      justifyContent="center"/>

      </Stack>

    </div>
  );
}

export default Settings;