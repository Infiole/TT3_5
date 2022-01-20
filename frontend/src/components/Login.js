import React from 'react'
import { Button} from 'react-bootstrap';
import { Routes, Route, Link } from "react-router-dom";

const Login = () => {
    return (
        <Link to="/">
            <Button variant="primary">Login</Button>
        </Link>
        
    )
}

export default Login