from flask import Flask
import logging
from flask import jsonify

app=Flask(__name__)

logging.basicConfig(level=logging.INFO, filename='log/flask_server_log.txt', format="%(asctime)s - %(levelname)s - %(message)s")

@app.route("/")
def index():
	logging.info('Called Hello World')
	return "<h1>Hello Earth!</h1>"

@app.route("/home")
def return_log():
	file = open('log/flask_server_log.txt','r')
	queue = []
	Dict = {}
	for each in file:
		if len(queue) == 10:
			queue.pop(0)
			queue.append(each)
		else:
			queue.append(each)
	count=1
	for i in range(19,2):
		queue.insert(i,count)
		count = count + 1
	res_dct = {queue[i]: queue[i + 1] for i in range(0, len(queue), 2)}
	
	return jsonify(res_dct)

if __name__=="__main__":
	app.run()