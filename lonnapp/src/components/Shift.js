import React from 'react';

const Shifts = ({todo, handleToggle}) => {
    const handleClick = (e) => {
        e.preventDefault()
        handleToggle(e.currentTarget.id)
    }

    return (
        <div id={todo.id} key={todo.id + todo.name} name="todo" value={todo.id} onClick={handleClick} className={todo.done ? "todo strike" : "todo"}>
            {todo.name}
        </div>
    );
};

export default Shifts;