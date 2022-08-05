import axios from "axios";
import { getApiDomain } from "../App";
import { User, UserEditable } from "../types/User";

export async function getUserEmail(){
    let response = await axios.get(getApiDomain() + "/api/user_email");
    return response.data;
}

export async function getUserExists(){
    let response = await axios.get(getApiDomain() + "/api/user_exists");
    return response.data;
}

export async function addUser(user: UserEditable){
    let response = await axios.post(getApiDomain() + "/api/user", user)
    console.log(response)
    return response
}

export async function getUser(): Promise<User> {
    let response = await axios.get(getApiDomain() + "/api/user")
    console.log(response.data)
    return response.data
}