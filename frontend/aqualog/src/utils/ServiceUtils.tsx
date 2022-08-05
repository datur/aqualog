import { Tank, TankRequest, TankResponse } from "../types/Tank"

export function mapTankToRequest(tank: Tank) : TankRequest {
    let wt = convertWaterTypeToInt(tank.water_type!)!
    let ut = convertUnitTypeToInt(tank.unit_type!)!
    return {
        name: tank.name,
        capacity: tank.capacity,
        unit_type : ut,
        water_type : wt
    }
}

export function mapTankFromResponse(tank: TankResponse){

}

function convertWaterTypeToInt(wt: string){
    switch(wt){
        case "FRESH":
            return 1
        case "SALT":
            return 2
        case "BRACKISH":
            return 3
    }
}

function convertUnitTypeToInt(wt: string){
    switch(wt){
        case "LITRES":
            return 1
        case "GALLONS":
            return 2
    }
}