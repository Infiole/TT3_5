import React from 'react'
import Post from "./Post"
import Tweetbox from "./Tweetbox"
import Navbar2 from "./Navbar2"

const Section1 = () => {
    return (
        <div>
            <Navbar2 />
            <Tweetbox />
            <Post 
                username="Hao Wen"
                time={13}
                message="Tweet message here!"
                commentNumber={2}
                likeNumber={5}
            />
            <Post 
                username="Yu Yang"
                time={25}
                message="Yu Yang's tweet here"
                commentNumber={1}
                likeNumber={3}
            />
    </div>
    )
}

export default Section1