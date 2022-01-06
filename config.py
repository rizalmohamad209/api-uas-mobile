import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    HOST = "localhost"
    DATABASE = "berita"
    USERNAME = "root"
    PASSWORD = "Rizalmohamad123"
    JWT_SECRET_KEY = str(os.environ.get("JWT_SECRET"))
    #SQLALCHEMY_DATABASE_URI = 'mysql://'+USERNAME+':'+PASSWORD+'@'+HOST+'/'+DATABASE
    SQLALCHEMY_DATABASE_URI = 'postgresql://piaaijqlullvfi:c7b5b771c4c5555ddbccff9c6b5e38147c2cf5db7451d7a5e7a3b3703a1aaef0@ec2-34-239-196-254.compute-1.amazonaws.com:5432/de7141salhmp9n'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
