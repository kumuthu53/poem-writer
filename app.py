from flask import Flask, request
from openai_write import get_poem

# Create an instance of Flask.
app = Flask(__name__)


# Define the function with the path and method to call it.
@app.get("/write_poem")
def write_poem():

    # Obtains the title from the request parameters.
    title = request.args['title']

    # Writes the poem by calling the get_poem() method.
    # It would make more sense to wrap the poem in a JSON if this endpoint is consumed by an app.
    result = get_poem(title)

    return result
