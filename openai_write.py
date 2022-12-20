import openai
import json


def get_poem(title, logger):

    # Reads and sets the api key the first time this function is evoked.
    if not hasattr(get_poem, 'api_key'):
        api_key_file = open("api_key.txt", "r")
        get_poem.api_key = api_key_file.read()
        api_key_file.close()

        openai.api_key = get_poem.api_key

    # Builds prompt.
    prompt = f"Write a poem with the title '{title}'"

    # Generates the response from GPT-3.
    try:
        response = openai.Completion.create(model="text-davinci-003",
                                            prompt=prompt,
                                            temperature=0.7,
                                            max_tokens=500)

        logger.info("Response received from OpenAI")
        logger.debug("Response: " + json.dumps(response, indent=4))
    except Exception as e:
        logger.error("Exception during request to OpenAI.")
        raise e

    # Extracts the poem.
    try:
        poem = response["choices"][0]["text"]
    except KeyError as e:
        logger.error("Response from GPT-3 has an unexpected format")
        raise e

    # Remove preceding and trailing whitespace.
    poem = poem.strip()

    # Checks if poem is empty.
    if len(poem) == 0:
        logger.error("Poem generated is empty")
        raise Exception("Poem generated is empty")

    return poem


