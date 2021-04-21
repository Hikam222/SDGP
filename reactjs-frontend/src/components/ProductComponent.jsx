import React, { Component } from 'react'
import UserService from '../services/UserService'

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
                {/* <div span="right" >
                <form action="/search"	method="GET" >
                    <table class="none" id="close">
                    <tr>
                    <td></td><td></td>
                    <td><b>Search Reference:</b></td>
                    <td><select name="refer" required>
                        <option value="JobNo">JobNo</option>
                        <option value="ItemCode">ItemCode</option>
                        <option value="ColorGroup">ColorGroup</option>
                        <option value="Total_Quantity">Total_Quantity</option>
                        <option value="Total_Wastage">Total_Wastage</option>
                    </select></td>
                    <td><input type="text" name="key" placeholder="Search" size="15" /></td>
                    <td><button type="submit">Search</button></td>
                    </tr>
                    </table>
                </form>
                </div> */}
                 <h2 className="text-center">Elastic List</h2>
                 <br></br>
                 <div className = "row">
                        <table className = "table table-striped table-bordered">

                            <thead>
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
