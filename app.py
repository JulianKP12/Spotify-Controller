from flask import request, session, Flask, render_template, redirect
from controller import Controller
import threading
import requests
import serial
import time

global created
global token

app = Flask(__name__)
app.secret_key = "haha funny poopy haha stinkyyyyyyy oh noooooo"
created = False


# ----------------------------------------------------
# Api geneuk
# ----------------------------------------------------



def handle_coms(code):
	controller = Controller(code)

	ser = serial.Serial("COM5", 9600)
	time.sleep(2)

	print("Listening...")
	while True:
		recieved_raw = ser.readline().decode()
		recieved = recieved_raw.rstrip()

		if recieved == "B":
			controller.previous()

		elif recieved == "P":
			if controller.pauseMode == 1:
				controller.pause()

			else:
				controller.play()

		elif recieved == "F":
			controller.next()

	ser.close()



# ----------------------------------------------------
# Webserver geneuk
# ----------------------------------------------------



@app.route("/")
def home():
	if "code" in session:
		if not created:
			threading.Thread(target=handle_coms, args=(session["code"],)).start()
		return render_template("index.html", loggedin=True)

	else:
		if len(request.args) > 0:
			session["code"] = request.args["code"]
			if not created:
				threading.Thread(target=handle_coms, args=(session["code"],)).start()
			return render_template("index.html", loggedin=True)

		return render_template("index.html")



@app.route("/logout")
def logout():
	session.pop("code", None)
	return redirect("http://localhost:5000/")


app.run(debug=True)