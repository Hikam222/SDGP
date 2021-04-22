import { Grid, makeStyles, TextField } from '@material-ui/core';
import React,{useState,useeffect} from 'react';

const useStyles = makeStyles(theme =>({
    root:{
        '& .MuiFormControl-root': {
            width:'80%',
            margin:theme.spacing(1)
        }
    }
}
))

const initialFValues = {
    id:0,
    fullName:'',
    email:'',
    mobile:'',
    city:'',
    gender:'male',
    departmentId:'',
    hireDate:new Date(),
    isPermanant:false,

}
export default function EmployeeForm(){

    const [values,setvalues] = useState(initialFValues);
    const classes = useStyles();
    return(
        <form className={classes.root}>
            <Grid container>
                <Grid item xs={6}>
                    <TextField
                    variant="outlined"
                    label="Full name"
                    value={values.fullName}
                    />

                    <TextField
                    variant="outlined"
                    label="Email"
                    value={values.email}
                    />
                </Grid>

                <Grid item xs={6}>
                
                </Grid>

            </Grid>
        </form>
    )
}