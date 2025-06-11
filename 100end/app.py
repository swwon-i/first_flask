from flask import Flask, render_template, request, redirect, url_for, session

# 객체 생성
app = Flask(__name__)
app.secret_key = 'tjrdnjs'

# 기본 루트
## 실행하자마자자
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

# GET : 초기에 경로로 들어가면 작성 폼을 보여주자
# POST : 입력받은 폼 가지고 뭔가를 보여주자
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method== 'POST':
        name = request.form.get('name')
        mail = request.form.get('email')
        message = request.form.get('message')
        print(name, mail, message)
        
        # 그냥 패턴 readme 참조
        # return render_template('contact.html', success=True)
        
        # PRG 패턴
        session['success'] = True
        return redirect(url_for('contact'))
    
    # get 방식
    success = session.pop('success', False)
    return render_template('contact.html', success=success)

if __name__ == '__main__':
    app.run(debug=True)