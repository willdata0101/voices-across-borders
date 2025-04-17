# Voices Across Borders

🎧 **Multilingual Podcast Dubbing + QA Tool using ElevenLabs + Groq/Llama**

This Streamlit-based app takes a Spanish-language podcast or audio clip, generates an English dub using ElevenLabs, and then uses an LLM (Mixtral via Groq API) to perform QA between the original and translated texts.

Built to demonstrate the power of combining LLMs, linguistic QA, and voice technology, this project is ideal for showcasing:
- Language translation and quality validation
- Voice synthesis
- LLM-based reasoning
- Automated testing

---

## 🚀 Features

- 📥 Upload Spanish-language audio files
- 📝 Auto-transcribe (placeholder for Whisper or ElevenLabs integration)
- 🌍 Translate text using Llama 3-8B (via Groq API)
- 🔊 Generate English dub using ElevenLabs (stubbed with placeholder response)
- ✅ Run linguistic and semantic quality checks using LLM
- 🧪 Full test suite with `pytest` and mock Groq API calls

---

## 🧠 Tech Stack

| Tool | Purpose |
|------|---------|
| `Streamlit` | App UI |
| `Groq + Llama 3-8B` | Translation & QA LLM |
| `ElevenLabs API` | Dubbing audio synthesis (stubbed for testing) |
| `pytest` | Automated unit testing |
| `unittest.mock` | Mocking external APIs |

---

## 🧪 Running Tests

```bash
pip install -r requirements.txt
pytest --cov=app --cov-report=term-missing
```

Test coverage includes:
- Translation output
- QA evaluation
- Dubbing endpoint response
- Edge cases (empty input)
- API failure handling

---

## 📂 Project Structure

```bash
├── app.py                   # Main Streamlit app
├── test_app.py              # Unit tests
├── requirements.txt         # Dependencies
├── README.md
└── .env                     # API keys (not tracked)
```

---

## 🌍 Example Use Case

🎙️ Input: Spanish podcast segment
🧠 Output: Translated English text
🔊 Output: English voice dub (via ElevenLabs)
✅ Output: QA assessment from LLM

---

## 🧑‍💻 Author
**William Daugherty**  
AI & NLP Specialist | Spanish-English Linguist | Voice AI Enthusiast  
[LinkedIn](https://linkedin.com/in/williamthetranslator) | [GitHub](https://github.com/willdata0101)

---

## 📩 Want a Demo or Feedback?
Feel free to reach out directly or open an issue. I'd love to improve the project based on real-world feedback from the ElevenLabs team or other AI audio innovators.

