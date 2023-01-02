import React from 'react';
import Rules from '../components/Rules';
import Stack from '@mui/material/Stack';
import IconButton from '@mui/material/IconButton';
import DeleteIcon from '@mui/icons-material/Delete';

const RuleList = ({RuleList, handleDelete, clearAll}) => {
    return (
        <div>
        <Stack direction="row" spacing={1} alignItems="center" justifyContent="center">
            <IconButton aria-label="delete all" color="secondary" onClick={clearAll} >
            <DeleteIcon fontSize="inherit"/>
            </IconButton>
            </Stack>
            {RuleList.map(Rule => {
                return (
                    <div>
                        <Rules Rule={Rule}/>
                        <IconButton aria-label="delete" size="small">
                        <DeleteIcon fontSize="inherit" onClick={handleDelete} />
                        </IconButton>
                    </div>
                )
            })}
            
        </div>
    );
};

export default RuleList;