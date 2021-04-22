import React from 'react';
import validate from './validateInfo';
import useForm from './useForm';
import './Form.css';

const FormSignup = ({ submitForm }) => {
  const { handleChange, handleSubmit, values, errors } = useForm(
    submitForm,
    validate
  );

  return (
    <div className='form-content-right'>
      <form action="" method="post" onSubmit={handleSubmit} className='form' noValidate>
        <h1 style={{textAlign: 'center'}}> WELCOME</h1>
        <h3 style={{textAlign: 'left'}}>
          Login to your account
        </h3>
        <div className='form-inputs'>
            <br/>
          
          <input
            className='form-input'
            type='text'
            name='username'
            placeholder='User Name'
            value={values.username}
            onChange={handleChange}
          />
           
           <br/>
          {errors.username && <p>{errors.username}</p>}
        </div>
       
        <div className='form-inputs'>
          
          <input
            className='form-input'
            type='password'
            name='password'
            placeholder='Password'  
            value={values.password} 
            onChange={handleChange}
          />
          
          {errors.password && <p>{errors.password}</p>}
        </div>
        

        <button className='form-input-btn' type='submit' onClick={(e) => {
          e.preventDefault();
          window.location.href='/home';
        }} >
          Login
        </button>

      </form>
    </div>
  );
};

export default FormSignup;