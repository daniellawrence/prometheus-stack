from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)  # noqa


@app.route('/')
def index():
    return 'ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
