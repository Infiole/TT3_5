import React from 'react'
import { Container, Row, Form, Button} from 'react-bootstrap';

const Tweetbox = ({username, time, message, commentNumber,likeNumber}) => {
    return (
        <div>
            <Container className="border">
                <Row>
                    <Form>
                        <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                            <Form.Label className="fw-bold">Tweet in the box below!</Form.Label>
                            <Form.Control placeholder="What's happening?" />
                            <Button variant="primary" className="mt-3 d-flex ms-auto" type="submit">
                                Tweet
                            </Button>
                        </Form.Group>
                    </Form>
                </Row>
            </Container>
        </div>
    )
}

export default Tweetbox