# 🌐 Language Translator

A simple and clean language translation web app built with Python and Streamlit, powered by the MyMemory Translation API.

## Features

- Translate text between 20+ languages
- Text-to-speech playback of translated text
- Download translation as a `.txt` file
- Built-in copy button on translated output
- Input sanitization and rate limiting for security
- Clean and minimal UI powered by Streamlit

## Languages Supported

English, Hindi, French, Spanish, German, Japanese, Chinese, Arabic, Portuguese, Russian, Korean, Italian, Telugu, Tamil, Bengali, Dutch, Polish, Swedish, Turkish, Ukrainian

## Project Structure

```
language-translator/
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
├── .gitignore           # Files excluded from Git
└── README.md            # Project documentation
```

## Prerequisites

- Python 3.8 or above
- pip
- VS Code (recommended)
- Internet connection (for translation API and text-to-speech)

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/language-translator.git
cd language-translator
```

### 2. Create and activate a virtual environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

## How to Use

1. Select the **source language** (language you are translating from)
2. Select the **target language** (language you want to translate to)
3. Type or paste your text in the input box
4. Click the **Translate** button
5. View the translated text — use the copy icon to copy it
6. Optionally download the translation or listen to it using the audio player

## Dependencies

| Package | Purpose |
|---|---|
| `streamlit` | Web UI framework |
| `requests` | Calling the MyMemory API |
| `gtts` | Text-to-speech audio generation |

Install all at once:
```bash
pip install streamlit requests gtts
```

## API Used

This app uses the **MyMemory Translation API** — a free, no-key-required translation service.

- API endpoint: `https://api.mymemory.translated.net/get`
- Free limit: ~1000 words/day per IP address
- No API key or account needed
- Docs: [mymemory.translated.net](https://mymemory.translated.net)

> ⚠️ Text entered is sent to MyMemory's servers for translation. Do not translate sensitive or personal information.

## Security Features

- **Input sanitization** — blocks special characters like `< > { } \`
- **Rate limiting** — enforces a 3-second cooldown between requests
- **No API keys** — no credentials stored or required
- **Error handling** — clear messages for timeouts, API failures, and invalid input

## Deployment

You can deploy this app for free on **Streamlit Community Cloud**:

1. Push your project to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Click **Deploy**

Your app will be live at a public URL within minutes.

## Known Limitations

- MyMemory free tier allows approximately 1000 words/day per IP
- Text-to-speech may not be available for all languages
- Translation quality depends on the MyMemory API

## License

This project was built as part of a student internship task at [CodeAlpha](https://www.codealpha.tech).
