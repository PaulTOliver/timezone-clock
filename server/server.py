import time

from datetime import datetime
from flask import abort, Flask, jsonify
from flask_cors import CORS
from pytz import common_timezones, timezone


app = Flask(__name__)
CORS(app)


@app.route('/zones/', methods=['GET'])
def zones():
    """ Return a list of common timezones """
    # time.sleep(5) # Simulate slow connection
    return jsonify(common_timezones)


@app.route('/time-at/<path:zone>', methods=['GET'])
def time_at(zone):
    """ Return current time at given timezone """
    # time.sleep(5) # Simulate slow connection

    if zone not in common_timezones:
        abort(404)

    tzobj = timezone(zone)

    return jsonify({
        'zone': tzobj.zone,
        'time': datetime.now(tzobj).strftime('%a %d %b %Y %H:%M:%S'),
    })
