from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",message="偶奇、素数判定する数字、もしくは計算式を半角英数字で入力してください。")

@app.route("/result",methods=["GET"])
def result_get():
    #課題1 偶奇判定 入力値が無効な場合等の処理は見ての通りしてません(素数も同様)
    field = int(request.args.get("field",""))
    result = "偶数です" if field % 2 == 0 else "奇数です"
    return render_template("result.html",message=f"{field}は{result}。")

@app.route("/result",methods=["POST"])
def result_post():
    #課題2 素数判定 折角なのでPOST処理をそのまま使用
    field = int(request.form["field"])
    result = "素数です" if isPrime(field) else "素数ではありません"
    return render_template("result.html",message=f"{field}は{result}。")

def isPrime(num):
    if num == 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

@app.route("/result/calculator",methods=["GET"])
def calc_result_get():
    #課題3 入力値が無効な場合+悪意のある入力だった場合等の処理は課題1,2と同様にしてません
    field = request.args.get("field","")
    result = eval(field)
    return render_template("result.html",message=f"{field}の計算結果は{result}です。")



if __name__ == "__main__":
    app.run()