import { useState } from 'react';
import axios from 'axios';

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [question, setQuestion] = useState('');
  const [ocr, setOcr] = useState('');
  const [answer, setAnswer] = useState('');

  const handleSubmit = async () => {
    if (!file || !question) return;
    const formData = new FormData();
    formData.append('file', file);
    formData.append('question', question);

    const res = await axios.post('https://organic-zebra-5x57gwjw9w5fvx5r-8000.app.github.dev/process', formData);
    setOcr(res.data.ocr_text);
    setAnswer(res.data.answer);
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Image OCR + LLM Q&A</h2>
      <input type="file" onChange={e => setFile(e.target.files?.[0] || null)} />
      <br /><br />
      <input
        type="text"
        placeholder="Ask a question about the image..."
        value={question}
        onChange={e => setQuestion(e.target.value)}
        style={{ width: '80%' }}
      />
      <br /><br />
      <button onClick={handleSubmit}>Submit</button>

      {ocr && (
        <>
          <h3>OCR Text</h3>
          <pre>{ocr}</pre>
        </>
      )}

      {answer && (
        <>
          <h3>Answer</h3>
          <p>{answer}</p>
        </>
      )}
    </div>
  );
}
