from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

# 애플리케이션 팩토리
# flask run으로 실행해야 함.
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

     # 블루프린트
    from views import main_views
    app.register_blueprint(main_views.bp)
    import models

    return app