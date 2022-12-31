import React, { useState, useEffect } from 'react';
import RulesForm from '../components/RulseForm';
import { Stack } from '@mui/material';

function Rules() {

  const [ rulesList, setRulesList] = useState([]);

  useEffect(() =>  {
    fetch('http://127.0.0.1:5000/api/rules/')
  }, []);

  const addRule =  ( ruleType, ruleTypeVal, increaseT, ruleValue)  => {
    const newRulesList = rulesList.concat({ id: rulesList.length+1, type: ruleType, increasetype: increaseT, value: ruleValue})
    setRulesList(newRulesList);


    
    
        fetch('http://127.0.0.1:5000/api/rules/', {
           method: 'POST', 
           headers: {
             'Content-Type': 'application/json'
           },
           body: JSON.stringify({
            id: rulesList.length+1,
            type: ruleType,
            typeVal: ruleTypeVal,
            increaseType: increaseT,
            value: ruleValue
           })
       });
      };

    


  return (
    <Stack spacing={1} alignItems="center" justifyContent="center">
      <h1>Rules</h1>
      <Stack direction="row" spacing={1} alignItems="center" justifyContent="center">
      <RulesForm addRule={addRule}></RulesForm>
      </Stack>
    </Stack>
  );
}

export default Rules;