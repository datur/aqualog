import { Base } from "./Base"
import { Tank } from "./Tank"

export interface UserEditable {
    first_name: string,
    last_name: string,
    email: string
}

export interface User extends Base, UserEditable{
    tanks: [Tank]
}