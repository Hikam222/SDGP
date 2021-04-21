import axios from 'axios';

const USER_API_BASE_URL = "http://localhost:5000/elastic";

class UserService {

    getUsers(){
        return axios.get(USER_API_BASE_URL);
    }

    getSearch(refer){
        return axios.get("http://localhost:5000/search/"+refer)
    }
    

}

export default new UserService()