import React, { useState } from 'react';
import Select from "react-dropdown-select";



const RulesForm = ({ addRule }) => {

    const [ ruleType, setRuleType ] = useState(''); //contains type (day)
    const [ increaseT, setIncreaseT ] = useState(''); //contains type (day)
    const [ ruleValue, setRuleValue ] = useState(''); //contains value (kr increase)
    const [ ruleList, setRuleList ] = useState([]); //contains all rules
    const [ rule = {type: ruleType, value: ruleValue}, setRule ] = useState(''); //rule contains type and value

    const Days = [
        { label: "Monday", value: 1 },
        { label: "Tuesday", value: 2 },
        { label: "Wednsday", value: 3 },
        { label: "Thursday", value: 4 },
        { label: "Friday", value: 5 },
        { label: "Saturday", value: 6 },
        { label: "Sunday", value: 7 }
      ];

    const Values = [
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
        { label: "%", value: 1 },
        { label: "kr", value: 2 }
    ]

    const type = [
        { label: "Day", value: 1 },
        { label: "Time", value: 2 }
    ]

    const setType = type => {
        setRuleType(type);
    }



    function handleSubmit() {
        addRule(rule.toString());
    }


    return (
      
        <div className='rowline' style={{
          margin: 'auto',
          width: 'fit-content',
          display: 'flex',
        }}>
        <Select options={type}onChange={setType} value={ruleType}> </Select> 
        <Select options={Days} onChange={setRuleValue} value={ruleValue}> </Select>
        <Select options={Times} onChange={setRuleValue} value={ruleValue}> </Select>
        <Select options={increaseType} onChange={setIncreaseT} value={increaseT}> </Select>
        <Select> </Select>
        </div>
      );
};

export default RulesForm;