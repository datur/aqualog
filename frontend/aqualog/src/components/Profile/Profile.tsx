import React, { useEffect, useState } from "react";
import { getUser } from "../../services/UserService";
import { User } from "../../types/User";

export default function Profile(props: {update: boolean}){
    let title = props.update ? "Update Profile" : "Profile"

    const [user, setUser] = useState<User | undefined>(undefined);

    useEffect(() => {
        getUser().then(user => setUser(user))
    }, [])

    return (
        <div>
            <h3>{title} </h3> <br/>
            {user?.first_name} <br/>
            {user?.last_name} <br/>
            {user?.email} <br/>
        </div>
    )
}