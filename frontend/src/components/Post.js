import React from 'react'
import { Container, Col, Row, Dropdown} from 'react-bootstrap';

const Post = ({username, time, message, commentNumber,likeNumber}) => {
    return (
        <div>
            <Container>
                    <Row className="border w-50">
                            <Col xs={10}>
                                <div>
                                    <span className='fw-bold'>{username}</span>
                                    <span> . {time}m</span>
                                </div>
                                <div className="mt-3">{message}</div>
                                <div className="mt-3">
                                    <span className="me-4">
                                        <a href="/" className="text-decoration-none text-secondary"><i class="bi bi-chat"> {commentNumber}</i></a>                      
                                    </span>
                                    <span>
                                        <a href="/" className="text-decoration-none text-secondary"><i class="bi bi-heart"></i> {likeNumber}</a> 
                                    </span>
                                </div>
                            </Col>
                            <Col xs={2}>
                                <Dropdown>
                                    <Dropdown.Toggle id="dropdown-basic" variant="white">
                                        <i class="bi bi-three-dots"></i>
                                    </Dropdown.Toggle>

                                    <Dropdown.Menu>
                                        <Dropdown.Item href="#/action-1">Delete</Dropdown.Item>
                                        <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>
                                        <Dropdown.Item href="#/action-3">Something else</Dropdown.Item>
                                    </Dropdown.Menu>
                                </Dropdown>
                            </Col>
                    </Row>
            </Container>
        </div>
    )
}

export default Post