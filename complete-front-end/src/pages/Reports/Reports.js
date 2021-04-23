import React from 'react';
import TextField from '@material-ui/core/TextField';
import MenuItem from '@material-ui/core/MenuItem';
import './Reports.css';
import InputAdornment from '@material-ui/core/InputAdornment';
import {useState,useRef, useEffect} from 'react';
import { Button, Paper } from '@material-ui/core';
import Grid from '@material-ui/core/Grid';
import { makeStyles, createStyles, Theme } from '@material-ui/core/styles';
import Navbar from "../../Side bar/Navbar";
import 'bootstrap/dist/css/bootstrap.min.css';
import { Spinner } from 'react-bootstrap';


//loading page styles

const useStyles = makeStyles((theme: Theme) =>
    createStyles({
        root: {
            flexGrow: 1,
        },
        paper: {
            padding: theme.spacing(2),
            textAlign: 'center',
            color: theme.palette.text.secondary,
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

const initialFValues = {
    quantity: ''
}


function Reports({userInput,userInput2}) {



    const classes = useStyles(); // loading page styles
  
  const[addTodo,setAddTodo]=useState('')

  const[addTodo1,setAddTodo1]=useState('')

  const[addTodo2,setAddTodo2]=useState('')

  const[todo4,setTodo4]=useState([])

  const[todo5,setTodo5]=useState("1")

  

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
  const handleFormSubmit1 =(event) =>{
    window.location.reload(false)
  }

  const handleFormSubmit =(event) =>{
    setAddTodo2(event.target.value)
    console.log(addTodo2)
    event.preventDefault()
    setTodo5("3")
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
        setTodo5("2")
        
      })
}

const ProgLang = ["FJ101980-032.0", "FJ103791-032.0", "FJ103880-032.0WH","FK048204-008.5","FK048204-008.5BK-1142",
"FK048204-008.5BL-0857","FK048204-008.5BM-1441","FK048204-008.5BP-1373","FK048204-008.5CC-1385","FK048204-008.5CD-1340",
"FK048204-008.5FP-0820","FK048204-008.5LM-0923","FK048204-008.5MP-1400","FK048204-008.5MP-1408","FK048204-008.5PL-0926",
"FK048204-008.5SG-1407","FK048204-008.5SN-1383","FK048204-008.5WH-0834","FK048204-008.5WH-1039","FK054594-015","FK054595-008",
"FK380002-007BK-0231","FK380002-007BK-1200","FK380028-008","FK380028-008(15G)","FK380028-008BK-0042","FK380028-008BS-0043",
"FK380028-008CR-0044","FK380028-008GA-0046","FK380028-008MK-0277","FK380028-008NI-0050","FK380028-008PL-0054",
"FK380028-008PP-0055","FK380028-008RW-0056","FK380028-008SD-0057","FK380028-008SP-0058","FK380028-008TA-0059","FK380028-008WH-0061",
"FK380038-011BK","FK380038-011BK/GR","FK380038-011SD","FK380051-056BK/CT","FK380051-058BK/CT","FK380051-058SD/CT",
"FK380052-008","FK380052-008WH-0070","FK380075-025SD","FK380078-08.5BK-0250","FK380078-08.5BK-0250","FK380087-032BK",
"FK380087-032SD/CT","FK380111-006BK/CT","FK380111-006SD/CT","FK380112-006SD","FK380120-022BK/CT","FK380120-022SD/CT",
"FK380120-029BK/CT","FK380120-029SD/CT","FK380120-029SD/CT/GR","FK380120-083SD/GR","FK380122-025SD","FK380212-010","FK380212-010WH-0834",
"FK380239-003SD","FK380334-010.5","FK380334-010.5SG-1061","FK380334-010.5SG-1061","FK380334-010.5WH-1041","FK380504-008BK"
,"FK380504-008SD","FK380617-004WH-1704","FK380642-012BK","FW002007-004","FW002007-004BK-1092","FW002007-004MG-1093"
,"FW002007-004WH-1095","FW002007-006BK-1092","FW002007-006MG-1093","FW002007-006WH-1095","FW051849-007.5","FW101426-017.0",
"FW380006-006BK-0263","FW380009-019WH/HT","FW380009-032BL/HT","FW380009-032BL/HT/GR","FW380009-032WH/HT","FW380026-014",
"FW380026-014BK-0042","FW380026-014CR-0044","FW380026-014NI-0050","FW380026-014PP-0055","FW380026-014RW-0056",
"FW380026-014TA-0059","FW380026-014VA-0060","FW380026-014WH-0061","FW380034-015","FW380080-020BK-0148","FW380161-010",
"FW380230-025BK-1099","FW380471-032"];

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
if(todo5=="1"){

  return (

      <div>
          <Navbar/>

    <div className="reports">

          <h1 id = "reportHeadding">- Reports -</h1>
    
        <Paper className="paper">
         <form  noValidate autoComplete="off">
           <div className="input-fields-3">
    
            {/* quantity field */}
            <div className="quantity-tf">
            <TextField

                name="quantity"
              required value={userInput} 
              onChange={handleFormChange}
              label="Quantity"
              id="standard-start-adornment"
              helperText=""
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
                      placeholder="   Elastic type    *"
                      className="search"
                      value={searchtext}
                      onChange={handleChange1}
                    />
                    {getSuggestions()}
             </div>
           </div>
    
            {/* submit button */}
             <div className="submit-btn">
                 <Button variant="contained" color="primary" onClick={handleFormSubmit}>
                     SEARCH
                 </Button>
            </div>
    
          </form> 
          </Paper>
    
                 
    </div>
      </div>
      );

}
if(todo5=="2"){
  return(
  <div className="grid-background">
    {/*<ul><li> {todo4.response}</li><li> {todo4.jac}</li><li> {todo4.knt}</li><li> {todo4.pk}</li><li> {todo4.wev}</li><li> {todo4.WP}</li><li> {todo4.qa}</li><li> {todo4.dye}</li></ul>     */}

      <div className="percentage-vise">
          <h1>Percentage vise</h1>
      </div>

      <div className={classes.root}>
          <div className="first-grid">
              <Grid container spacing={1}>

                  <Grid item xs={6} sm={5}>
                      <div className="columns">
                      <Paper className={classes.paper}><b>Total waste percentage</b></Paper>
                      </div>
                  </Grid>

                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}>{todo4.response}</Paper>
                  </Grid>

                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}><b>jac</b></Paper>
                  </Grid>
                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}>{todo4.jac}</Paper>
                  </Grid>

                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}><b>knt</b></Paper>
                  </Grid>
                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}>{todo4.knt}</Paper>
                  </Grid>

                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}><b>pk</b></Paper>
                  </Grid>
                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}>{todo4.pk}</Paper>
                  </Grid>

                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}><b>wev</b></Paper>
                  </Grid>
                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}>{todo4.wev}</Paper>
                  </Grid>

                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}><b>WP</b></Paper>
                  </Grid>
                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}>{todo4.WP}</Paper>
                  </Grid>

                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}><b>qa</b></Paper>
                  </Grid>
                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}>{todo4.qa}</Paper>
                  </Grid>

                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}><b>dye</b></Paper>
                  </Grid>
                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}>{todo4.dye}</Paper>
                  </Grid>



              </Grid>
          </div>
      </div>

      <div className="kg-vise">
      <h1>Kilogram vise</h1>
     </div>
    {/*<ul><li> {todo4.q}</li><li> {todo4.jac1}</li><li> {todo4.knt1}</li><li> {todo4.pk1}</li><li> {todo4.wev1}</li><li> {todo4.WP1}</li><li> {todo4.qa1}</li><li> {todo4.dye1}</li></ul>     */}

      <div className={classes.root}>
          <div className="first-grid">
              <Grid container spacing={1}>
                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}><b>quantity</b></Paper>
                  </Grid>

                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}>{todo4.q}</Paper>
                  </Grid>

                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}><b>jac1</b></Paper>
                  </Grid>
                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}>{todo4.jac1}</Paper>
                  </Grid>

                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}><b>knt1</b></Paper>
                  </Grid>
                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}>{todo4.knt1}</Paper>
                  </Grid>

                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}><b>pk1</b></Paper>
                  </Grid>
                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}>{todo4.pk1}</Paper>
                  </Grid>

                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}><b>wev1</b></Paper>
                  </Grid>
                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}>{todo4.wev1}</Paper>
                  </Grid>

                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}><b>WP1</b></Paper>
                  </Grid>
                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}>{todo4.WP1}</Paper>
                  </Grid>

                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}><b>qa1</b></Paper>
                  </Grid>
                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}>{todo4.qa1}</Paper>
                  </Grid>

                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}><b>dye1</b></Paper>
                  </Grid>
                  <Grid item xs={6} sm={5}>
                      <Paper className={classes.paper}>{todo4.dye1}</Paper>
                  </Grid>



              </Grid>
          </div>
      </div>

    <form >
    {/*<input type='text' className="btn btn-primary" name="back"></input>*/}
        <div className="back-button">
        <Button variant="contained" color="primary" onClick={handleFormSubmit1}>
            Back To Form
        </Button>
         </div>
    </form>

  </div>
    
    
  );

}
if(todo5=="3"){
  return(

      <div>
          <Button variant="primary" disabled>
              <Spinner
                  as="span"
                  animation="grow"
                  size="sm"
                  role="status"
                  aria-hidden="true"
              />
              Loading...
          </Button>
      </div >

  );

}
 
}

export default Reports;