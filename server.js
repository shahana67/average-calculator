const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3001;

app.use(bodyParser.json());

app.post('/calculate-average', (req, res) => {
    const numbers = req.body.numbers;
    if (!Array.isArray(numbers) || numbers.length === 0) {
        return res.status(400).json({ error: 'Invalid input' });
    }

    const sum = numbers.reduce((acc, num) => acc + num, 0);
    const average = sum / numbers.length;

    res.json({ average });
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});




//Run in cmd
//node server.js
