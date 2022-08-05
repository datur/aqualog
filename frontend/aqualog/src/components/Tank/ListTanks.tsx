import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { ListUsersTanks } from "../../services/TankService";
import {Tank} from "../../types/Tank";

export default function ListTanks(){

    const [tanks, setTanks] = useState<Array<Tank>>();

    useEffect(() => {
        async function getTanks(){
            let response = await ListUsersTanks();
            setTanks(response);
        }
        getTanks();
    }, []);
    

    return (
        <div>
            <Link to={"/tank/add"}>Add
            </Link> <br/>
            Tanks:
            {
                tanks?.map((tank) => (
                    <div key={tank.id! + tank.created}>
                    <Link
                    to={`/tank/${tank.id}`}
                    key={tank.id}>
                        {tank.name}
                    </Link>
                    <Link
                    to={`/tank/${tank.id}/update`}
                    key={tank.id + "updatelink"}
                    state={{update: true, currTank: tank}}>
                        Update
                    </Link>
                    </div>
                ))
            }
        </div>
    )
}