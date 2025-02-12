from flask import Flask, render_template, request
import _sqlite3

app = Flask(__name__) 

@app.route("/", methods=["GET", "POST"])
def menuPage():

    return render_template("menu.html")

@app.route("/fibonacci", methods=["GET", "POST"])
def fibPage():
    result = ""
    if request.method == "POST":             # If form submitted, calculate fib term of input and return value to html.
        result = fib(int(request.form["n"]))
    return render_template("fibonacci.html", result=result)

@app.route("/palindrome", methods=["GET", "POST"])
def palPage():
    result = ""
    if request.method == "POST":          # If form submitted, check if palindrome and return value to html.
        result = pal(request.form["str"])
    return render_template("palindrome.html", result=result)

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1 
    else:
        a, b = 0, 1
        for _ in range(n-2):
            a, b = b, a + b
        return b 
    
def pal(str):
    if str == str[::-1]:
        return "That is a palindrome :)"
    else:
        return "That is not a palindrome :("

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = "8080", debug = False)