from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')
                #이름  # 모듈명   #URL 프리픽스
# bp는 Blueprint클래스로 생성한 객체
            #URL프리픽스에 url_prefix='/'대신 url_prefix='/main'이 입력되면 URL은 localhost:5000/main/

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    return redirect(url_for('question._list'))
#question은 등록된 블루프린트 이름, _list는 블루프린트에 등록된 함수명
#_list는 question_veiws.py에 등록된 함수이다. 유지보수가 쉬워진다.