import React from 'react';
import validate from './validateInfo';
import useForm from './useForm';
import './Form.css';
import {useState,useRef, useEffect} from 'react';

const FormSignup = ({ submitForm }) => {
  const { handleChange, handleSubmit, values, errors } = useForm(
    submitForm,
    validate
  );

  const[todo4,setTodo4]=useState([])

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
            //  value=""
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
        //  value=""
            onChange={handleChange}
          />
          
          {errors.password && <p>{errors.password}</p>}
        </div>
        

        <button className='form-input-btn' type='submit' onClick={(e) => {
           fetch('/login',{
               method:'POST',
               body:JSON.stringify({
                  username:values.username ,
                  password: values.password
                  
               }),
               headers:{
                   "Content-type":"application/json; charset=UTF-8"
               }
           }).then(response=>response.json())
             .then(data =>{
               console.log(data)
              if(data.response=="successfull"){
                e.preventDefault();
                window.location.href='/home';
    
              }
              setTodo4(data) 
             })
          
          
        }} >
          Login
        </button>

      </form>
        <div className="incorrect-info">
      <p><b>{todo4.response}</b></p>
        </div>
    </div>
  );
};

export default FormSignup;