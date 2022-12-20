from flask import Flask, request
from openai_write import get_poem
import logging

# Create an instance of Flask.
app = Flask("poem-writer")

# Setup logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
logger.addHandler(handler)


# Define the function with the path and method to call it.
@app.get("/write_poem")
def write_poem():

    # Initialize response.
    response = {
        "status": None,
        "message": None,
        "poem": None
    }

    # Obtains the title from the request parameters.
    try:
        title = request.args['title']
        logger.info(f"Title received is '{title}'")
    except KeyError as e:

        logger.error("The parameter 'title' is missing in the request.")

        response["status"] = "error"
        response["message"] = "The parameter 'title' is missing in the request."

        return response

    # Writes the poem by calling the get_poem() method.
    try:
        poem = get_poem(title, logger)
    except Exception as e:
        logger.error("Error during generating poem.")

        response["status"] = "error"
        response["message"] = "Error during generating poem."

        return response

    # Build response.
    response["status"] = "success"
    response["message"] = "Poem has been successfully generated"
    response["poem"] = poem

    return response
