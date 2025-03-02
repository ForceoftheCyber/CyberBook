# CyberBook

## Building instructions

### Initial setup
Make a Python virtual environment:

Windows:
```bash
python -m venv ".venv"
.\.venv\Scripts\activate
python -m pip install -r requirements.txt
```

### Building the book

```bash
teachbooks build book
```

### Launch locally
```bash
teachbooks serve
```
This will provide you with a link to open up the built book in a browser.
