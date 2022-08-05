import { timeStamp } from "console";
import React, { useEffect, useState } from "react";
import { useLocation, useNavigate, useParams } from "react-router-dom";
import { addReading } from "../../services/ReadingService";
import { ListUsersTanks } from "../../services/TankService";
import { Reading } from "../../types/Reading";
import { Tank } from "../../types/Tank";

interface LocationState{
    currTank: Tank
}

export default function AddReading(){
    let params = useParams();
    let navigate = useNavigate();
    const location = useLocation()
    const state = location.state as LocationState

    const [tankOptions, setTankOptions] = useState<JSX.Element[]>();
    const [tankWaterTypes, setTankWaterTypes] = useState<{ id: string; water_type: string; }[]>();
    const [readingWaterType, setReadingWaterType] = useState<string>();
    const [reading, setReading] = useState<Reading>();

    async function getTankDropdown(){
        let items: JSX.Element[] = []
        let tankWaterType: { id: string; water_type: string; }[] = []
        let tanks = await ListUsersTanks()

        tanks.forEach(element => {
            items.push(<option key={element.name} value={element.id}>{element.name}</option>)
            tankWaterType.push({id : element.id!, water_type : element.water_type})
        });
        items.sort((a, b) => {
            if (a.key! < b.key!) return -1;
            if (a.key! > b.key!) return 1;
            return 0;
        })
        var wt = tankWaterType!.find(f => {return f.id === items[0].props.value})
        setReadingWaterType(wt!.water_type)
        setTankOptions(items)
        setTankWaterTypes(tankWaterType)
    }

    useEffect(() => {
        if (state !== null){
            setReadingWaterType(state.currTank.water_type)
        }
        else{
            getTankDropdown()
        }
    }, [])

    function onTankDropdownChange(event: React.ChangeEvent<HTMLSelectElement>){
        let value = event.target.value;
        var wt = tankWaterTypes!.find(f => {return f.id === value})
        setReadingWaterType(wt!.water_type)
        setReading(reading => ({
            ...reading!,
            tank_id: value
        }))
    }

    function onTempChange(event: React.ChangeEvent<HTMLInputElement>){
        setReading(reading => ({
            ...reading!,
            temp: parseFloat(event.target.value)
        }))
    }

    function onPhChange(event: React.ChangeEvent<HTMLInputElement>){
        setReading(reading => ({
            ...reading!,
            ph: parseFloat(event.target.value)
        }))
    }

    function onAmmoniaChange(event: React.ChangeEvent<HTMLInputElement>){
        setReading(reading => ({
            ...reading!,
            ammonia: parseFloat(event.target.value)
        }))
    }

    function onNitriteChange(event: React.ChangeEvent<HTMLInputElement>){
        setReading(reading => ({
            ...reading!,
            nitrite: parseFloat(event.target.value)
        }))
    }

    function onNitrateChange(event: React.ChangeEvent<HTMLInputElement>){
        setReading(reading => ({
            ...reading!,
            nitrate: parseFloat(event.target.value)
        }))
    }

    function onGhChange(event: React.ChangeEvent<HTMLInputElement>){
        setReading(reading => ({
            ...reading!,
            gh: parseInt(event.target.value)
        }))
    }

    function onKhChange(event: React.ChangeEvent<HTMLInputElement>){
        setReading(reading => ({
            ...reading!,
            kh: parseInt(event.target.value)
        }))
    }

    function onSpecificGravityChange(event: React.ChangeEvent<HTMLInputElement>){
        setReading(reading => ({
            ...reading!,
            specific_gravity: parseFloat(event.target.value)
        }))
    }

    function onAlkalinityChange(event: React.ChangeEvent<HTMLInputElement>){
        setReading(reading => ({
            ...reading!,
            alkalinity: parseFloat(event.target.value)
        }))
    }

    function onPhosphateChange(event: React.ChangeEvent<HTMLInputElement>){
        setReading(reading => ({
            ...reading!,
            specific_gravity: parseFloat(event.target.value)
        }))
    }

    function onCalciumChange(event: React.ChangeEvent<HTMLInputElement>){
        setReading(reading => ({
            ...reading!,
            calcium: parseFloat(event.target.value)
        }))
    }

    function onMagnesiumChange(event: React.ChangeEvent<HTMLInputElement>){
        setReading(reading => ({
            ...reading!,
            magnesium: parseFloat(event.target.value)
        }))
    }

    function onIodineChange(event: React.ChangeEvent<HTMLInputElement>){
        setReading(reading => ({
            ...reading!,
            iodine: parseFloat(event.target.value)
        }))
    }

    function onStrontiumChange(event: React.ChangeEvent<HTMLInputElement>){
        setReading(reading => ({
            ...reading!,
            strontium: parseFloat(event.target.value)
        }))
    }
    
    function onSilicateChange(event: React.ChangeEvent<HTMLInputElement>){
        setReading(reading => ({
            ...reading!,
            silicate: parseFloat(event.target.value)
        }))
    }

    function handleReadingSubmit(event : React.FormEvent<HTMLFormElement>){
        event.preventDefault();
        reading!.tank_id = params.id!
        var _ = addReading(reading!)
        navigate(-1)
    }

    return (
        <div>
            Add Reading { (state !== null )? `for tank: ${state.currTank.name}` : "" }

            <form onSubmit={handleReadingSubmit}>
                { (state !== null) ? "" : (
                <label>
                    Tank:
                    <select id="userTanks"
                    onChange={onTankDropdownChange}
                    >
                        {tankOptions}
                    </select>
                </label>)
                }
                <label>
                    Temperature:
                    <input
                    type="number"
                    step="0.1"
                    name="temperature"
                    required={true}
                    onChange={onTempChange}>
                    </input>
                </label>
                <br/>
                <label>
                    PH:
                    <input
                    type="number"
                    step="0.01"
                    name="ph"
                    onChange={onPhChange}>
                    </input>
                </label>
                <br/>
                <label>
                    Ammonia:
                    <input
                    type="number"
                    step="0.01"
                    name="ammonia"
                    onChange={onAmmoniaChange}></input>
                </label>
                <br/>
                <label>
                    Nitrite:
                    <input
                    type="number"
                    step="0.01"
                    name="nitrite"
                    onChange={onNitriteChange}></input>
                </label>
                <br/>
                <label>
                    Nitrate:
                    <input
                    type="number"
                    step="0.01"
                    name="nitrate"
                    onChange={onNitrateChange}></input>
                </label>
                <br/>
                {
                    (readingWaterType === "FRESH") ?
                    ([<label>
                        Gh:
                        <input
                        type="number"
                        name="gh"
                        onChange={onGhChange}></input><br/>
                    </label>, <label>
                    Kh:
                    <input
                    type="number"
                    name="kh"
                    onChange={onKhChange}></input>
                </label>]
                    ) : ""
                }
                {
                    (readingWaterType === "BRACKISH") ? (
                        [
                        <label>
                        Specific Gravity:
                        <input
                        type="number"
                        step="0.001"
                        name="specificgravity"
                        onChange={onSpecificGravityChange}></input>
                        </label>,
                        ]
                    ) : ""
                }
                {
                    (readingWaterType === "SALT") ? (
                        [
                        <label>
                        Specific Gravity:
                        <input
                        type="number"
                        step="0.001"
                        name="specificgravity"
                        onChange={onSpecificGravityChange}></input>
                        </label>,
                        <label>
                        Alkalinity:
                        <input
                        type="number"
                        name="alkalinity"
                        onChange={onAlkalinityChange}></input>
                        </label>,
                        <label>
                        Phosphate:
                        <input
                        type="number"
                        step="0.1"
                        name="phosphate"
                        onChange={onPhosphateChange}></input>
                        </label>,
                        <label>
                        Calcium:
                        <input
                        type="number"
                        name="calcium"
                        onChange={onCalciumChange}></input>
                        </label>,
                        <label>
                        Magnesium:
                        <input
                        type="number"
                        name="magnesium"
                        onChange={onMagnesiumChange}></input>
                        </label>,
                        <label>
                        Iodine:
                        <input
                        type="number"
                        step="0.1"
                        name="iodine"
                        onChange={onIodineChange}></input>
                        </label>,
                        <label>
                        Strontium:
                        <input
                        type="number"
                        name="strontium"
                        onChange={onStrontiumChange}></input>
                        </label>,
                        <label>
                        Silicate:
                        <input
                        type="number"
                        step="0.1"
                        name="silicate"
                        onChange={onSilicateChange}></input>
                        </label>,
                        ]

                    ) : ""
                }
                <br/>
                <input type="submit" value="Submit" />
            </form>
        </div>
    )
}