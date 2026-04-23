from flask import Flask, render_template, request
import json
import time
from datetime import datetime
from waitress import serve
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

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


    # show only if there is a record
    if len(records) < 1:
        return render_template("no_records.html")
    else:
        latest = int(records[-1]['timestamp'])
        diff = now - latest
    
    
    # delete all records if the latest record is older than 1 min
    if diff > 60000:
        return render_template("no_records.html")
    else:
        curr_rec = records[-1]
        curr_rec['last_record'] = datetime.fromtimestamp(curr_rec['timestamp'])
        return render_template('base.html', loc=curr_rec)


if __name__ == '__main__':
    serve(app, host='127.0.0.1', port=8082, url_scheme='https')
