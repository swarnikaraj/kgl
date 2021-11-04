import os
import pdfkit

import pymysql
from flask import Flask
from flask_wkhtmltopdf import Wkhtmltopdf
from flask_sqlalchemy import SQLAlchemy

pymysql.install_as_MySQLdb()

basedir=os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

wkhtmltopdf = Wkhtmltopdf(app)
app.secret_key = 'super-secret-key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/kglab'


db = SQLAlchemy(app)

from kgl import routes





