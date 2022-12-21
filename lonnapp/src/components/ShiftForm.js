import React, { useState } from 'react';
import DatePicker from 'react-date-picker'
import TimePicker from 'react-time-picker'
import '../Shiftpage.css'
import SendIcon from '@mui/icons-material/Send';
import Button from '@mui/material/Button';
import moment from 'moment';
import { format } from 'date-fns'


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

    function format_Date(date){
        return moment(date).format("DD/MM/YYYY");
     }

    function handleSubmit() {
       var date = format_Date(workDate)
        addShift(date.toString(), startTime.toString(), endTime.toString());
    }

    return (
      
        <div className='rowline' style={{
          margin: 'auto',
          width: 'fit-content',
          display: 'flex',
        }}>

{/* "MM/yyyy" */}
          <DatePicker id="datepicker"
                          viewMode="days"
                          timeFormat={false}
                          dateFormat="DD/MM/YYYY"
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