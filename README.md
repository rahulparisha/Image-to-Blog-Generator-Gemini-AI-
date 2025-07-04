# Image-to-Blog-Generator-Gemini-AI-
This is an AI-powered blog generator application that creates rich, descriptive blog content from an input image. Built with Streamlit and Google Gemini AI LLMs, this app takes an uploaded image (e.g., a person, object, scene) and generates a blog-style narrative or description using advanced generative AI capabilities.

The app uses google-generativeai for interacting with Gemini LLMs and python-dotenv to manage API keys securely.

# Features
✅ Upload any image — Person, object, scenery, or item
✅ AI-powered blog generation — Generates human-like blog content describing the image
✅ Clean Streamlit UI — Simple and intuitive for users
✅ Lightweight and extendable — Easy to add extra features like style options or download

# Tech Stack
Frontend-Streamlit
Backend-Python
AI Model-Google Gemini LLMs (via google-generativeai)
Config-python-dotenv

# Install dependencies
pip install -r requirements.txt

# requirements.txt content:

streamlit
google-generativeai
python-dotenv
Pillow

#  Set up your API key
Create a .env file at the root of the project:
GOOGLE_API_KEY=your_gemini_api_key_here

# Run the app
streamlit run app.py
