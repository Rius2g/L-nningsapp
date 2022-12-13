import { Button, Stack } from '@mui/material';
import React, { useState, useEffect } from 'react';
import UserDisplay from '../components/UserList';
import SendIcon from '@mui/icons-material/Send';
import TextField from '@mui/material/TextField';

function Settings() {

  const [ payRate, setPayRate ] = useState(0);
  const [ taxRate, setTaxRate ] = useState(0);

  useEffect(() =>  {
    fetch('http://127.0.0.1:5000/api/payrate/')
    .then(response => response.json())
    .then(data => setPayRate(data.payrate))


    fetch(fetch('http://127.0.0.1:5000/api/taxrate/')
    .then(response => response.json())
    .then(data => setTaxRate(data.taxrate)))
  }, []);



  const handlePayChange = (e) => {
    setPayRate(e.currentTarget.value) //constantly update the input
  };


  const handleSubmit = (event) => {
    fetch('http://127.0.0.1:5000/api/payrate/', {
       method: 'PUT', 
       headers: {
         'Content-Type': 'application/json'
       },
       body: JSON.stringify({
        payrate: payRate,
        taxrate: taxRate
       })
   });
  setPayRate(payRate);
  setTaxRate(taxRate);
  };

  const handleTaxChange = (e) => {
    setTaxRate(e.currentTarget.value) //constantly update the input
  };


  return (
    <div className="App">
      <h1>
        Settings page
      </h1>
      <h2>
        Pay Rate: {payRate}
        Tax rate: {taxRate}%
        </h2>
    <form onSubmit={handleSubmit}>
    <TextField
    id="pay-rate"
    label="Enter Pay Rate"
    value={payRate}
    onChange={handlePayChange}
    />
    <TextField
    id="tax-rate"
    label="Enter Tax Rate"
    value={taxRate}
    onChange={handleTaxChange}
    />
    <Button variant="contained" onClick={handleSubmit} endIcon={<SendIcon />} style={{ minHeight: '7.2vh' }}>
        Submit
    </Button>
</form>
</div> 
);
}

export default Settings;