import { makeStyles, Paper } from '@material-ui/core';
import React from 'react';
import EmployeeForm from './EmployeeForm';

const useStyles = makeStyles(theme => ({
    pageContent:{
        margin:theme.spacing(5),
        padding:theme.spacing(3)
    }
}))

export default function Employees(){

    const classes = useStyles();
    
    return(
        
        <Paper className={classes.pageContent}>
        <EmployeeForm/>
        </Paper>
    )
}