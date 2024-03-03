import streamlit as st
import whisper
from gpt4all import GPT4All
import os
import time

# Initialize Whisper model
whisper_model = whisper.load_model("base")

# Initialize GPT-4 model
gpt4_model = GPT4All(model_name="orca-mini-3b-gguf2-q4_0.gguf")

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

    # Initialize variables for tracking time intervals
    start_time = time.time()
    question_interval = 180  # 3 minutes interval

    # Streamlit loop
    while True:
        # csheck if it's time to generate a question
        elapsed_time = time.time() - start_time
        if elapsed_time >= question_interval:
            try:
                # transcribe the audio for the last 3 minutes
                transcription = whisper_model.transcribe(temp_audio_path)
                
                # generate a question based on the transcription
                generated_question = gpt4_model.generate("Generate a trivia question about: " + transcription["text"])

                # display the question
                st.write("Generated Question:", generated_question)

                # reset the timer for the next question
                start_time = time.time()
            except Exception as e:
                st.error(f"Error during transcription or question generation: {str(e)}")

    os.remove(temp_audio_path)
else:
    st.info("Please upload an audio file.")
