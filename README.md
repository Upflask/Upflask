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

How to install on Windows (Not tested but should work in theory):
1. Install the latest version of Python3 for Windows
2. (Optional) Install Git
3. pip or pip3 install flask
4. Configure the "conf.py" file
5. Create two folders, f/ and file/
8. python or python3 or python3.5 server.py
9. That's it.

## FAQ

Why did you make this?  
I used to have a PHP file uploader just called "Upload!", but, it was PHP.
I wanted to create a clone of that uploader's functions, but in Python.  

This looks like...Quadfile  
LOOKS like but that's just the static page, since I'm uncreative when it comes to web 
design, however, the actual Python uploader is completely different from Quadfile, as <a 
href="https://twitter.com/QuadPiece">QuadPiece</a> didn't sumbit the source code when I made it, however he has now, I've seen its complexity, and decided that it is too complex for a file uploader, so therefore, I will not make any changes to match his.  

Why doesn't X work?  
No idea, but you can try asking me on my Twitter.  

You didn't make a Mac tutorial  
I don't own one, therefore, make it yourself.

WHY IS THERE OTHER LANGUAGES IN HERE??
I'm too lazy to completely seperate English from the other languages, so feel free to remove them manually.

## Troubleshooting

Non-ASCII character issues:
DON'T USE PYTHON2, USE PYTHON3  

Flask module not found:
pip3 install flask (or sudo)
