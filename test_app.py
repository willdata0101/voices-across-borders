import pytest
import voices_across_borders as app
from unittest.mock import patch

sample_transcript = "Cuando tenía seis años vi una vez una magnífica lámina..."
sample_translation = "When I was six years old, I once saw a magnificent illustration..."
sample_qa_result = "Translation is accurate. Fluency: 9/10, Accuracy: 10/10"

@patch("voices_across_borders.requests.post")
def test_translate_transcript(mock_post):
    # Mock response from Groq
    mock_post.return_value.json.return_value = {
        "choices": [
            {"message": {"content": sample_translation}}
        ]
    }

    result = app.translate_transcript(sample_transcript)
    assert sample_translation in result

@patch("voices_across_borders.requests.post")
def test_run_quality_check(mock_post):
    # Mock QA check result
    mock_post.return_value.json.return_value = {
        "choices": [
            {"message": {"content": sample_qa_result}}
        ]
    }

    result = app.run_quality_check(sample_transcript, sample_translation)
    assert "Fluency" in result and "Accuracy" in result

def test_transcribe_audio():
    dummy_file = "fake_audio.mp3"
    result = app.transcribe_audio(dummy_file)
    assert result == "[Spanish transcript]"

def test_generate_dub():
    result = app.generate_dub("test text")
    assert result = "[Audio file URL or playback]"

    