from flask import Flask, render_template, request
import datetime
from waitress import serve

app = Flask(__name__)

records = []

# Homepage - Liste aller Notizen
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.methods == 'POST':
        records.append(request.args.to_dict())
    else:

        timestamps = [ entry['timestamp'] for enty in records]

        if len(records <= 5):
            return render_template("no_records.html")
        
        elif datetime.datetime.now() - max(timestamps) < 1000:
            records = []
            return render_template("no_records.html")
        else:
            return render_template('base.html', notes=notes)


if __name__ == '__main__':
    init_db()
    serve(app, host='127.0.0.1', port=8080, url_prefix='/notes', url_scheme='https')
