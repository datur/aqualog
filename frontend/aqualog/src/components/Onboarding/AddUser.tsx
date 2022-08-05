import { AxiosError } from "axios";
import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { addUser, getUserEmail, getUserExists } from "../../services/UserService";

export default function AddUser(){
    const navigate = useNavigate();

    const [user, setUser] = useState({
        first_name: '',
        last_name: '',
        email: String(),
    })

    const [userExists, setUserExists] = useState({
        exists: Boolean
    })

    useEffect(() => {
        async function existsRequest(){
            let response = await getUserExists()
            setUserExists(response)
        }
        async function getUserEmailRequest() {
            let response = await getUserEmail()
            setUser(response)
        }
        existsRequest()
        console.log(userExists)
        if (!userExists.exists){
            getUserEmailRequest()
        }
        else{
            navigate('/dashboard')
        }
    }, [])

    async function handleSubmit(event: React.FormEvent<HTMLFormElement>){
        event.preventDefault()
        try{
            let response = await addUser(user)
            navigate('/dashboard')
        }
        catch(error){
            const err = error as AxiosError
            alert(err.response?.data)
        }
    }

    function handleFirstNameChange(event: React.ChangeEvent<HTMLInputElement>){
        setUser(user => ({
            ...user,
            first_name: event.target.value
        }))
    }

    function handleLastNameChange(event: React.ChangeEvent<HTMLInputElement>){
        setUser(user => ({
            ...user,
            last_name: event.target.value
        }))
    }

    return (
        <div>
            Create User

            <form onSubmit={handleSubmit}>
                <label>
                    First Name:
                    <input type="text" name="firstName" onChange={handleFirstNameChange} value={user.first_name || ''}></input>
                </label>
                <br/>
                <label>
                    Last Name:
                    <input type="text" name="lastName" onChange={handleLastNameChange} value={user.last_name || ''}></input>
                </label>
                <br/>
                <label>
                    Email:
                    <input type="text" name="email" value={user.email} readOnly></input>
                </label>
                <br/>
                <input type="submit" value="Submit" />
            </form>
        </div>
    )
}