from flask import Flask
from flask import json
import logging

from werkzeug.sansio.response import Response

app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info('Main request sucessfull')
    return "Hello World!"

@app.route("/status")
def healthcheck():
    response = app.response_class(
        response=json.dumps({"result":"OK - health"}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('Status request sucessfull')
    return response
    
@app.route("/metrics")
def metrics():
    response = app.response_class(
        response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UsersCountActive":23}}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('Metrics request sucessfull')
    return response

if __name__ == "__main__":
    logging.basicConfig(filename='app.log',format='%(asctime)s %(message)s', level=logging.DEBUG)
    app.run(host='0.0.0.0')