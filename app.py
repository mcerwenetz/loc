from flask import Flask, render_template, request
import json
import time
from waitress import serve

app = Flask(__name__)


records = []
# Homepage - Liste aller Notizen
@app.route('/', methods=['GET'])
def index():
    global records
    now = int(time.time() * 1000 )

    if request.args:
        entry = request.args.to_dict()
        records.append(entry)
        # dont store more than 100 records
        if len(records) > 99:
            records.remove(records[0])
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


    # show only for consecutive records, not just the first one
    if len(records) <= 5:
        return render_template("no_records.html")
    else:
        latest = int(records[-1]['timestamp'])
        diff = now - latest
    
    
    # delete all records if the latest record is older than 1 min
    if diff > 60000:
        records = []
        return render_template("no_records.html")
    else:
        return render_template('base.html', loc=records[-1])


if __name__ == '__main__':
    serve(app, host='127.0.0.1', port=8082, url_scheme='https')
