import React, { Component } from 'react'
import UserService from './services/UserService'
import'bootstrap/dist/css/bootstrap.min.css';
import Navbar from "../../Side bar/Navbar";
class ProductComponent extends Component {
    constructor(props) {
        super(props)

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
        return (
            <div>
                <Navbar/>
                 <h2 className="text-center">Product</h2>
                 <br></br>
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
        )
    }
}

export default ProductComponent
