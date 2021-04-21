import React, { Component } from 'react'
import UserService from '../services/UserService'

class SearchComponent extends Component {
    constructor(props) {
        super(props)

        this.state = {
                elastic: []
        }
        
    }


    componentDidMount(refer){
        UserService.getSearch(refer).then((res) => {
            this.setState({ elastic: res.data});
        });
    }


    render() {
        return (
            <div>
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
export default SearchComponent
