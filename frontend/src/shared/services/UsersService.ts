import { Token } from "../types/Token";
import BaseAPIService from "./BaseAPIService"

export interface LoginParams{
    name:string,
    password:string
};

export default class UsersService extends BaseAPIService{
    async login({name, password}:LoginParams){
        
        const response = await fetch(`${this.baseUrl}/users/login`, {
            method: 'POST',
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({name, password})
        });

        console.log(JSON.stringify({name, password}));

        const result = (await response.json()) as Token;

        console.log(result);
    }
}