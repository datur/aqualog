import { Base } from "./Base";
import { Reading } from "./Reading";

export interface Tank extends Base {
    name: string,
    capacity: number,
    unit_type: string,
    water_type: string,
    readings?: Array<Reading>
}

export interface TankResponse {
    name: string,
    capacity: number,
    unit_type: number ,
    water_type: number,
}

export interface TankRequest extends TankResponse {}