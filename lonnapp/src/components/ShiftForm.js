import React, { useState } from 'react';
import DatePicker from 'react-date-picker'
import TimeRangePicker from '@wojtekmaj/react-timerange-picker'
import '../Shiftpage.css'
import SendIcon from '@mui/icons-material/Send';
import Button from '@mui/material/Button';
import Moment from 'moment';

const ShiftForm = ({ addShift }) => {

    const [ workDate, setWorkDate ] = useState(new Date());

    function handleSubmit(date) {
        setWorkDate(date);
        addShift(date, "10", "10");
    }

    return (
        <div className='rowline' style={{
          margin: 'auto',
          width: 'fit-content',
          display: 'flex'
        }}>
          <DatePicker id="datepicker"
                           viewMode="days"
                           timeFormat={false}
                            dateFormat="DD-MM-YY"
                            value={workDate}
                           onChange={setWorkDate} />
            <Button variant="contained" onClick={handleSubmit} endIcon={<SendIcon />} style={{ minHeight: '7vh' }}>
                Submit
            </Button>
          {/* <TimeRangePicker /> */}
        </div>
      );
};

export default ShiftForm;