import React from 'react';
import {createStyles,makeStyles,Theme} from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import MenuItem from '@material-ui/core/MenuItem';
import './Reports.css';
import clsx from 'clsx';
import InputAdornment from '@material-ui/core/InputAdornment';
import AutoCompleteText from "./AutoCompleteText/AutoCompleteText";
import countries from "./AutoCompleteText/countries";
import {useState,useRef, useEffect} from 'react';

const useStyles = makeStyles((theme: Theme) =>
createStyles({
  root:{
    '& .MuiTextField-root' : {
      margin:theme.spacing(1),
      width: '25ch',
    },
  },
}),
);

const currencies = [
  {
    value: 'DYE_SG_BK',
    label: 'DYE_SG_BK',
  },
  {
    value: 'DYE_SG_DK',
    label: 'DYE_SG_DK',
  },
  {
    value: 'DYE_SG_FI',
    label: 'DYE_SG_FI',
  },
  {
    value: 'DYE_SG_LT',
    label: 'DYE_SG_LT',
  },
  {
    value: 'DYE_SG_MD',
    label: 'DYE_SG_MD',
  },
  {
    value: 'DYE_SG_WH',
    label: 'DYE_SG_WH',
  },
  {
    value: 'No Color',
    label: 'No Color',
  },
];


function Reports({userInput,userInput2}) {

  
  const[addTodo,setAddTodo]=useState('')

  const[addTodo1,setAddTodo1]=useState('')

  const[addTodo2,setAddTodo2]=useState('')

  const[todo4,setTodo4]=useState([])

  const classes = useStyles();

  const [currency, setCurrency] = React.useState('EUR');

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setCurrency(event.target.value)
    setAddTodo1(event.target.value)
    console.log(addTodo1)
  };
  const handleFormChange =(event) =>{
    setAddTodo(event.target.value)
    console.log(addTodo)
  }
  

  const handleFormSubmit =(event) =>{
    setAddTodo2(event.target.value)
    console.log(addTodo2)
    event.preventDefault()
    fetch('/sendData',{
        method:'POST',
        body:JSON.stringify({
           type: addTodo2,
           color: addTodo1,
           quantity:addTodo
           
           
           
        }),
        headers:{
            "Content-type":"application/json; charset=UTF-8"
        }
    }).then(response=>response.json())
      .then(data =>{
        console.log(data)
        setTodo4(data)
        
      })
}


  return (
<div className="reports">
      <h1 id = "reportHeadding">Reports</h1>

     <form className={classes.root} noValidate autoComplete="off" onSubmit={handleFormSubmit}>
       <div className="colourAndQuantity">

        
         <div className={classes.root}>

        <div>
        <TextField
          required value={userInput} 
          onChange={handleFormChange}
          label="With normal TextField"
          id="standard-start-adornment"
          className={clsx(classes.margin, classes.textField)}
          InputProps={{
            startAdornment: <InputAdornment position="start">Kg</InputAdornment>,
          }}
        />
        </div>
        </div>
        
         <div className = "TFDropdown">
           <TextField
               id="standard-select-currency"
               select
               label="Select"
               required value={currency}
               onChange={handleChange}
               helperText="Please select colour"
           >
             {currencies.map((option) => (
                 <MenuItem key={option.value} value={option.value}>
                   {option.label}
                 </MenuItem>
             ))}
           </TextField>
         </div>
       </div>

    <div className="type-search">
      <AutoCompleteText items={countries} />
    </div>
      
     </form>  
     <ul key={todo4.id}>
                       <li>
                           {todo4.response}
                        </li>
                   </ul>                
</div>
  );
}

export default Reports;