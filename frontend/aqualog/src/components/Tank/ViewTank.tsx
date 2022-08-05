import MaterialTable, { Column } from "material-table";
import { ThemeProvider, createTheme } from '@mui/material';
import React, { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { ReadUserTank } from "../../services/TankService";
import {Tank} from "../../types/Tank";
import { toTitleCase } from "../../utils/Text";
import { getMaterialTableColumns } from "../../utils/Reading";
import { Reading } from "../../types/Reading";
import { deleteReadings } from "../../services/ReadingService";
import { AreaChart, CartesianGrid, Legend, Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";

export default function ViewTank(){

    let params = useParams();
    const [tank, setTank] = useState<Tank | undefined>(undefined);
    const [columns, setColumns] = useState<Column<object>[]>();

    var options = {
        selection: true
    }

    const defaultMaterialTheme = createTheme();

    function deleteSelectedReadings(evt: any, data: any){
        let readingIdsToDelete: string[] = []
        data.forEach((element: Reading) => {
            readingIdsToDelete.push(element.id)

        });
        deleteReadings(readingIdsToDelete)

        var nt = ReadUserTank(tank!.id!)
        nt.then(t => {
            t.readings?.filter(reading => !readingIdsToDelete.some(id => id === reading.id))
            setTank(t)
        })

    }

    useEffect(() => {
        async function getTank(){
            let response = await ReadUserTank(params.id!);
            setTank(response);
            setColumns(getMaterialTableColumns(response))
        }
        if (tank === undefined){
            getTank()
        }
    }, [tank]);

    return (
        <div >
            <Link
            to={`/tank/${tank?.id}/reading/add`}
            key={params.id}
            state={{currTank: tank}}
            >Add Reading</Link>
            <Link
            to={`/tank/${tank?.id}/readings`}
            key={params.id + "readings"}
            state={{currTank: tank}}
            >List Readings</Link>
            <div>
                Name: {tank?.name} <br/>
                Capacity: {tank?.capacity} {toTitleCase(tank?.unit_type!)} <br/>
                Water Type: {toTitleCase(tank?.water_type!)} <br/>
                { tank !== undefined ?
                "Number of Readings: " + tank!.readings!.length : ""
                }
            </div>
            <div>
                <Link
                to={`/tank/${tank?.id}/update`}
                key={tank?.id+"updatepage"}
                state={{update: true, currTank: tank}}>
                    Update
                </Link>
            </div>

            <div style={{ width: '100%', height: '50%' }}>
            <link
                rel="stylesheet"
                href="https://fonts.googleapis.com/icon?family=Material+Icons"
                />
            <ThemeProvider theme={defaultMaterialTheme}>
            <MaterialTable
                columns={columns === undefined ? [] : columns}
                data={tank?.readings === undefined? [] : tank.readings}
                title={"Readings"}
                options={options}
                actions={
                    [
                        {
                          tooltip: 'Remove All Selected Readings',
                          icon: 'delete',
                          onClick: deleteSelectedReadings
                        }
                    ]
                }/>
            </ThemeProvider>
            </div>
            <div >
            Temperature:
            <ResponsiveContainer width={'100%'} height={'100%'} aspect={3}>
            <LineChart data={tank?.readings}
            margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="created" allowDataOverflow={false}/>
                <YAxis type="number" domain={['dataMin - 0.25', 'dataMax + 0.25']} />
                <Tooltip />
                <Legend />
                <Line type="monotone" dataKey="temp" stroke="#a3c1ad" strokeWidth={3} />
            </LineChart>
            </ResponsiveContainer>
            Ph:
            <ResponsiveContainer width={'100%'} height={'100%'} aspect={3}>
                <LineChart data={tank?.readings}
                margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="created" allowDataOverflow={false}/>
                    <YAxis type="number" domain={['dataMin - 0.25', 'dataMax + 0.25']} />
                    <Tooltip />
                    <Legend />
                    <Line type="monotone" dataKey="ph" stroke="#a3c1ad" strokeWidth={3} />
                </LineChart>
            </ResponsiveContainer>
            Ammonia:
            <LineChart width={(window.innerWidth)} height={250} data={tank?.readings}
            margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="created" allowDataOverflow={false}/>
                <YAxis type="number" domain={[(dataMin: number) => (0 - dataMin === 0 ? 0 : Math.abs(dataMin)), (dataMax: number) => (dataMax + 0.1)]} />
                <Tooltip />
                <Legend />
                <Line type="monotone" dataKey="ammonia" stroke="#a3c1ad" strokeWidth={3} />
            </LineChart>
            Nitrite:
            <LineChart width={(window.innerWidth)} height={250} data={tank?.readings}
            margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="created" allowDataOverflow={false}/>
                <YAxis type="number" domain={['auto', 'dataMax + 0.25']}/>
                <Tooltip />
                <Legend />
                <Line type="monotone" dataKey="nitrite" stroke="#a3c1ad" strokeWidth={3} />
            </LineChart>
            Nitrate:
            <LineChart width={(window.innerWidth)} height={250} data={tank?.readings}
            margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="created" allowDataOverflow={false}/>
                <YAxis type="number" domain={['auto', 'dataMax + 0.25']} />
                <Tooltip />
                <Legend />
                <Line type="monotone" dataKey="nitrate" stroke="#a3c1ad" strokeWidth={3} />
            </LineChart>
            Kh:
            <LineChart width={(window.innerWidth)} height={250} data={tank?.readings}
            margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="created" allowDataOverflow={false}/>
                <YAxis type="number" domain={[0, 'dataMax + 1']}/>
                <Tooltip />
                <Legend />
                <Line type="monotone" dataKey="kh" stroke="#a3c1ad" strokeWidth={3} />
            </LineChart>
            Gh:
            <LineChart width={(window.innerWidth)} height={250} data={tank?.readings}
            margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="created" allowDataOverflow={false}/>
                <YAxis type="number" domain={[0, 'dataMax + 1']} />
                <Tooltip />
                <Legend />
                <Line type="monotone" dataKey="gh" stroke="#a3c1ad" strokeWidth={3} />
            </LineChart>
            </div>
        </div>
    )
}