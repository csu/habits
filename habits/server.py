from flask import Flask, render_template
from api import api_blueprint

app = Flask(__name__)
app.register_blueprint(api_blueprint, url_prefix='/api')

@app.route('/')
def index():
    return app.send_static_file('app.html')

def production():
    app.run(debug=False)

if __name__ == '__main__':
    app.run(debug=True)