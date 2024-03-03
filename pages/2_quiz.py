import streamlit as st
from gpt4all import GPT4All

# Initialize GPT-4 model
gpt4_model = GPT4All(model_name="gpt4all-falcon-newbpe-q4_0.gguf")

def generate_question():
    prompt = "Generate a trivia question about:"
    user_input = st.text_input("Enter a topic:", "history")  # Default topic is history

    if st.button("Generate Question"):
        try:
            generated_question = gpt4_model.generate(prompt + f" {user_input}")
            st.write("Generated Question:", generated_question)
            generate_answers(generated_question)
        except Exception as e:
            st.error(f"Error during question generation: {str(e)}")

def generate_answers(question):
    # Generate correct answer
    q_prompt = "give me the correct answer to this question" + question
    correct_answer = gpt4_model.generate(q_prompt)
    # Generate three wrong answers
    w_prompt = "give me three wrong answers separated by commas" + question
    wrong_answers = gpt4_model.generate(w_prompt)

    # Combine correct and wrong answers into a list
    answers = [correct_answer] + wrong_answers.split(", ")

    # Display the answers
    selected_answer = st.radio("Choose the correct answer:", answers)

    if st.button("Check Answer"):
        if selected_answer == correct_answer:
            st.success("Correct! 🎉")
        else:
            st.error(f"Wrong! The correct answer is {correct_answer}.")

# Streamlit app
st.title("Quiz App")

# Generate a question and answers
generate_question()
