import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
#데이터베이스 접속주소                                                    #pybo.db=데이터베이스파일
SQLALCHEMY_TRACK_MODIFICATIONS = False
#SQLAlchemy의 이벤트를 처리하는 옵션
SECRET_KEY = "dev"
#Flask-WTF사용키