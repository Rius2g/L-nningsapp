import React from 'react';
import Shifts from '../components/Shift';
import IconButton from '@mui/material/IconButton';
import Stack from '@mui/material/Stack';
import DeleteIcon from '@mui/icons-material/Delete';

const ShiftList = ({ShiftList, handleFilter, clearAll}) => {
    return (
        <div>
        <Stack direction="row" spacing={1} alignItems="center" justifyContent="center">
            <IconButton aria-label="delete all" color="secondary" onClick={clearAll} >
            <DeleteIcon fontSize="inherit"/>
            </IconButton>
            </Stack>
            {ShiftList.map(shift => {
                return (
                    <Shifts Shift={shift}/>
                )
            })}
        </div>
    );
};

export default ShiftList;