import React from 'react';
import{Input}from 'reactstrap'

const  Inputi = ({atribute, handleChange, param}) => {
    return(
        <div className='input-container'>
            <Input
            id={atribute.id}
            name={atribute.name}
            placeholder={atribute.placeholder}
            type={atribute.type}
            onChange={(e) => handleChange(e.target.name, e.target.value)}
            className={param ? 'input-error' : 'regular-style'}
            />
        </div>
    )
};

export default Inputi;