import React, { useState, useEffect } from 'react';
import { Button, Stack } from '@mui/material';
import DatePicker from 'react-date-picker'
import SendIcon from '@mui/icons-material/Send';
import { format } from 'date-fns'

function Home() {

  const [ expectedPay, setExpectedPay] = useState(0);
  const [ startRange, setStartRange ] = useState(new Date());
  const [ endRange, setEndRange ] = useState(new Date());


  useEffect(() =>  {
    fetch('http://127.0.0.1:5000/api/expectedpay/')
    .then(response => response.json())
    .then(data => setExpectedPay(data.expectedpay))

  }, []);


  const handleSet = (event) => {
    fetch('http://127.0.0.1:5000/api/expectedpay/', {
       method: 'PUT', 
       headers: {
         'Content-Type': 'application/json'
       },
       body: JSON.stringify({
        startRange: startRange,
        endRange: endRange
       })
   });
  setStartRange(startRange);
  setEndRange(endRange);

  fetch('http://127.0.0.1:5000/api/expectedpay/')
    .then(response => response.json())
    .then(data => setExpectedPay(data.expectedpay))
  };


  return (
    <div className='rowline' style={{
      margin: 'auto',
      width: '50%',
      display: 'flex',
    }}>
      <Stack spacing={2}>
      <h1>Home </h1>

      <p> Selected range is </p>
      <p>{startRange.toDateString()} - {endRange.toDateString()}</p>
      <Stack spacing={2} direction="row">
      <DatePicker id="datepicker"
                           viewMode="days"
                           timeFormat={false}
                            dateFormat="DD-MM-YY"
                            value={startRange}
                           onChange={setStartRange} />

      <DatePicker id="datepicker"
                           viewMode="days"
                           timeFormat={false}
                            dateFormat="DD-MM-YY"
                            value={endRange}
                           onChange={setEndRange}/>

      <Button variant="contained" onClick={handleSet} endIcon={<SendIcon/>} style={{ minHeight: '7.2vh' }} >
        Set Range
      </Button>
      </Stack>              
      <h2>Expected Pay: {expectedPay}</h2>
      </Stack>
    </div>
  );
}

export default Home;