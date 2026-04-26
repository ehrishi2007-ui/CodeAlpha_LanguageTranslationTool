import streamlit as st
import requests
from gtts import gTTS
import io
import time

# --- Page Config ---
st.set_page_config(page_title="Language Translator", page_icon="🌐", layout="centered")

# --- Session State for rate limiting ---
if "last_translation_time" not in st.session_state:
    st.session_state.last_translation_time = 0

# --- Language Options ---
LANGUAGES = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Chinese": "zh",
    "Arabic": "ar",
    "Portuguese": "pt",
    "Russian": "ru",
    "Korean": "ko",
    "Italian": "it",
    "Telugu": "te",
    "Tamil": "ta",
    "Bengali": "bn",
    "Dutch": "nl",
    "Polish": "pl",
    "Swedish": "sv",
    "Turkish": "tr",
    "Ukrainian": "uk",
}

lang_names = list(LANGUAGES.keys())

# --- UI ---
st.title("🌐 Language Translator")
st.caption("Powered by MyMemory Translation API")
st.warning("⚠️ Do not translate sensitive or personal information.")

# --- Language Selection ---
col1, col2 = st.columns(2)
with col1:
    src_lang_name = st.selectbox("Source Language", lang_names, index=0)
with col2:
    tgt_lang_name = st.selectbox("Target Language", lang_names, index=1)

src_lang = LANGUAGES[src_lang_name]
tgt_lang = LANGUAGES[tgt_lang_name]

# --- Text Input ---
input_text = st.text_area(
    "Enter text to translate",
    placeholder="Type or paste your text here...",
    height=150,
    max_chars=500,
)
st.caption(f"{len(input_text)} / 500 characters")


# --- Translate Function ---
def translate_text(text, src, tgt):
    url = "https://api.mymemory.translated.net/get"
    params = {"q": text, "langpair": f"{src}|{tgt}"}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    if data["responseStatus"] == 200:
        return data["responseData"]["translatedText"]
    else:
        raise Exception(data.get("responseDetails", "Translation failed"))


# --- Translate Button ---
if st.button("🔄 Translate", use_container_width=True, type="primary"):
    # -- Validation --
    if not input_text.strip():
        st.warning("Please enter some text to translate.")
        st.stop()

    if src_lang == tgt_lang:
        st.warning("Source and target languages are the same.")
        st.stop()

    # -- Input sanitization --
    forbidden_chars = ["<", ">", "{", "}", "\\"]
    if any(char in input_text for char in forbidden_chars):
        st.warning(
            "Please enter plain text only. Special characters like < > { } are not allowed."
        )
        st.stop()

    # -- Rate limiting --
    current_time = time.time()
    time_since_last = current_time - st.session_state.last_translation_time
    if time_since_last < 3:
        wait = round(3 - time_since_last)
        st.warning(f"Please wait {wait} second(s) before translating again.")
        st.stop()

    # -- Translation --
    with st.spinner("Translating..."):
        try:
            translated = translate_text(input_text, src_lang, tgt_lang)
            st.session_state.last_translation_time = time.time()

            # -- Display result --
            st.success("Translation complete!")
            st.subheader("Translated Text")
            st.code(translated, language=None)

            # -- Download button --
            st.download_button(
                label="⬇️ Download Translation",
                data=translated,
                file_name="translation.txt",
                mime="text/plain",
            )

            # -- Text to Speech --
            st.subheader("🔊 Listen to Translation")
            try:
                tts = gTTS(text=translated, lang=tgt_lang)
                audio_buffer = io.BytesIO()
                tts.write_to_fp(audio_buffer)
                audio_buffer.seek(0)
                st.audio(audio_buffer, format="audio/mp3")
            except Exception:
                st.caption("Audio not available for this language.")

        except requests.exceptions.Timeout:
            st.error("Request timed out. Check your internet connection.")
        except requests.exceptions.HTTPError as e:
            st.error(f"API error: {e}")
        except Exception as e:
            st.error(f"Translation failed: {e}")
