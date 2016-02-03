# Upflask
A Flask file uploader

Requirements:
Python3  
Flask  
A reverse proxy (Nginx)  
Virtualenv (optional)  
tmux (optional but highly recommened)  
Gunicorn (optional but makes Nginx easier)  

How to install on Linux:
1. git clone
2. Make virtual environment (optional but recommened) with virtualenv
3. Source into that virtualenv
4. pip3 install flask
5. Configure the "conf.py" file
6. Create two folders, f/ and file/
7. chmod +x server.py
8. ./server.py
9. That's it.

How to install on Cygwin/Babun:
1. git clone
2. install python3
3. Somehow install easy_install for python3 and install pip3 or get python3 to install pip3
4. pip3 install flask
5. If any errno11 errors occur, rebase and try again
6. Configure the "conf.py" file
7. Create two folders, f/ and file/
8. chmod +x server.py
9. ./server.py
10. That's it.

## FAQ

Why did you make this?  
I used to have a PHP file uploader just called "Upload!", but, it was PHP.
I wanted to create a clone of that uploader's functions, but in Python.  

This looks like...Quadfile  
LOOKS like but that's just the static page, since I'm uncreative when it comes to web 
design, however, the actual Python uploader is completely different from Quadfile, as <a 
href="https://twitter.com/QuadPiece">QuadPiece</a> hasn't submitted the source code.  

Why doesn't X work?  
No idea, but you can try asking me on my Twitter.  

You didn't make a Mac tutorial  
I don't own one, therefore, make it yourself.
