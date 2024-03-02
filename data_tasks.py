import pandas as pd
from gpt4all import GPT4All

def start_model():
    model = GPT4All(model_name="nous-hermes-llama2-13b.Q4_0.gguf")
    return model


def model_question(string):
    model = start_model()
    question = model.generate(f"Make a question out of this phrase: {string}")
    return question


def load_data(filename='question_data.csv'):
    pd.options.display.max_rows = 9999
    pd.options.display.max_columns = 9999
    file = pd.read_csv(filename)
    return file

def find_question_question(desired_question):
    file = load_data()
    found_question = False
    question_row = 0
    for question in file['question']:
        if question == desired_question:
            found_question = True
        else:
            question_row += 1
    if found_question == False:
        return 'ERR'
    else:
        return file[question_row]


def fetch_question_by_number(num):
    file = load_data()
    item = file.iloc[num]
    return item

