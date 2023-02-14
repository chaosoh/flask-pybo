import os

BASE_DIR = os.path.dirname(__file__)    # 현재 파일이 위치한 폴더 myproject

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "dev"
