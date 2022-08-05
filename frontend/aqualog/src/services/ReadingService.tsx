import axios from "axios";
import Session from "supertokens-auth-react/recipe/session";
import { getApiDomain } from "../App";
import { Reading } from "../types/Reading";

Session.addAxiosInterceptors(axios);

export async function addReading(reading: Reading){
    let response = await axios.post(getApiDomain() + "/api/reading", reading)
    return response.data
}

export async function listReadings(tank_id: string){
    let response = await axios.get(getApiDomain() + "/api/readings", {params: {tank_id: tank_id}})
    let data: Reading[] = []
    response.data.readings.forEach((element: Reading) => {
        data.push(element as Reading)
    });
    return data
}

export async function deleteReadings(reading_ids: Array<string>){

    let response = await axios.post(getApiDomain() + "/api/readings/delete", {"reading_ids": reading_ids})

    return response.data
}