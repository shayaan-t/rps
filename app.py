from distutils.log import debug
from pickle import TRUE
from flask import Flask,render_template,session,request
import random
app = Flask(__name__)

@app.route("/rps", methods = ["GET","POST"])
def rps():
    if request.method == "GET":
        return render_template("rps.html")
    elif request.method == "POST":
        user_choice = request.form.get("rps")
        rps = ["rock","paper","scissors"]
        message = ""
        computer_choice = random.choice(rps)
        if user_choice == computer_choice:
            message = "It is a TIE"
        elif user_choice == "rock" and computer_choice == "paper":
            message = "Computer WINS"
        elif user_choice == "rock" and computer_choice == "scissors":
            message = "You WIN"
        elif user_choice == "paper" and computer_choice == "rock":
            message = "You WIN"
        elif user_choice == "paper" and computer_choice == "scissors":
            message = "Computer WINS"
        elif user_choice == "scissors" and computer_choice == "rock":
            message = "Computer WINS"
        elif user_choice == "scissors" and computer_choice == "paper":
            message = "You WIN"
        return render_template("rps.html", message = message,uc = user_choice, cc = computer_choice)
        
            
        

if __name__ == "__main__":
    app.run(debug=TRUE)