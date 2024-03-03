import streamlit as st
from gpt4all import GPT4All

# Initialize GPT-4 model
gpt4_model = GPT4All(model_name="orca-mini-3b-gguf2-q4_0.gguf")

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
    # You need to implement logic to generate multiple-choice answers based on the question.
    # For simplicity, let's assume some generic answers here.
    answers = ["Option A", "Option B", "Option C", "Option D"]

    # Display the answers
    selected_answer = st.radio("Choose the correct answer:", answers)
    
    if st.button("Check Answer"):
        correct_answer = "Option A"  # Replace with the actual correct answer
        if selected_answer == correct_answer:
            st.success("Correct! 🎉")
        else:
            st.error(f"Wrong! The correct answer is {correct_answer}.")

# Streamlit app
st.title("GPT-4 Quiz App")

# Generate a question and answers
generate_question()
