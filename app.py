
from flask import Flask,render_template
import server



app = Flask(__name__)



@app.route("/",methods=["GET"])
def home():
    return render_template("index.html",ip=server.host)




if __name__ == "__main__":
    app.run()