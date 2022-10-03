from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'b58f7064154253'
app.config['MYSQL_DATABASE_PASSWORD'] = '32de4f18'
app.config['MYSQL_DATABASE_DB'] = 'heroku_dbb5a8d2e1d2fbf'
app.config['MYSQL_DATABASE_HOST'] = 'us-cdbr-east-06.cleardb.net'
mysql.init_app(app)