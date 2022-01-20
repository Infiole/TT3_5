import React from 'react'
import { Card } from 'react-bootstrap';
import '../../styles/Posts.css'

const Post = ({key, title, description, image, likes, comments}) => {

    return (
        <div>
            <Card className='Posts'>
                <Card.Img variant="top" src={image} />
                <Card.Body>
                    <Card.Title>{title}</Card.Title>
                    <Card.Text>
                    {description}
                    </Card.Text>
                    <div>
                        <span className="me-4">
                            <a href="/" className="text-decoration-none text-secondary"><i class="bi bi-heart"></i> {likes.length}</a>
                        </span>
                        <span>
                            <a href="/" className="text-decoration-none text-secondary"><i class="bi bi-chat"> {comments.length}</i></a>
                        </span>
                    </div>
                </Card.Body>
            </Card>
        </div>
    )
}

export default Post