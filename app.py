
from flask import Flask
from flask.wrappers import Response
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis.default.svc.cluster.local', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return 'Hello World k8s parcial distribuidos v2'+str(count)
@app.route('/health')
def health():
    respuesta = app.response_class(
        status=200
    )
    return respuesta

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8082, debug=True)