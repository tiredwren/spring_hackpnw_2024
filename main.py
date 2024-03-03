import streamlit as st
import whisper
import os

st.title("Whisper App")

# Upload audio file with streamlit
audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3", "m4a"])

# Check if an audio file is uploaded
if audio_file is not None:
    st.audio(audio_file, format="audio/*")

    # Save the uploaded file to a temporary location
    temp_audio_path = "temp_audio_file.wav"
    with open(temp_audio_path, "wb") as temp_audio_file:
        temp_audio_file.write(audio_file.read())

    # Load the whisper model
    model = whisper.load_model("base")
    st.text("Whisper Model Loaded")

    if st.sidebar.button("Transcribe Audio"):
        st.sidebar.success("Transcribing Audio")
        try:
            # Transcribe the audio
            transcription = model.transcribe(temp_audio_path)
            st.sidebar.success("Transcription Complete")
            st.markdown(transcription["text"])
        except Exception as e:
            st.sidebar.error(f"Error during transcription: {str(e)}")

    # Remove the temporary audio file after processing
    os.remove(temp_audio_path)
else:
    st.info("Please upload an audio file.")
