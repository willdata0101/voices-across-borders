import app as app
from unittest.mock import patch, MagicMock

@patch("app.client_gr.chat.completions.create")
def test_translate_transcript(mock_create):
    # Setup fake response JSON
    mock_create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content="This is the translated text."))]
    )
    # Input for the test
    spanish_input = "Hola, ¿cómo estás?"

    # Call the function under test
    result = app.translate_transcript(spanish_input)

    # Assertions
    assert result == "This is the translated text."
    mock_create.assert_called_once()

@patch("app.client_gr.chat.completions.create")
def test_run_quality_check(mock_create):
    # Mock QA check result
    mock_create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content="Fluency: 9/10, Accuracy: 10/10"))]
    )
    spanish_input = "Hola, ¿cómo estás?"
    english_input = "Hello, how are you?"

    # Call the function under test
    result = app.run_quality_check(spanish_input, english_input)
    # Assertions
    assert result == "Fluency: 9/10, Accuracy: 10/10"
    mock_create.assert_called_once()

@patch("app.client_el.text_to_speech.convert")
def test_generate_dub(mock_create):
    # Simulate the ElevenLabs-like response structure
    mock_create.return_value = MagicMock(
        choices=[MagicMock(
            message=MagicMock(
                content="This is the generated audio stream."
            )
        )])

    input_text = "Hello there!"
    result = app.generate_dub(input_text)

    assert result == "This is the generated audio stream."
    mock_create.assert_called_once()

# ----------------------------
# Edge cases / negative tests
# ----------------------------

@patch("app.client_gr.chat.completions.create")
def test_translate_transcript_empty_input(mock_create):
    # Setup fake response JSON
    mock_create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content=""))]
    )
    # Input for the test
    spanish_input = ""

    # Call the function under test
    result = app.translate_transcript(spanish_input)

    # Assertions
    assert result == ""
    mock_create.assert_called_once()

@patch("app.client_gr.chat.completions.create")
def test_run_quality_check_incomplete(mock_create):
    mock_create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content=""))]
    )
    spanish_input = "Hola, ¿cómo estás?"
    english_input = ""

    # Call the function under test
    result = app.run_quality_check(spanish_input, english_input)
    # Assertions
    assert result == ""
    mock_create.assert_called_once()

@patch("app.client_el.text_to_speech.convert")
def test_generate_dub_empty_text(mock_create):
    mock_create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content=""))])
    
    result = app.generate_dub("")
    assert result == ""

# ----------------------------
# Exception Handling Tests
# ----------------------------

@patch("app.client_gr.chat.completions.create")
def test_translate_transcript_exception(mock_create):
    mock_create.side_effect = Exception("API error")
    spanish_input = "Hola, ¿cómo estás?"

    # Call the function under test
    with patch("builtins.print") as mock_print:
        result = app.translate_transcript(spanish_input)
        assert result is None
        mock_print.assert_called_once_with("API error")