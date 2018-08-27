import os
class Config:
	SECRET_KEY = '83d85693f189fa3d4ce51938bc41a455'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	MAIL_SERVER = 'smtp.163.com'
	MAIL_PORT = '25'
	MAIL_USE_TLS = False
	MAIL_USERNAME = os.environ.get('EMAIL_USER')
	MAIL_PASSWORD = os.environ.get('EMAIL_PASS')