import React from "react";
import { Link, NavLink, useNavigate } from "react-router-dom";
import { isEmailVerified } from "supertokens-auth-react/recipe/emailpassword";
import { signOut, useSessionContext } from "supertokens-auth-react/recipe/session";


export default function NavBar() {
    const { userId, doesSessionExist } = useSessionContext();

    const navigate = useNavigate();

    async function loginClicked() {
        navigate("/auth");
    }

    async function logoutClicked() {
        await signOut();
        navigate("/");
    }

    return (
        <div>
            {dashboardLink(doesSessionExist)} <span> </span>
            {tanksLink(doesSessionExist)} <span> </span>
            {newTankLink(doesSessionExist)} <span> </span>
            {profileLink(doesSessionExist)} <span> </span>
            {newReadingLink(doesSessionExist)} <span> </span>

            <NavLink
                to={doesSessionExist ? "/" : "/auth"}
                onClick={doesSessionExist ? logoutClicked : loginClicked}
                >
            {doesSessionExist ? "Log Out" : "Log In"}
            </NavLink>
        </div>
    )
}

function dashboardLink(doesSessionExist: boolean){

    return (
        doesSessionExist ? (
        <NavLink
            to="/dashboard"
        >
            Dashboard
        </NavLink>) : null
    )
}

function tanksLink(doesSessionExist: boolean){

    return (
        doesSessionExist ? (
        <NavLink
            to="/tanks"
        >
            Tanks
        </NavLink>) : null
    )
}

function newReadingLink(doesSessionExist: boolean){

    return (
        doesSessionExist ? (
            <NavLink
                to="/reading/add"
            >
                Add New Reading
            </NavLink>) : null
    )
}

function newTankLink(doesSessionExist: boolean){

    return (
        doesSessionExist ? (
            <NavLink
                to="/tank/add"
            >
                Add New Tank
            </NavLink>) : null
    )
}

function profileLink(doesSessionExist: boolean){
    return (
        doesSessionExist ? (
            <NavLink
                to="/profile"
            >
                Profile
            </NavLink>) : null
    )
}