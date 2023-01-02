import React, { useState } from 'react';
import Select from "react-dropdown-select";
import Button from '@mui/material/Button';
import { Stack } from '@mui/system';



const RulesForm = ({ addRule }) => {

    const [ ruleType, setRuleType ] = useState(0); //contains type day or time
    const [ ruleTypeVal, setRuleTypeVal ] = useState(0); //contains THE day or time value
    const [ increaseT, setIncreaseT ] = useState(0); //contains type (kr increase) or %
    const [ ruleValue, setRuleValue ] = useState(0); //contains value (kr increase)

    const Days = [
        { label: "Monday", value: 1 },
        { label: "Tuesday", value: 2 },
        { label: "Wednsday", value: 3 },
        { label: "Thursday", value: 4 },
        { label: "Friday", value: 5 },
        { label: "Saturday", value: 6 },
        { label: "Sunday", value: 7 }
      ];

    const percentage = [
        { label: "10%", value: 10 },
        { label: "20%", value: 20 },
        { label: "30%", value: 30 },
        { label: "40%", value: 40 },
        { label: "50%", value: 50 },
        { label: "60%", value: 60 },
        { label: "70%", value: 70 },
        { label: "80%", value: 80 },
        { label: "90%", value: 90 },
        { label: "100%", value: 100 }
    ];

    const Times = [
        { label: "00:00", value: 0 },
        { label: "01:00", value: 1 },
        { label: "02:00", value: 2 },
        { label: "03:00", value: 3 },
        { label: "04:00", value: 4 },
        { label: "05:00", value: 5 },
        { label: "06:00", value: 6 },
        { label: "07:00", value: 7 },
        { label: "08:00", value: 8 },
        { label: "09:00", value: 9 },
        { label: "10:00", value: 10 },
        { label: "11:00", value: 11 },
        { label: "12:00", value: 12 },
        { label: "13:00", value: 13 },
        { label: "14:00", value: 14 },
        { label: "15:00", value: 15 },
        { label: "16:00", value: 16 },
        { label: "17:00", value: 17 },
        { label: "18:00", value: 18 },
        { label: "19:00", value: 19 },
        { label: "20:00", value: 20 },
        { label: "21:00", value: 21 },
        { label: "22:00", value: 22 },
        { label: "23:00", value: 23 }
    ];

    const increaseType = [
        { label: "%", value: 0 },
        { label: "kr", value: 1 }
    ]

    const type = [
        { label: "Day", value: 0 },
        { label: "Time", value: 1 },
        {label: "Time and day", value: 2}
    ]
    

    function handleType(e){
        setRuleType(ruleType => e[0].value);
    }

    function handleIncreaseType(e){
        setIncreaseT(increaseT => e[0].value);
    }

    function handleValueType(e){
        setRuleTypeVal(ruleTypeVal => e[0].value);
    }

    function handleValue(e){
        setRuleValue(e.currentTarget.value);
    }

    function handlePercentage(e){
        setRuleValue(ruleValue => e[0].value)
    }

    function handleSubmit() {
        addRule(ruleType, ruleTypeVal, increaseT, ruleValue);
    }

    return (
      
        <div className='rowline' style={{
          margin: 'auto',
          width: 'fit-content',
          display: 'flex',
        }}>
        <Select options={type} onChange={handleType} value={ruleType}> </Select>

        {(() => {

        if (ruleType === 0) {
        return (

            <Select options={Days} onChange={handleValueType} value={ruleTypeVal}> </Select>
        )
        } else if (ruleType === 1) {
        return (

            <Select options={Times} onChange={handleValueType} value={ruleTypeVal}> </Select>
        )
        } else {
        return (
            <Stack direction="rowline">

            <Select options={Days} onChange={handleValueType} value={ruleTypeVal}> </Select>
            <Select options={Times} onChange={handleValueType} value={ruleTypeVal}> </Select>

            </Stack>
        )
        }

    })()}

        <Select options={increaseType} onChange={handleIncreaseType} value={increaseT}> </Select>

        {increaseT ?  <input type="number" onChange={handleValue} value={ruleValue}></input> : <Select options={percentage} onChange={handlePercentage} value={ruleValue}> </Select>}
        <Button variant="contained" onClick={handleSubmit}>Add Rule</Button>
        </div>
      );
};

export default RulesForm;