import React from "react";
import {useNavigate} from 'react-router-dom';

export default function NotFound(){
    const navigate = useNavigate();

    return (
        <div>
            <h1>Oops... Looks there is an error</h1>
            <button onClick={() => navigate(-1)}>Go Back</button>
        </div>
    )
}