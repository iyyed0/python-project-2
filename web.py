import http.server
import socket
import webbrowser
import pyqrcode
import os

PORT=8010
os.environ['USERPROFILE']

desktop=os.path.join(os.path.join(os.environ['USERPROFILE']),'OneDrive')
os.chdir(desktop)

handler = http.server.SimpleHTTPRequestHandler
hostname = socket.gethostname()

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(("8.8.8.8",80))
IP = "http://"+s.getsockname()[0] + ":" + str(PORT)
link = IP
url =pyqrcode.create(link)
url.png("myqr.png",scale=8)
html_content=f"""
<html>
<head>
    <title>project 2</title>
</head>
<body>
    <img src="myqr.png" alt="QR Code" style="width: 200px; height:200px;">
    <p>Serving at port: {PORT}</p>
    <p>Type this in your browser:{IP}</p>
    <p>Or scan the QR Code</p>
</body>
</html>
"""
with open ("project.html","w") as html_file:
    html_file.write(html_content)

webbrowser.open('project.html')
