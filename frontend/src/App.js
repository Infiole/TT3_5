import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Post from "./components/Post"
import Tweetbox from "./components/Tweetbox"

function App() {
  return (
    <div>
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
  );
}

export default App;
