import json
import sys
import chromadb
import replicate
from chromadb import Documents


# Use bge-large-en-v1.5 on Replicate to generate embeddings.
class EmbeddingFunction:
    def __init__(self):
        pass

    def __call__(self, input):
        texts = json.loads(input["texts"])
        return replicate.run(
            "nateraw/bge-large-en-v1.5:9cf9f015a9cb9c61d1a2610659cdac4a4ca222f2d3707a68517b18c198a9add1",
            input={"texts": json.dumps(texts)},
        )


# Instantiate the embedding function
generate_embeddings = EmbeddingFunction()

# Instantiate the chromadb client, with embedding function
client = chromadb.PersistentClient(path="./")
collection = client.get_or_create_collection(
    name=f"Students", embedding_function=generate_embeddings
)

# Accept a user prompt from the first command line argument.
user_prompt = "What is the student's name?"

# Query Chromadb for the 10 most similar titles to the user prompt.
results = collection.query(
    query_texts=[user_prompt],
    n_results=10,
)

# Concatenate the results into a single string, which we will shove into the prompt.
successful_titles = '\n'.join(results['documents'][0])

# LLM Prompt template.
# NOTE: The [INST] and [/INST] tags are required for mistral-7b-instruct to leverage instruction fine-tuning.
PROMPT_TEMPLATE = f'''[INST] You are an expert in all things. You will be given a USER_PROMPT. You will respond with 
the correct answer to the USER_PROMPT.

USER_PROMPT: {user_prompt}

[/INST]
'''

# Prompt the mistral-7b-instruct LLM
mistral_response = replicate.run(
    "a16z-infra/mistral-7b-instruct-v0.1:83b6a56e7c828e667f21fd596c338fd4f0039b46bcfa18d973e8e70e455fda70",
    input={
        "prompt": PROMPT_TEMPLATE,
        "temperature": 0.75,
        'max_new_tokens': 2048,
    },
)

# Concatenate the response into a single string.
suggestions = ''.join([str(s) for s in mistral_response])

# Print the suggestions.
print(suggestions)

print('====')

print('PROMPT_TEMPLATE', PROMPT_TEMPLATE)
