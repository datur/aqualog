import { ThemeProvider, createTheme } from '@mui/material';
import MaterialTable, { Column } from "material-table";
import React, { useEffect, useState } from "react";
import { Link, useLocation, useNavigate, useParams } from "react-router-dom";
import { listReadings } from "../../services/ReadingService";
import { Reading } from "../../types/Reading";
import { Tank } from "../../types/Tank";
import { getMaterialTableColumns } from '../../utils/Reading';

interface LocationState {
    currTank: Tank
  }

export default function ListReadings(){
    let params = useParams();
    let navigate = useNavigate();

    const location = useLocation()
    const state = location.state as LocationState

    const [readings, setReadings] = useState<Reading[]>();
    const [columns, setColumns] = useState<Column<object>[]>();

    async function getReadings(){
        let response = await listReadings(params.id!)
        setReadings(response)
    }

    useEffect(() => {
        getReadings()
        setColumns(getMaterialTableColumns(state.currTank as Tank))
    },[])

    const defaultMaterialTheme = createTheme();

    return (
        <div style={{ maxWidth: "100%" }}>
            <div style={{ width: '100%', height: '100%' }}>
            <link
                rel="stylesheet"
                href="https://fonts.googleapis.com/icon?family=Material+Icons"
                />
            <ThemeProvider theme={defaultMaterialTheme}>
            <MaterialTable columns={columns === undefined ? [] : columns} data={readings === undefined? [] : readings} title={"Readings"} />
            </ThemeProvider>
            </div>
        </div>
    )
}