import React, {Component} from 'react'
import UserService from './services/UserService'
import'bootstrap/dist/css/bootstrap.min.css';
import './Product.css';
import Navbar from "../../Side bar/Navbar";
import {useState} from 'react';
import {Button} from "@material-ui/core";
import {Spinner} from "react-bootstrap";

class ProductComponent extends Component {
    constructor(props) {
        super(props)
        // eslint-disable-next-line react-hooks/rules-of-hooks


        this.state = {
                elastic: []
        }
        
    }


    componentDidMount(){
        UserService.getUsers().then((res) => {
            this.setState({ elastic: res.data});
        });



    }

    render() {
        // eslint-disable-next-line react-hooks/rules-of-hooks


        return (
            <div className="product">
                <Navbar/>
                <div className="product-heading">
                 <h2 className="text-center">- Product -</h2>
                    </div>

                 <br></br>
                <div className="table-padding">
                 <div className = "table-responsive-sm">
                        <table className = "table table-striped table-bordered table-info">

                            <thead className="thead-dark">
                                <tr>
                                    <th> JOBNO</th>
                                    <th> ITEM CODE</th>
                                    <th> COLOUR GROUP</th>
                                    <th> TOTAL QUANTITY</th>
                                    <th> TOTAL WASTAGE</th>
                                    <th> WASTAGE PRECENTAGE</th>
                                </tr>
                            </thead>
                            <tbody>
                                {
                                    this.state.elastic.map(
                                        elastic => 
                                        <tr key = {elastic.id}>
                                             <td> {elastic.JobNo} </td>   
                                             <td> {elastic.ItemCode}</td>
                                             <td> {elastic.ColorGroup}</td>
                                             <td> {elastic.Total_Quantity}</td>
                                             <td> {elastic.Total_Wastage}</td>
                                             <td> {elastic.waste_pecentage}</td>
                                        </tr>
                                    )
                                }
                            </tbody>
                        </table>

                 </div>
            </div>
            </div>
        )
    }
}

export default ProductComponent
