import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
    const [numbers, setNumbers] = useState('');
    const [average, setAverage] = useState(null);
    const [error, setError] = useState(null);

    const calculateAverage = async () => {
        try {
            const response = await axios.post('http://localhost:3001/calculate-average', {
                numbers: numbers.split(',').map(Number)
            });
            setAverage(response.data.average);
            setError(null);
        } catch (err) {
            setError(err.response.data.error);
            setAverage(null);
        }
    };

    return (
        <div className="App">
            <h1>Average Calculator</h1>
            <input
                type="text"
                value={numbers}
                onChange={(e) => setNumbers(e.target.value)}
                placeholder="Enter numbers separated by commas"
            />
            <button onClick={calculateAverage}>Calculate Average</button>
            {average !== null && <h2>Average: {average}</h2>}
            {error && <h2>Error: {error}</h2>}
        </div>
    );
}

export default App;
