import React, { useState } from 'react';
import SendIcon from '@mui/icons-material/Send';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import TimePick from './Timepicker';

const ToDoForm = ({ addTask }) => {

    const [ userInput, setUserInput ] = useState('');

    const handleChange = (e) => {
        setUserInput(e.currentTarget.value)
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        addTask(userInput);
        setUserInput("");
    }
    return (
        <div style={{
          margin: 'auto',
          display: 'block',
          width: 'fit-content'
        }} direction="row" 
        spacing={2} 
        alignItems="center" 
        justifyContent="center">
          <TextField
            id="date"
            label=""
            type="date"
            InputLabelProps={{
              shrink: true,
            }}
          />
          <TimePick></TimePick>
        </div>
      );
};

export default ToDoForm;