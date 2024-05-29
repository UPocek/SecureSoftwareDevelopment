import styles from '@/styles/Home.module.css';
import { useState } from 'react';

export default function Home() {
  const [message, setMessage] = useState('');

  async function submitfile(event) {
    event.preventDefault();

    const formData = new FormData();
    const fileInput = event.target.elements.file;

    if (fileInput.files.length === 0) {
      alert('Please select a file to upload');
      return;
    }

    formData.append('file', fileInput.files[0]);

    try {
      const response = await fetch('http://localhost:5001/unslippy', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        setMessage('File uploaded successfully!');
      } else {
        setMessage('Failed to upload file.');
      }
    } catch (error) {
      console.error('Error:', error);
      setMessage('An error occurred. Please try again.');
    }
  }

  return (
    <div className='container'>
      <h1>File Upload</h1>
      <form onSubmit={submitfile}>
        <input type="file" name="file" />
        <button type="submit">Submit</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}
