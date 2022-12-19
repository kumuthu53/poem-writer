from flask import Flask, request
from openai_write import get_poem

app = Flask(__name__)


@app.get("/write_poem")
def write_poem():

    title = request.args['title']

    result = {
        "poem": get_poem(title)
    }

    return result["poem"]


