import React, { useEffect, useState } from "react";
import { useLocation, useNavigate, useParams } from "react-router-dom";
import { AddUserTank, DeleteUserTank, UpdateUserTank } from "../../services/TankService";
import { Tank } from "../../types/Tank";

interface LocationState {
    update: boolean
    currTank: Tank
  }

export default function EditTank(props: any){
    let params = useParams();
    let navigate = useNavigate();
    const location = useLocation()
    const state = location.state as LocationState


    const [tank, setTank] = useState<Tank | undefined>(undefined);
    const [update, setUpdate] = useState(Boolean);
    const [unitType, setUnitType] = useState(false);

    let title = update ? "Update Tank" : "Add Tank"

    useEffect(() => {
        if (state !== null){
            const { update, currTank } = state;
            title = update ? "Update Tank" : "Add Tank"
            setTank(currTank)
            setUpdate(update)
            setUnitType(mapUnitTypeToBool())
        }
        else{
        setTank({unit_type: "LITRES", name: "", water_type: "FRESH", capacity: 0})
        }
    }, [])

    function mapUnitTypeToBool() {
        let result = tank?.unit_type == "GALLONS" ? true : false
        return result
    }

    function mapUnitTypeFromBool(val: boolean) {
        return val ? "GALLONS" : "LITRES"
    }

    function onNameChange(event: React.ChangeEvent<HTMLInputElement>){
        setTank(tank => ({
            ...tank!,
            name: event.target.value
        }))
    }

    function onCapacityChange(event: React.ChangeEvent<HTMLInputElement>){

        let total = parseInt(event.target.value)

        setTank(tank => ({
            ...tank!,
            capacity: total
        }))
    }

    function onUnitTypeChange(){
        setTank(tank => ({
            ...tank!,
            unit_type: mapUnitTypeFromBool(!unitType)
        }))
        setUnitType(!unitType);
    }

    function onWaterTypeChange(event: React.ChangeEvent<HTMLSelectElement>){
        setTank(tank => ({
            ...tank!,
            water_type: event.target.value
        }))
    }

    function handleSubmit(event: React.FormEvent<HTMLFormElement>){
        event.preventDefault()
        if (update){
            let t = UpdateUserTank(params.id!, tank!)
            navigate(-1)
        } else {
            let r = AddUserTank(tank!)
            navigate(-1)

        }
    }

    function handleDelete(event: React.FormEvent<HTMLButtonElement>){
        let r = DeleteUserTank(params.id!)
        navigate(-1)
    }

    return (
        <div>
            {title}
            <form onSubmit={handleSubmit}>
                <label>
                    Name:
                    <input
                        type="text"
                        name="tankName"
                        required={true}
                        value={tank?.name || ""}
                        onChange={onNameChange}></input>
                </label>
                <label>
                    Capacity:
                    <input
                        type="number"
                        name="tankCapacity"
                        required={true}
                        min={5}
                        value={tank?.capacity || ""}
                        onChange={onCapacityChange}></input>
                </label>
                <label className="switch">
                    Unit Type:
                    <input
                        type="checkbox"
                        defaultChecked={unitType}
                        onChange={onUnitTypeChange}
                    />
                    {/* <span className="slider"></span> */}
                </label>
                <label>
                    Water Type:
                    <select 
                        id="water-type" 
                        value={tank?.water_type || "FRESH"}
                        onChange={onWaterTypeChange}>
                        <option value="FRESH">Fresh</option>
                        <option value="BRACKISH">Brackish</option>
                        <option value="SALT">Salt</option>
                    </select>
                </label>
                <label>
                    { update ? 
                    <button onClick={handleDelete}>
                        Delete
                    </button>
                     : ""
                    }
                </label>
                <br/>
                <input type="submit" value="Submit" />
            </form>
        </div>
    )
}