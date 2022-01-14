import {useState} from 'react';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import CircularProgress from '@mui/material/CircularProgress';
import Paper from '@mui/material/Paper';
import './MainPage.css';

function ReferencedPaper({count, paperId}) {
  return <p key={paperId}>{paperId} used {count} time{count !== 1 && 's'}</p>;
}

export default function MainPage() {
  const [author, setAuthor] = useState('');
  const [mostReferenced, setMostReferenced] = useState({
    init: true,
    isLoading: false,
    data: [],
    error: '',
  });

  function handleSubmit(e) {
    e.preventDefault();
    if (author.length === 0) {
      setMostReferenced({
        init: false,
        isLoading: false,
        data: [],
        error: 'Search field is empty',
      })
      return;
    }
    setMostReferenced({
      init: false,
      isLoading: true,
      data: [],
      error: '',
    });

    fetch(`http://localhost:5000/author/${author}/citations`).then(res => res.json())
    .then((res) => {
      setMostReferenced({
        isLoading: false,
        ...res,
      })
    })
    .catch(err => {
      setMostReferenced({
        isLoading: false,
        data: [],
        error: err.message,
      })
    });

  }

  function handleChange(e) {
    setAuthor(e.target.value);
  }
  
  let results = null;
  if (mostReferenced.init) {
    results = null;
  }
  else if (mostReferenced.isLoading) {
    results = <CircularProgress/>;
  }
  else if (mostReferenced.error && mostReferenced.error.length > 0) {
    results = <Paper>{mostReferenced.error}</Paper>;
  }
  else {
    const {name, mostReferenced: referencedPapers} = mostReferenced.data;
    results = (
      <Paper>
        <h2>{name}</h2>
        {
          referencedPapers.map(({count, paperId}) => <ReferencedPaper key={paperId} count={count}paperId={paperId} />)
        }
      </Paper>
    )
  }
  return (
    <div className="main-page">
      <h1>Most Commonly Referenced Papers</h1>
      
      <form className="main-page-info" onSubmit={handleSubmit}>
        <TextField id="standard-basic" label="Author's Name or AuthorId" variant="standard" fullWidth value={author} onChange={handleChange}/>
        <Button sx={{marginLeft: '20px'}} onClick={handleSubmit} variant="contained">Search</Button>
      </form>

      {results}
    </div>
  )
}