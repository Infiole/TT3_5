import React from 'react'
import { Container, Col, Row, Dropdown} from 'react-bootstrap';

const Post = ({id, title, description, commentNumber,likeNumber, posts}) => {
    
    var likes = posts.filter(function(element){
        return element.id === id
    }).length;

    var comments = posts.filter(function(element){
        return element.id === id
    }).length;
    return (
        <div>
            <Container className="border">
                <Row>
                    <Col xs={10}>
                        <div>
                            <span className='fw-bold'>{title}</span>
                        </div>
                        <div>{description}</div>
                        <div>
                            <span className="me-4">
                                <a href="/" className="text-decoration-none text-secondary"><i class="bi bi-chat"> {comments}</i></a>                      
                            </span>
                            <span>
                                <a href="/" className="text-decoration-none text-secondary"><i class="bi bi-heart"></i> {likes}</a> 
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