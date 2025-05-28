from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        try:
            width = float(request.form["width"])
            height = float(request.form["height"])
            fabric_width = float(request.form["fabric_width"])

            area = round(width * height, 3)
            ping = round(area / 3.3, 3)
            tsai = round(ping * 36, 3)

            result = {
                "area": area,
                "ping": ping,
                "tsai": tsai
            }
        except:
            result = {"error": "輸入錯誤，請輸入正確數字格式"}

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
