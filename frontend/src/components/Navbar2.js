import React from 'react'
import { Container, Navbar, Nav} from 'react-bootstrap';
import { Routes, Route, Link } from "react-router-dom";

const Navbar2 = () => {
    return (
            <Navbar bg="primary" variant="dark">
                <Container>
                    <Navbar.Brand href="#home">Navbar</Navbar.Brand>
                    <Nav className="me-auto">
                        <Nav.Link href="#home">Home</Nav.Link>
                        <Nav.Link href="#features">Features</Nav.Link>
                        <Link to="/Logout" className="text-white text-decoration-none mt-2">Logout</Link>
                    </Nav>
                </Container>
            </Navbar>
    )
}

export default Navbar2

