from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import MetaData

import config

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()
#--------------------------------------------------------------------------------
# db와 migrate는 create_app에서 생성하면 블루프린트와 같이 다른 모듈을 불러올수 없이 때문에
# create_app함수 밖에서 생성하고 실제 객체초기화는 create_app함수에서 init_app함수를 통해 진행한다
#--------------------------------------------------------------------------------


def create_app():
    # create_app()는 플라스크내부에 정의된 함수이다. 이름이 바뀌면 동작x
    # create_app 함수가 app 객체를 생성해 반환

    app = Flask(__name__) #app.config 환경변수에 부름
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    from . import models

    # 블루프린트
    from .views import main_views, question_views, answer_views, auth_views, comment_views, comment_views, vote_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(comment_views.bp)
    app.register_blueprint(vote_views.bp)
    #필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime
    return app

