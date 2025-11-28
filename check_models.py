import google.generativeai as genai

API_KEY = os.getenv("GEMINI_API_KEY")  # Use the same key you generated
genai.configure(api_key=API_KEY)

print("Checking available models...")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)