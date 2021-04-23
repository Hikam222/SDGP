import axios from 'axios';

const USER_API_BASE_URL = "http://localhost:5000";

class UserService {

    getUsers(){
        return axios.get(USER_API_BASE_URL+'/elastic');
    }

    getLogin(){
        return axios.get(USER_API_BASE_URL);
    }


}

export default new UserService()