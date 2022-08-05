import React from "react";
import { useSessionContext } from "supertokens-auth-react/recipe/session";
import { useNavigate } from "react-router-dom";

export default function HomePage() {
    const navigate = useNavigate();

    return (
        <div>
            <h1>AquaLog</h1>

        </div>
    )
}