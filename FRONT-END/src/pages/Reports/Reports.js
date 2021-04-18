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
import { Button, Paper } from '@material-ui/core';
import "./AutoComplete.css";

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

const ProgLang = ["FF102155-010BB-1009", "FF102155-010BE-0859", "FF102155-010BK-0791"];

  const [searchtext, setSearchtext] = useState("");
  const [suggest, setSuggest] = useState([]);
  const [resfound, setResfound] = useState(true);
  const handleChange1 = (e) => {
    let searchval = e.target.value;
    let suggestion = [];
    if (searchval.length > 0) {
      suggestion = ProgLang
        .sort()
        .filter((e) => e.toLowerCase().includes(searchval.toLowerCase()));
      setResfound(suggestion.length !== 0 ? true : false);
    }
    setSuggest(suggestion);
    setSearchtext(searchval);
    

  };

  const suggestedText = (value) => {
    console.log(value);
    setSearchtext(value);
    setAddTodo2(value);
    console.log(value);
    setSuggest([]);
  };

  const getSuggestions = () => {
    if (suggest.length === 0 && searchtext !== "" && !resfound) {
      return <p>Search Content Not Found</p>;
    }

    return (
      <ul>
        {suggest.map((item, index) => {
          return (
            <div key={index}>
              <li onClick={() => suggestedText(item)}>{item}</li>
              {index !== suggest.length - 1 && <hr />}
            </div>
          );
        })}
      </ul>
    );
  };

  return (
<div className="reports">

      <h1 id = "reportHeadding">Reports</h1>

    <Paper className="paper">
     <form  noValidate autoComplete="off" onSubmit={handleFormSubmit}>
       <div className="input-fields-3">

        {/* quantity field */}
        <div className="quantity-tf">
        <TextField 
          required value={userInput} 
          onChange={handleFormChange}
          label="Quantity"
          id="standard-start-adornment"
          style = {{width: "60%"}}
          InputProps={{
            startAdornment: <InputAdornment position="start">Kg</InputAdornment>,
          }}
        />
        </div>
        
        {/* colour field */}
         <div className = "colour-tf">
           <TextField
               id="standard-select-currency"
               style = {{width: "60%"}}
               select
               label="Colour"
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

          {/* Elastic type field */}
          <div className="searchcontainer">
                <input id="suggestion "
                  type="text"
                  placeholder="Elastic type    *"
                  className="search"
                  value={searchtext}
                  onChange={handleChange1}
                />
                {getSuggestions()}
         </div>
       </div>

        {/* submit button */}
         <div className="submitbtn">
         <input type='submit' className="btn btn-primary"></input>
        </div>

      </form> 
      </Paper>

     <ul key={todo4.id}>
                       <li>
                           {todo4.response}
                        </li>
                   </ul>                
</div>
  );
}

export default Reports;