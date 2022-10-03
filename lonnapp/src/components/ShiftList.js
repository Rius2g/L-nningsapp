import React from 'react';
import todo from '../Todo';
import IconButton from '@mui/material/IconButton';
import Stack from '@mui/material/Stack';
import DeleteIcon from '@mui/icons-material/Delete';

const ShiftList = ({ShiftList, handleToggle, handleFilter, clearAll}) => {
    return (
        <div>
        <Stack direction="row" spacing={1} alignItems="center" justifyContent="center">
            <button style={{margin: '20px'}} onClick={handleFilter}>Clear Completed</button>
            <IconButton aria-label="delete all" color="secondary" onClick={clearAll} >
            <DeleteIcon fontSize="inherit"/>
            </IconButton>
            </Stack>
            {ShiftList.map(shift => {
                return (
                    <todo todo={todo} handleToggle={handleToggle}/>
                )
            })}
        </div>
    );
};

export default ShiftList;