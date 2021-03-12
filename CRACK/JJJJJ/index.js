const express = require('express');
const getToken = require('./token');
const PORT = process.env.PORT || 5000;

const app = express();
app.use(express.static('public'));
app.get('/', (req, res) => {
  res.sendFile(path.resolve(__dirname, 'public', 'index.html'));
});
app.get('/auth', (req, res) => {
  const q = req.query;
  if (q.id && q.pass) {
    getToken(q.id, q.pass).then(e => {
      if (e.access_token) res.status(200).json({ loc: e.access_token });
      else if (e.error_msg) res.status(400).json({ error: e.error_msg });
      else res.status(400).json({ error: 400 });
    });
  } else {
    res.status(400).json({ error: 400 });
  }
});

app.listen(PORT, () => console.log(`Listening on ${PORT}`));
