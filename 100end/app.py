from flask import Flask, render_template

# 객체 생성
app = Flask(__name__)

# 기본 루트
## 실행하자마자자
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)