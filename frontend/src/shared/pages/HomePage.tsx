import UsersService from "../services/UsersService";

export default function HomePage(){
    (new UsersService().login({name:"admin", password: "12345678"}));
    return <>This is the home page</>;
}