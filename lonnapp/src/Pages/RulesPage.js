import React from 'react';
import RulesForm from '../components/RulseForm';
import { Stack } from '@mui/material';

function Rules() {
  return (
    <Stack spacing={1} alignItems="center" justifyContent="center">
      <h1>Rules</h1>
      <Stack direction="row" spacing={1} alignItems="center" justifyContent="center">
      <RulesForm></RulesForm>
      </Stack>
    </Stack>
  );
}

export default Rules;