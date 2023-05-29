from flask import Flask, request, Response
from utils import handle_request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()

        handle_request(msg)


        return Response('ok', status=200)
    else:
        print("not post")
        return "<h1>Welcome!</h1>"


if __name__ == '__main__':
    app.run(debug=True, port=5002)