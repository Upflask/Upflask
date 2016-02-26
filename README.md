# Upflask
> A Flask file uploader

### Requirements:
- Python 3.5  
- Flask  
- Flask-Cache  
- A reverse proxy (Nginx)  
- Virtualenv *(optional)*
- tmux *(optional)*
- Gunicorn or uWSGI *(optional, but makes Nginx easier)*

***

### Installation
#### Linux
It's recommended, although optional, to create a virtual environment with *virtualenv*.

Clone this repo, create a virtual environment, and then source into it.
```bash
$ git clone https://github.com/Upflask/Upflask
$ pip3.5 install flask Flask-Cache
```

Afterwards, configure the `conf.py` file. Create **two** folders, `f/` and `file/`.

```bash
$ chmod +x server.py
$ ./server.py
```

#### Cygwin/Babun
Install [python3.5](http://cygwin.com/packages/x86_64/python3/) and pip3.5
```bash
$ git clone https://github.com/Upflask/Upflask
$ pip3.5 install flask Flask-Cache
```
If any errno11 errors occur, rebase and try again.

Similar to the Linux installations, afterwards, configure the `conf.py` file. Create **two** folders, `f/` and `file/`.
```bash
$ chmod +x server.py
$ ./server.py
```

## FAQ

#### Why did you make this?  
I used to have a PHP file uploader just called `Upload!`, but it was PHP.
I wanted to create a clone of that uploader's functions, but in Python.  

#### This looks like...Quadfile
Yeah, I stole all the Jinja2 template files.

However, the actual Python uploader is completely different from Quadfile, since <a
href="https://twitter.com/QuadPiece">QuadPiece</a> hadn't submitted the source code at the time of Upflask's inception.

#### Why doesn't X work?  
No idea, but you can either sumbit an issue here or try asking me on my Twitter.  

#### You didn't make a Mac tutorial
I don't own a Mac therefore, will not.

### Do I have to use Python3.5?
No but you **MUST** use `Python3` as it was created in `Python3.5`, however `Python3.4 or older` will work just fine.

***
## Troubleshooting

#### Any other errors:  
Check to make sure you are using Python 3.5 and not 3.4 or any older version

#### Flask module not found:
```bash
$ pip3.5 install flask
```
#### Import module flask.ext.cache not found:  
```bash
$ pip3.5 install Flask-Cache
```
