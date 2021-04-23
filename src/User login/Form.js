/* eslint-disable jsx-a11y/img-redundant-alt */
import React, { useState } from 'react';
import './Form.css';
import FormSignup from './FormSignup';
import FormSuccess from './FormSuccess';

const Form = () => {
  const [isSubmitted, setIsSubmitted] = useState(false);

  function submitForm() {
    setIsSubmitted(true);
  }
  return (
    <>
      <div className='form-container'>
        
        <div className='form-content-left'>
          <img className='form-img' src='img/bg2.jpg' alt='Login Page Image' />
        </div>
        <FormSignup submitForm={submitForm} />
        {/* {!isSubmitted ? (
          <FormSignup submitForm={submitForm} />
        ) : (
          <FormSuccess />
        )} */}
      </div>
    </>
  );
};

export default Form;