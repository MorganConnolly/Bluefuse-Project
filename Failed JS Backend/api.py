from flask import Flask, render_template, request

app = Flask(__name__) 

@app.route("/", methods=["GET", "POST"])
def menuPage():
    fib_result = ""
    pal_result = ""
    if request.method == "POST":
        try:
            fib_result = fib(int(request.form["n"]))
        except:
            pal_result = pal(request.form["str"])
    return render_template("menu.html", fib_result=fib_result, pal_result=pal_result)

# @app.route("/fibonacci", methods=["GET", "POST"])
# def fibPage():
#     fib_result = ""
#     if request.method == "POST":
#         fib_result = fib(int(request.form["n"]))
#     return render_template("fibonacci.html", fib_result=fib_result)

# @app.route("/palindrome", methods=["GET", "POST"])
# def palPage():
#     pal_result = ""
#     if request.method == "POST":
#         pal_result = pal(request.form["str"])
#     return render_template("palindrome.html", pal_result=pal_result)

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
    app.run(host = "0.0.0.0", port = "8080", debug = True)