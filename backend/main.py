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
    return {'startTime': -1,
            'stopTime': -1,
            'buses': elem['buses'],
            'passengerCount': elem['passengers'],
            'routeId': elem['routeId']
            }


def transformAlgorithmData(timeDict):
    routes = {}
    for key, arr in timeDict.items():
        for elem in arr:
            if elem['isStart'] is True:
                routes[elem['routeId']] = createRoute(elem)
                routes[elem['routeId']]['startTime'] = key
            else:
                routes[elem['routeId']]['stopTime'] = key
                routes[elem['routeId']]['id'] = key
    return routes


def transformSchedule(routes, startMinute=0):
    res = {}
    for key, elem in routes.items():
        if elem['stopTime'] > startMinute:
            res[key] = elem
    return res


def transformSchedule(routes, startMinute=0):
    res = {}
    for key, elem in routes.items():
        if elem['stopTime'] > startMinute:
            res[key] = elem
    return res


schedule = transformAlgorithmData(exampleTimeDict)


@app.errorhandler(404)
def handel_404(error):
    return Response(status=404)


@app.errorhandler(400)
def handel_400(error):
    return Response(status=400)


@app.route('/routes/new', methods=['POST'])
def routeNew():
    routeId = int(request.args.get('routeId'))
    startTime = int(request.args.get('startTime'))
    stopTime = int(request.args.get('stopTime'))
    startPoint = int(request.args.get('startPoint'))
    stopPoint = int(request.args.get('stopPoint'))
    passengers = int(request.args.get('passengers'))
    buses = request.args.get('buses')
    buses = [int(val) for val in buses.split(',')]
    schedule[routeId] = {}
    schedule[routeId].update({'routeId': routeId, 'startTime': startTime, 'stopTime': stopTime,
                              'startPoint': startPoint, 'stopPoint': stopPoint, 'passengerCount': passengers,
                              'buses': buses})

    return Response(status=200)


@app.route('/routes/update', methods=['POST'])
def routeUpdate():
    routeId = request.args.get('routeId')
    startTime = request.args.get('startTime')
    print("/routes/update", routeId, startTime)

    return jsonify(
        username="das",
        email="fsd",
        id="sdfd"
    )


@app.route('/routes/deleteBus', methods=['DELETE'])
def routeDeleteBus():
    routeId = request.args.get('routeId')
    startTime = request.args.get('startTime')
    print("/routes/update", routeId, startTime)

    return jsonify(
        username="das",
        email="fsd",
        id="sdfd"
    )


@app.route('/routes/addBus', methods=['UPDATE'])
def routeAddBus():
    routeId = request.args.get('routeId')
    startTime = request.args.get('startTime')
    print("/routes/update", routeId, startTime)

    return jsonify(
        username="das",
        email="fsd",
        id="sdfd"
    )


@app.route('/day', methods=['GET'])
def getDaySchedule():
    global schedule
    return jsonify(
        list(schedule.values())
    )


@app.route('/fromMinute', methods=['GET'])
def getCurrentSchedule():
    global schedule
    startTime = request.args.get('minute')
    schedule = transformSchedule(schedule, startMinute=int(startTime))
    return jsonify(
        list(schedule.values())
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0')
