import React from 'react'
import { Card } from 'react-bootstrap';

const Post = ({key, title, description, image}) => {

    return (
        <div>
            <Card style={{ width: '32rem', margin: 'auto'}}>
                <Card.Img variant="top" src={image} />
                <Card.Body>
                    <Card.Title>{title}</Card.Title>
                    <Card.Text>
                    {description}
                    </Card.Text>
                </Card.Body>
            </Card>
        </div>
    )
}

export default Post