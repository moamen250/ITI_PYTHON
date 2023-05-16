import openai
openai.api_key = "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" # replace with your API key

def ask_questions(prompts):
    responses = []
    for prompt in prompts:
        response = openai.Completion.create(
            engine="text-davinci-002", # specify which GPT model to use
            prompt=prompt,
            max_tokens=2048, # maximum length of the generated response
            n=1, # how many responses to generate
            stop=None, # stop generating responses when one of these strings is generated
            temperature=0.7, # controls the randomness of the generated response
        )
        answer = response.choices[0].text.strip()
        responses.append(answer)
    return responses

prompts = ["What is the meaning of life?", "How do I bake a cake?", "What is the capital of France?"]
answers = ask_questions(prompts)
for answer in answers:
   print(answer)






