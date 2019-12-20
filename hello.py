#flask는 python 내부에 없기 때문에 외부에서 가져옴
from flask import Flask, escape, request, render_template

# 코드 app.run(debug=True)를 입력하기전에는 (입력후엔 python hello.py로 실행
# env FLASK_APP=hello.py flask run을 깃배쉬에 입력해야 실행됨 

#[python내부에 있는 랜덤기능을 불러옴]
import random
app = Flask(__name__)
import requests
import json

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!!!'


@app.route('/myname')
def myname():
    return '이재천입니다.'

# 랜덤으로 점심메뉴 추천해주는 서버
# def는 함수 함수로 정의를함
@app.route('/lunch')
def lunch():
    menus = ['양자강', '김밥카페', '20층', '한식뷔폐', '편의점'] 
    lunch = random.choice(menus)
    return lunch

# 아이돌 백과사전
# 이상태에선 한글이 깨져서 보여서
# JSON Viewer Chrome을 웹스토에서 받아서 설치해주자
@app.route('/idol')
def idol():
    idols = {
        'bts':{
            '지민':25,
            '랩몬스터':23
        },
        'rv':'레드벨벳',
        '핑클':{
            '이효리':'거꾸로해도이효리',
            '옥주현':'35'
        },
        'SES':['유진','바다','슈']
    }
    return idols





@app.route('/post/<int:num>')    
def post(num):
    posts = ['0번 포스트', '1번 포스트', '2번 포스트']
    return posts[num]


# 실습 cube뒤에 전달된 수의 세제곱수를 화면에 보여주세요
# 1->
# 2->8

# str() : 숫자를 문자로 바꿔주는 함수

@app.route('/cube/<int:num>')
def cube(num):
    cubed = num
    return str(cubed)

#클라이언트에게 html 파일을 주고싶어요!

@app.route('/html')
def html():
    return render_template('hello.html')

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    age = request.args.get('age')
    # age = request.args['age'] 위와 거의 유사하게 동작 거의 같은코드
    return render_template('pong.html',age_in_html=age)

# 로또번호를 가져와서 보여주는 서버
@app.route('/lotto_result/<int:round>')
def lotto_result(round):
    url = f'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo={round}'
    result = requests.get(url).json()

    winner = []
    for i in range(1,7):
        winner.append(result.get(f'drwtNo{i}'))
        # winner.append(result[f'drwNo{i}'])
    
    winner.append(result.get('bnusNo'))

    return json.dumps(winner)

app.run(debug=True)