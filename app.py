from flask import Flask, render_template, request
from database import create_put_requestdb, put_request

app = Flask(__name__)


 


@app.route("/")
def myapp():
    #cursor = mysql.get_db().cursor()
    #cursor.execute('''CREATE TABLE put_request(VARCHAR CompanyName,VARCHAR Material, VARCHAR DepartureLocation, DATETIME DepartureTime, VARCHAR ArrivalLocation, DATETIME ArrivalTime, VARCHAR Phone);''')
    #cursor.execute('''INSERT INTO put_resuest (CompanyName,Material,DepartureLocation,DepartureTime,ArrivalLocation,ArrivalTime,Phone) VALUES ('CHEP','Palette', 'Aydin', '2023-04-12 08:15:00','Izmir', '2023-04-14 02:00:00', '552-256-8080') ''')
    #rv = cursor.fetchall()
    #create_put_requestdb()
    requests = put_request()
    return str(requests)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 10000, debug=True)

