from flask import Flask
from flask import request
from flask import jsonify
from flask import Response

app = Flask(__name__)
buses = {
    5: {
        'capacity': 100,
        'driver': "Ivan Shumilov"
    },
    6: {
        'capacity': 50,
        'driver': "Nikita Zvezda"
    },
    10: {
        'capacity': 50,
        'driver': "Ivan Ivanov"
    },
    15: {
        'capacity': 50,
        'driver': "Nikolai Ushakov"
    },
    20: {
        'capacity': 50,
        'driver': "Alexander Kireev"
    }
}
start1 = {'isStart': True,
          'routeId': 100,
          'buses': [5, 6, 10],
          'startPoint': 100,
          'stopPoint': 150,
          'passengers': 200
          }
stop1 = {'isStart': False,
         'routeId': 100,
         'buses': [5, 6, 10],
         'startPoint': 100,
         'stopPoint': 150,
         'passengers': 200
         }
start2 = {'isStart': True,
          'routeId': 150,
          'buses': [15, 20],
          'startPoint': 200,
          'stopPoint': 250,
          'passengers': 100
          }
stop2 = {'isStart': False,
         'routeId': 150,
         'buses': [15, 20],
         'startPoint': 200,
         'stopPoint': 250,
         'passengers': 100
         }
exampleTimeDict = {
    45: [start1],
    70: [stop1, start2],
    120: [stop2]
}


def createRoute(elem):
    return { 'startTime': -1,
             'stopTime': -1,
             'buses': elem['buses'],
             'passengerCount': elem['passengers']
             }


def transformAlgorithmData(timeDict, startMinute=0):
    routes = {}
    for key, arr in timeDict.items():
        for elem in arr:
            if elem['isStart'] is True:
                routes[elem['routeId']] = createRoute(elem)
                routes[elem['routeId']]['startTime'] = key
            else:
                routes[elem['routeId']]['stopTime'] = key
    res = {}
    for key, elem in routes.items():
        if elem['stopTime'] > startMinute:
            res[key] = elem
    return res


@app.route('/about')
def about():
    return "About page"


@app.route('/routes/new')
def des():
    routeId = request.args.get('routeId')
    startTime = request.args.get('startTime')
    busNumbers = request.args.get('busNumbers')
    print("/routes/new", routeId, startTime, busNumbers)

    return jsonify(
        username="das",
        email="fsd",
        id="sdfd"
    )


@app.route('/routes/update')
def des2():
    routeId = request.args.get('routeId')
    startTime = request.args.get('startTime')
    print("/routes/update", routeId, startTime)

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
