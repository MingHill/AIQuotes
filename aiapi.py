import openai
import config

api_key = config.DevelopmentConfig.OPENAI_KEY
openai.api_key = api_key

def generateChatResponse(prompt): 
    messages = []

    question = {}
    question['role'] = 'user'
    question['content'] =  f"""You will given some context as well as some emotions from a user from a body of text delimited by triple backticks. 
    Based off of the information given, supply a quote or proverb that will make them feel better. First, give the quote by itself and who said it by in the format "a;lsdkfjasldaaldkafj.
    by xxxvvv". Then explain how this quote is relevent to their situation. ```{prompt}```.""" 
    messages.append(question)

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages = messages, temperature = 0)
    try: 
        answer = response['choices'][0]['message']['content'].replace('\n', '<br>')
    except:
        answer = 'Oops you beat the AI, try a different questions, if the problem persists, come back later.'

    return answer