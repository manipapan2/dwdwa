# from flask import Flask, render_template
# from flask_socketio import SocketIO
# import pyautogui
# import os
# output = os.popen("ipconfig").read()
# lines = output.split("\n")

# for line in lines:
#     if "IPv4 Address" in line:
#         ip_address = line.split(":")[-1].strip()
#         # print(f"My local IP address: {ip_address}")


# app = Flask(__name__)
# app.config["SECRET_KEY"] = "secret!"
# socketio = SocketIO(app)
# # socketio = SocketIO(app, async_mode='gevent')
# # hostname = socket.gethostname()
# # local_ip = socket.gethostbyname(hostname)

# @app.route("/")
# def index():
#     return render_template("index.html", adad=adad)

# adad = 0
# @socketio.on("click")
# def handle_click():
#     global adad
#     adad += 1
#     print(f"you clicked the button {adad} times")
#     pyautogui.click()
#     socketio.emit("update_adad", adad)



# if __name__ == "__main__":
#     socketio.run(app, host=ip_address, port=5000)

from flask import Flask, render_template
from flask_socketio import SocketIO
import pyautogui
import os
output = os.popen("ipconfig").read()
lines = output.split("\n")

for line in lines:
    if "IPv4 Address" in line:
        ip_address = line.split(":")[-1].strip()
        # print(f"My local IP address: {ip_address}")


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)
# socketio = SocketIO(app, async_mode='gevent')
# hostname = socket.gethostname()
# local_ip = socket.gethostbyname(hostname)

@app.route("/")
def index():
    return render_template("index.html", adad=adad)

adad = 0
@socketio.on("click")
def handle_click():
    global adad
    adad += 1
    print(f"you clicked the button {adad} times")
    pyautogui.click()
    socketio.emit("update_adad", adad)



if __name__ == "__main__":
    socketio.run(app, host=ip_address, port=5000)
