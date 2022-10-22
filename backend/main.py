from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)
		
@app.route('/about')
def about():
    return "About page"

@app.route('/trips/new')
def des():
	tripId = request.args.get('tripId')
	startTime = request.args.get('startTime')
	busNumbers = request.args.get('busNumbers')
	print("/trips/new",tripId,startTime,busNumbers)

	return jsonify(
		username="das",
		email="fsd",
		id="sdfd"
	)

@app.route('/trips/update')
def des2():
	tripId = request.args.get('tripId')
	startTime = request.args.get('startTime')
	print("/trips/update",tripId,startTime)

	return jsonify(
		username="das",
		email="fsd",
		id="sdfd"
	)

@app.route('/trips/day')
def des3():

	return jsonify(
		username="das",
		email="fsd",
		id="sdfd"
	)



if __name__ == "__main__":
    app.run()