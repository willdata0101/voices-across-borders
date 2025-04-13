# app.py - ElevenLabs Podcast Dubbing Project
"""
Voices Across Borders - A Multilingual Podcast Audio Dubbing Tool

This Streamlit-based app takes a Spanish podcast/audio file, dubs it in English via ElevenLabs API,
and runs a linguistic and semantic QA using LLMs (in this case, Llama-3-8-B via Groq) to evaluate
translation accuracy and tone. Ideal for showcasing real-world multilingual API deployment.
"""

import streamlit as st
from elevenlabs.client import ElevenLabs
from groq import Groq
from pydub import AudioSegment
from dotenv import load_dotenv
import os
import io

load_dotenv()

# ======CONFIGURATION========
GROQ_API_KEY = os.getenv("Groq")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
ELEVENLABS_API_KEY = os.getenv("ElevenLabs")
# Initialize ElevenLabs client
client_el = ElevenLabs(api_key=ELEVENLABS_API_KEY)
# Initialize Groq client
client_gr = Groq(api_key=GROQ_API_KEY)

# ======APP LAYOUT========
def transcribe_audio(audio_file):
    st.info("Transcribing audio...")
    # Transcribe audio using ElevenLabs API
    audio_data = AudioSegment.from_file(audio_file)
    audio_data = audio_data.set_frame_rate(44100).set_channels(1).set_sample_width(2) # Convert to 2 bytes / 16-bit .wav
    audio_buffer = io.BytesIO()
    audio_data.export(audio_buffer, format="wav")
    audio_buffer.seek(0)
    st.success("Audio converted successfully!")
    with st.spinner("✍ Transcribing audio... "):
        transcript = client_el.speech_to_text.convert(
            file = audio_buffer,
            model_id = "scribe_v1"
        )
    st.markdown("📜 Transcription: ")
    st.write(transcript.text)
    return transcript.text

def translate_transcript(transcript):
    st.info("Translating transcript using Llama-3-8B...")
    completion = client_gr.chat.completions.create(
        model = "llama3-8b-8192",
        messages = [
            {
                "role": "user",
                "content": f"Translate the following Spanish text to professional English:\n\n{transcript}"
            }
        ]
    )

    response = completion.choices[0].message.content
    return response

def generate_dub(translated_text):
    audio_data = client_el.text_to_speech.convert(
        text=translated_text,
        voice_id="EXAVITQu4vr4xnSDxMaL",
        model_id="eleven_multilingual_v2"
    )
    st.write(audio_data)

def run_quality_check(spanish, english):
    st.write(spanish)
    st.write(english)
    qa_prompt = f"""
    Compare the following Spanish source with its English translation.
    - Identify any mistranslations or tone shifts.
    - Rate fluency and accuracy from 1 to 10.
    
    Spanish: {spanish}
    English: {english}

    """

    completion = client_gr.chat.completions.create(
        model = "llama3-8b-8192",
        messages = [
            {
                "role": "user",
                "content": qa_prompt
            }
        ]
    )

    response = completion.choices[0].message.content
    return response

# ======APP LOGIC========
st.title("Voices Across Borders - Multilingual Podcast Dubbing Tool")
st.write("Upload a Spanish podcast audio file for dubbing in English.")
uploaded_file = st.file_uploader("Choose a Spanish audio file", type=["mp3", "wav"])

if uploaded_file:
    transcript = transcribe_audio(uploaded_file)
    st.subheader("Transcription")

    translated = translate_transcript(transcript)
    st.subheader("Translated Text")

    with st.spinner("💿 Generating dub..."):
        dubbed_audio = generate_dub(translated)
        if dubbed_audio:
            st.success("Dubbing process completed successfully!")
            dubbed_audio.seek(0)
            st.audio(dubbed_audio, format='audio/wav')

    with st.spinner("Running quality check... "):
        qa_result = run_quality_check(transcript, translated)
        if qa_result:
            st.success("Quality check complete!")
    st.markdown("### Quality Check Result")
    st.write(qa_result)