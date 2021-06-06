
from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    #count = redis.incr('hits')
    return 'Hello World k8s parcial distribuidos'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8082, debug=True)