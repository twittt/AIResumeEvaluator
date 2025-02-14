import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';
import axios from 'axios';
import ReactMarkdown from 'react-markdown';

function App() {
  const [resume, setResume] = useState(null);
  const [jobDescription, setJobDescription] = useState(null);
  const [result, setResult] = useState(null);
  const [submitted, setSubmitted] = useState(false);

  const handleResumeChange = (e) => {
    setResume(e.target.files[0]);
  };

  const handleJobDescriptionChange = (e) => {
    setJobDescription(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log('Submitting')
    const formData = new FormData();
    formData.append('resume', resume);
    formData.append('jobDescription', jobDescription);

    try {
      console.log("This is right before we make the request")
      const response = await axios.post('http://127.0.0.1:5000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      setResult(response.data);
      console.log("This is right before it sk=hould change")
      setSubmitted(true);
    } catch (error) {
      console.error('Error uploading files', error);
    }
  };

  const handleReset = () => {
    setResume(null);
    setJobDescription(null);
    setResult(null);
    setSubmitted(false);
  };

  return (
    <div>
      <h1>Resume and Job Description Matcher</h1>
      {!submitted ? (
        <form onSubmit={handleSubmit}>
          <div>
            <label>Upload Resume (.doc, .pdf, .docx):</label>
            <input type="file" accept=".doc,.pdf, .docx" onChange={handleResumeChange} required />
          </div>
          <div>
            <label>Upload Job Description (.doc, .pdf):</label>
            <input type="file" accept=".doc,.pdf, .docx" onChange={handleJobDescriptionChange} required />
          </div>
          <button type="submit">Submit</button>
        </form>
      ) : (
        <div>
          <h2>Match Result</h2>
          <p>Match Score: {result.score}</p>
          <h3>Suggestions to Improve Resume</h3>
           <ReactMarkdown>{result.suggestions}</ReactMarkdown>
          <button onClick={handleReset}>Upload Another</button>
        </div>
      )}
    </div>
  );
}

export default App;