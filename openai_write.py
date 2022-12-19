import openai


def get_poem(title):

    if not hasattr(get_poem, 'api_key'):
        api_key_file = open("api_key.txt", "r")
        get_poem.api_key = api_key_file.read()
        api_key_file.close()

        openai.api_key = get_poem.api_key

    prompt = f"Write a poem with the title '{title}'"

    response = openai.Completion.create(model="text-davinci-003",
                                        prompt=prompt,
                                        temperature=0.7,
                                        max_tokens=500)

    poem = response["choices"][0]["text"]

    return poem


