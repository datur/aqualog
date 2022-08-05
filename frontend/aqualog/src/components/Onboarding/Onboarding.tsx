import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { SendVerifyEmail } from "supertokens-auth-react/lib/build/recipe/emailverification/components/themes/emailVerification/sendVerifyEmail";
import { isEmailVerified } from "supertokens-auth-react/recipe/emailpassword";
import { useSessionContext } from "supertokens-auth-react/recipe/session";
import { getUserExists } from "../../services/UserService";
import AddUser from "./AddUser";
import ConfirmEmail from "./ConfirmEmail";


export default function Onboarding(){
    const [emailVerified, setEmailVerified] = useState(false);
    const [userExists, setUserExists] = useState(false);

    const navigate = useNavigate();

    useEffect(() => {
        async function checkEmailVerified(){
            setEmailVerified(await isEmailVerified())
        }
        async function checkUserExists() {
            var exists = await getUserExists()
            setUserExists(exists.exists)
        }
        checkUserExists()
        if (userExists){
            navigate('/dashboard')
        }
        else {
        checkEmailVerified()
        }
    })

    return (
        <div>
            {userExists ? null : <AddUser/>}
            {emailVerified ? null : <ConfirmEmail/>}
        </div>
    )
}
