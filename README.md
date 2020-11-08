# BitNews :newspaper:
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/unicorn-io/BitNews/graphs/commit-activity)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub contributors](https://img.shields.io/github/contributors/Naereen/StrapDown.js.svg)](https://GitHub.com/unicorn-io/BitNews/graphs/contributors/)
[![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://GitHub.com/unicorn-io/BitNews/graphs/contributors/)

This is a one of a kind web application for a modern news ecosystem to tackle fake news hassle free, written in flask-python. It further uses gunicorn as the WSGI interface to make it production ready.


<p align='center'><img src="https://i.ibb.co/gFg8542/jdge1.png" alt="jdge1" border="0" align='center'></p>

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
pip install -r requirements.txt
```

To deploy the application on the local host 
```
python run.py
```
To use an production ready WSGI Interface such as gunicorn
```
gunicorn --bind 0.0.0.0:8080 wsgi:app
```

## API's and References
<ul>
<li><a href="https://newsapi.org/">News Scrapping Api</a>
<li><a href="https://https://developer.ibm.com/technologies/blockchain/tutorials/develop-a-blockchain-application-from-scratch-in-python/">IBM Blockchain</a>
<li><a href="https://ipinfo.io/"> Geo Tagging API</a> 
<li><a href="https://ipfs.io/">Interpalanatory File System</a>
</ul>
