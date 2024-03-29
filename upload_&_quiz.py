import streamlit as st
import whisper
from gpt4all import GPT4All
from txtai.pipeline import Summary
import os

# Initialize Whisper model
whisper_model = whisper.load_model("base")


# Initialize GPT-4 model
gpt4_model = GPT4All(model_name="gpt4all-falcon-newbpe-q4_0.gguf")

# Function to generate a question
def generate_question(transcription):
    prompt = "Generate a trivia question About the information contained in the transcription: \n "
    try:
        # Get a random chunk of the transcription
        # start_index = random.randrange( 0, len(transcription), -200)  # Adjust 200 based on desired chunk size
        # print(start_index)
        # random_chunk = transcription[start_index:start_index + 200]  # Adjust 200 based on desired chunk size
        # print(random_chunk)
        data = transcription['text']
        data = data[0:80]
        print(data)
        generated_question = gpt4_model.generate(prompt + data)
        st.write(generated_question)
        generate_answers(generated_question)
    except Exception as e:
        st.error(f"error during question generation: {str(e)}")
        print(e)

# Function to generate answers
def generate_answers(question):
    # Generate correct answer
    correct_answer = gpt4_model.generate("give me the correct answer to this question: " + question)

    # Generate three wrong answers
    wrong_answers = gpt4_model.generate("give me three wrong answers to this question separated by commas: " + question)

    # Combine correct and wrong answers into a list
    answers = [correct_answer] + wrong_answers.split(", ")

    # Display the answers
    selected_answer = st.radio("Select an answer:", answers)

    if st.button("check Answer"):
        if selected_answer == correct_answer:
            st.success("Correct! 🎉")
        else:
            st.error(f"Wrong! The correct answer is {correct_answer}.")
            #explanation = gpt4_model.generate("why is " + correct_answer + " the correct answer to " + question + "?")
            #st.error(explanation)

# Function to summarize text
def text_summary(text, maxlength=None):
    # Create summary instance
    summary = Summary()
    result = summary(text)
    return result

# Streamlit app
st.title("Audio Quiz App")

# Upload audio file
audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3", "m4a"])

# Check if an audio file is uploaded
if audio_file is not None:
    st.audio(audio_file, format="audio/*")

    temp_audio_path = "temp_audio_file.wav"
    with open(temp_audio_path, "wb") as temp_audio_file:
        temp_audio_file.write(audio_file.read())

    st.text("Audio file uploaded successfully.")
    os.remove(temp_audio_path)
else:
    st.info("Please upload an audio file.")
    
st.radio("what is the cosine of 2pi/3",["32 inches", "24 inches", "50 inches", "120 inches"])
