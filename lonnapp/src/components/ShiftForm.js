import React, { useState } from 'react';
import DatePicker from 'react-date-picker'
import TimePicker from 'react-time-picker'
import '../Shiftpage.css'
import SendIcon from '@mui/icons-material/Send';
import Button from '@mui/material/Button';


const ShiftForm = ({ addShift }) => {

    const [ workDate, setWorkDate ] = useState(new Date());
    const [ startTime, setStarttime ] = useState('10:00');
    const [ endTime, setEndtime ] = useState("10:00");

    const onChangeStart = time => {
        setStarttime(time);
    }

    const onChangeEnd = time => {
        setEndtime(time);
    }

    function handleSubmit() {
        addShift(workDate.toDateString(), startTime.toString(), endTime.toString());
    }

    return (
      
        <div className='rowline' style={{
          margin: 'auto',
          width: 'fit-content',
          display: 'flex',
        }}>

          <DatePicker id="datepicker"
                           viewMode="days"
                           timeFormat={false}
                            dateFormat="DD-MM-YY"
                            value={workDate}
                           onChange={setWorkDate} />

          <TimePicker id="timerange start" onChange={onChangeStart} value={startTime} />

            <TimePicker id="timerange end"
                            value={[endTime]}
                            onChange={onChangeEnd}
                            />


        <Button variant="contained" onClick={handleSubmit} endIcon={<SendIcon />} style={{ minHeight: '7vh' }}>
                Submit
            </Button>
        </div>
      );
};

export default ShiftForm;