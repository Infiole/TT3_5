import React from 'react'
import { Card } from 'react-bootstrap';
import '../../styles/Comments.css'

const Comment = ({key, title, description, image}) => {

    return (
        <div>
            <Card className='Comments'>
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

export default Comment