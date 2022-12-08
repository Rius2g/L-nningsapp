import React from 'react';
import Stack from '@mui/material/Stack';

const UserDisplay = ({ payrate, taxrate  }) => {
    return (
        <div>
        <Stack direction="row" spacing={1} alignItems="center" justifyContent="center">
                    <h1 className='payrate'>Payrate: {payrate}</h1>
                    <h1 className='taxrate'>Taxrate: {taxrate}</h1>
            </Stack>
                
        </div>
    );
};

export default UserDisplay;