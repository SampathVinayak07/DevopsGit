from flask import Flask
app=Flask(__name__)
@app.route("/")
def home():
    return "hello,this is CICD with GitAction for Flask App</h1"
@app.route("/about")
def about():
    return "welcone about page"
@app.route("/service:")
def service():
    return "welcome Service Page"
if __name__=='__main__':
    app.run(host="0.0.0.0",port=5000)