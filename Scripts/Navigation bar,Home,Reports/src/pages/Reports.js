import React from 'react';
import {createStyles,makeStyles,Theme} from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import MenuItem from '@material-ui/core/MenuItem';
import App from './App.jsx';
import './Reports.css';

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

function Reports() {

  const classes = useStyles();

  const [currency, setCurrency] = React.useState('EUR');

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setCurrency(event.target.value);
  };

  return (
<div className="reports">
      <h1 id = "reportHeadding">Reports</h1>

     <form className={classes.root} noValidate autoComplete="off">
       <div className="colourAndQuantity">
         <TextField id ="standard-basic" label="Quantity" />
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



       <App/>
     </form>
</div>
  );
}

export default Reports;