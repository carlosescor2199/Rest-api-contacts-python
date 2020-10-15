from API import app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://unmzh7yffedswzzo:JbTFS0RvTSyf9FY1yYVP@b68edvt4jdgengl6qdhq-mysql.services.clever-cloud.com/b68edvt4jdgengl6qdhq"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)