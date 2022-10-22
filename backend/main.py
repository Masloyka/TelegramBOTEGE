from flask import Flask
from flask import request
from flask import jsonify
from flask import Response

app = Flask(__name__)
		
@app.route('/about')
def about():
    return "About page"

@app.route('/routes/new')
def des():
	routeId = request.args.get('routeId')
	startTime = request.args.get('startTime')
	busNumbers = request.args.get('busNumbers')
	print("/routes/new",routeId,startTime,busNumbers)

	return jsonify(
		username="das",
		email="fsd",
		id="sdfd"
	)

@app.route('/routes/update')
def des2():
	routeId = request.args.get('routeId')
	startTime = request.args.get('startTime')
	print("/routes/update",routeId,startTime)

	return jsonify(
		username="das",
		email="fsd",
		id="sdfd"
	)

@app.route('/day')
def des3():
	return Response(status=400, mimetype='application/json')



if __name__ == "__main__":
    app.run(host='0.0.0.0')