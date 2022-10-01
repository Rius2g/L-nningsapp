import React, { useState } from 'react';
import SendIcon from '@mui/icons-material/Send';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';

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
        <form onSubmit={handleSubmit}>
            <TextField
        id="outlined-name"
        label="Enter Todo"
        value={userInput}
        onChange={handleChange}
      />
            <Button variant="contained" onClick={handleSubmit} endIcon={<SendIcon />} style={{ minHeight: '7vh' }}>
                Submit
            </Button>
        </form>
    );
};

export default ToDoForm;