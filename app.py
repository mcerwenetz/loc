from flask import Flask, render_template, request
import datetime
import json
#from waitress import serve

app = Flask(__name__)


records = []
# Homepage - Liste aller Notizen
@app.route('/', methods=['GET', 'POST'])
def index():
    global records

    if request.method == 'POST':
        entry = request.args.to_dict()
        records.append(entry)
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
    elif request.method == 'GET':

        if len(records) <= 0:
            return render_template("no_records.html")
        
        #elif str(datetime.datetime.now()) - records[-1]['timestamp'] < 1000:
        #    records = []
        #    return render_template("no_records.html")
        else:
            return render_template('base.html', loc=records[-1])


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
