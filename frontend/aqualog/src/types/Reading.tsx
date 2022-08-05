interface ReadingBase{
    tank_id: string
    ph: number
    temp: number
    ammonia: number
    nitrite: number
    nitrate: number
}

export interface FreshWaterReading extends ReadingBase {
    gh: number
    kh: number
}

export interface BrackishWaterReading extends ReadingBase{
    specific_gravity: number
}

export interface SaltWaterReading extends ReadingBase {
    specific_gravity: number
    alkalinity: number
    phosphate: number
    calcium: number
    magnesium: number
    iodine: number
    strontium: number
    silicate: number
}

export interface Reading {
    id: string
    tank_id: string
    ph: number
    temp: number
    ammonia: number
    nitrite: number
    nitrate: number
    gh: number
    kh: number
    specific_gravity: number
    alkalinity: number
    phosphate: number
    calcium: number
    magnesium: number
    iodine: number
    strontium: number
    silicate: number
    created: Date
}