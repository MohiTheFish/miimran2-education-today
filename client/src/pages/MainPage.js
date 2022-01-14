import {useState, useEffect} from 'react';
import TextField from '@mui/material/TextField';
import CircularProgress from '@mui/material/CircularProgress';
import './MainPage.css';

export default function MainPage() {
  const [author, setAuthor] = useState('');
  const [authorList, setAuthorList] = useState({
    isLoading: true,
    isErrored: false,
    data: [],
  });
  const [mostReferenced, setMostReferenced] = useState({
    isLoading: false,
    isErrored: false,
    data: []
  });

  useEffect(() => {
    async function fetchAuthorList() {
      fetch('http://localhost:5000/author').then((res) => res.json())
      .then(res => {
        console.log(res);
      })
    }
    fetchAuthorList();
  }, [])
  function handleSubmit(e) {
    e.preventDefault();
    console.log(author);
  }

  function handleChange(e) {
    setAuthor(e.target.value);
  }
  return (
    <div className="main-page">
      <h1>Most Commonly Referenced Papers</h1>
      
      <form className="main-page-info" onSubmit={handleSubmit}>
        <TextField id="standard-basic" label="Author's Name" variant="standard" fullWidth value={author} onChange={handleChange}/>
      </form>
    </div>
  )
}