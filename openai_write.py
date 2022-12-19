import openai


def get_poem(title):

    # Reads and sets the api key the first time this function is evoked.
    if not hasattr(get_poem, 'api_key'):
        api_key_file = open("api_key.txt", "r")
        get_poem.api_key = api_key_file.read()
        api_key_file.close()

        openai.api_key = get_poem.api_key

    # Builds prompt.
    prompt = f"Write a poem with the title '{title}'"

    # Generates the response from GPT-3.
    response = openai.Completion.create(model="text-davinci-003",
                                        prompt=prompt,
                                        temperature=0.7,
                                        max_tokens=500)

    # Extracts the poem.
    poem = response["choices"][0]["text"]

    return poem


