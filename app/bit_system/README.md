---
noteId: "a4b293f0210211eb9800418121b1b313"
tags: []

---

# BitNews  :full_moon:
This is a web application for a news ecosystem written in flask-python. It further uses gunicorn as the WSGI interface to make it production ready.

[![Python Versions](https://img.shields.io/pypi/pyversions/yt2mp3.svg)](https://pypi.python.org/pypi/yt2mp3/)
[![Website cv.lbesson.qc.to](https://img.shields.io/website-up-down-green-red/http/cv.lbesson.qc.to.svg)](http://cv.lbesson.qc.to/)
[![GitHub contributors](https://img.shields.io/github/contributors/Naereen/StrapDown.js.svg)](https://GitHub.com/unicorn-io/BitNews/graphs/contributors/)
## Getting Started
To run the application
```
git clone https://www.github.com/unicorn-io/BitNews
```

As you are into the repository locally you can setup an virtual environment (optional)
```
python -m venv env
source /env/Scripts/activate
```

Now make sure you have installed all the requirements freezed in requirements.txt
```
pip install requirements.txt
```

Finally we are all setup goahead and bing the port as mentioned in the script (127.0.0.1:8080) and the application is running!.
```
gunicorn --bind 127.0.0.1:8080 wsgi:app
```



