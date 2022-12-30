import React from 'react';
import Shifts from '../components/Shift';
import Stack from '@mui/material/Stack';
import IconButton from '@mui/material/IconButton';
import DeleteIcon from '@mui/icons-material/Delete';

const ShiftList = ({ShiftList, handleDelete, clearAll}) => {
    return (
        <div>
        <Stack direction="row" spacing={1} alignItems="center" justifyContent="center">
            <IconButton aria-label="delete all" color="secondary" onClick={clearAll} >
            <DeleteIcon fontSize="inherit"/>
            </IconButton>
            </Stack>
            {ShiftList.map(shift => {
                return (
                    <div>
                        <Shifts Shift={shift}/>
                        <IconButton aria-label="delete" size="small">
                        <DeleteIcon fontSize="inherit" onClick={handleDelete} />
                        </IconButton>
                    </div>
                )
            })}
            
        </div>
    );
};

export default ShiftList;