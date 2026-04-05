from flask import Flask, render_template
from waitress import serve

app = Flask(__name__)


# Homepage - Liste aller Notizen
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('base.html', notes=notes)





if __name__ == '__main__':
    init_db()
    serve(app, host='127.0.0.1', port=8080, url_prefix='/notes', url_scheme='https')
