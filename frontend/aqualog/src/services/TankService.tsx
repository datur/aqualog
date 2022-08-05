import axios from "axios";
import Session from "supertokens-auth-react/recipe/session";
import { getApiDomain } from "../App";
import { Tank } from "../types/Tank";
import { mapTankToRequest } from "../utils/ServiceUtils";


Session.addAxiosInterceptors(axios);

export async function ListUsersTanks() : Promise<Array<Tank>> {
    let response = await axios.get(getApiDomain() + "/api/tanks");
    return response.data.tanks;
}

export async function AddUserTank(tank: Tank) : Promise<Tank> {
    let tankRequest = mapTankToRequest(tank)
    let response = await axios.post(getApiDomain() + "/api/tank", tankRequest)
    return response.data
}

export async function UpdateUserTank(id: string, tank: Tank) : Promise<Tank> {
    let tankRequest = mapTankToRequest(tank)
    let response = await axios.patch(getApiDomain() + "/api/tank", tankRequest, {params: {tank_id: id}})
    console.log(response)
    return response.data
}

export async function ReadUserTank(id: string) : Promise<Tank> {
    let response = await axios.get(getApiDomain() + "/api/tank", {params: {tank_id: id} });
    response.data.readings.forEach((element: { created: any; }) => {
        let date = new Date(Date.parse(element.created))
        let dateStr = `${date.getDate()}/${date.getMonth()}/${String(date.getFullYear()).slice(2)} ${date.getHours()}:${date.getMinutes()}`
        element.created = dateStr
    })
    return response.data;
}

export async function DeleteUserTank(id: string) {
    let response = await axios.delete(getApiDomain() + "/api/tank", {params: {tank_id: id, soft:true}})
    return response.data
}