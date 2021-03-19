import React from 'react';
import {createStyles,makeStyles,Theme} from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import MenuItem from '@material-ui/core/MenuItem';
// import App from './App.jsx';
import './Reports.css';
import clsx from 'clsx';
import InputAdornment from '@material-ui/core/InputAdornment';
import {useState,useRef, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../App.css';



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
    value: 'USD',
    label: 'Red',
  },
  {
    value: 'EUR',
    label: 'Yellow',
  },
  {
    value: 'BTC',
    label: 'Green',
  },
  {
    value: 'JPY',
    label: 'Blue',
  },
];

const SearchbarDropdown = (props) => {
  const {options,onInputChange} = props;
  const ulRef = useRef()
  const inputRef = useRef()
  useEffect(() => {
      inputRef.current.addEventListener('click',(event) => {
          event.stopPropagation();
          console.log('input clicked');
          ulRef.current.style.display = 'flex';
          onInputChange(event);
      });
      document.addEventListener('click',(event) => {
          console.log('document clicked');
          ulRef.current.style.display = 'none';
      });
  }, []);
  return (
  <div className="search-bar-dropdown">
      <input id='search-bar' type="text" className="form-control"
             placeholder="Search" ref={inputRef} onChange={onInputChange}/>
      <ul id='results' className="list-group" ref={ulRef}>
          {options.map((option, index )=> {
              return(
                  <button type="button" key ={index} onClick={(e => {
                      inputRef.current.value = option;
                  })}
                          className="list-group-item list-group-item-action">
                      {option}
                  </button>
              );
          })}
      </ul>
  </div>
  )
};

const defaultOptions = [];
// for(let i = 0; i < 10;i++){
  defaultOptions.push(`option`);
  defaultOptions.push(`suggestion`);
  defaultOptions.push(`advice`);
// }

function Reports() {

  const classes = useStyles();

  const [currency, setCurrency] = React.useState('EUR');

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setCurrency(event.target.value);
  };

  const [options,setOptions] = useState([]);
    const onInputChange = (event) => {
        setOptions(
            defaultOptions.filter((option )=> option.includes(event.target.value))
        );
    };


  return (
<div className="reports">
      <h1 id = "reportHeadding">Reports</h1>

     <form className={classes.root} noValidate autoComplete="off">
       <div className="colourAndQuantity">
         <div className={classes.root}>
        <div>
        <TextField
          label="Quantity"
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
               value={currency}
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



       <div className="App container mt-2 mb-3">
            {/*<h1>Search Bar Dropdown</h1>*/}
            <SearchbarDropdown options={options} onInputChange={onInputChange}/>
            <div className="btnSearch">
                <button className="btn btn-primary">Search</button>
            </div>
        </div>
     </form> 

                 
</div>
  );
}

export default Reports;