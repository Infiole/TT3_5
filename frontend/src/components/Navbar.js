import React from 'react'
import { Container, navbar, Nav} from 'react-bootstrap';

const Navbar = ({username, time, message, commentNumber,likeNumber}) => {
    return (
            <Navbar bg="primary" variant="dark">
                <Container>
                    <Navbar.Brand href="#home">Navbar</Navbar.Brand>
                    <Nav className="me-auto">
                        <Nav.Link href="#home">Home</Nav.Link>
                        <Nav.Link href="#features">Features</Nav.Link>
                        <Nav.Link href="#pricing">Pricing</Nav.Link>
                    </Nav>
                </Container>
            </Navbar>
    )
}

export default Navbar