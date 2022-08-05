import { Tank } from "../types/Tank"

export function getMaterialTableColumns(tank: Tank){
        var base = [
            {title: "Temperature", field: "temp"},
            {title: "Ph", field: "ph"},
            {title: "Ammonia", field: "ammonia"},
            {title: "Nitrite", field: "nitrite"},
            {title: "Nitrate", field: "nitrate"},
        ]
        var fresh = [
            {title: "Gh", field: "gh"},
            {title: "Kh", field: "kh"},

        ]
        var brackish = [
            {title: "Specific Gravity", field: "specific_gravity"},


        ]
        var salt = [
            {title: "Specific Gravity", field: "specific_gravity"},
            {title: "Alkalinity", field: "alkalinity"},
            {title: "Phosphate", field: "phosphate"},
            {title: "Calcium", field: "calcium"},
            {title: "Magnesium", field: "magnesium"},
            {title: "Iodine", field: "iodine"},
            {title: "Strontium", field: "strontium"},
            {title: "Silicate", field: "silicate"},

        ]
        switch (tank.water_type){
            case "FRESH":
                console.log(tank.water_type)
                return[
                    ...base,
                    ...fresh,
                    {title: "Created at", field: "created"}
                ]
            case "BRACKISH":
                return[
                    ...base,
                    ...brackish,
                    {title: "Created at", field: "created"}
                ]
            case "SALT":
                return[
                    ...base,
                    ...salt,
                    {title: "Created at", field: "created"}
                ]
        }
    }