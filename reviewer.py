import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Load the secret .env file
load_dotenv()

# 2. Get the key safely
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("Error: API Key not found. Make sure you have a .env file with GEMINI_API_KEY inside.")
    sys.exit(1)

genai.configure(api_key=API_KEY)

# 2. DEFINE THE AI MODEL
model = genai.GenerativeModel("gemini-2.0-flash")

def review_code(file_path):
    try:
        with open(file_path, "r") as f:
            code_content = f.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return

    # 3. PROMPT ENGINEERING 
    # We explicitly need to tell the AI to act as a Senior Engineer looking for SOLID violations.
    prompt = f"""
    Analyze the following Python code IMMEDIATELY for SOLID design principle violations.
    Do not greet me. Do not say "Okay". Just provide the review.
    
    CODE TO ANALYZE:
    ----------------
    {code_content}
    ----------------
    
    Output Format:
    1. List critical issues (focus on Single Responsibility Principle).
    2. Provide the REFACTORED CODE block.
    """

    print(f"🔍 Analyzing {file_path} with AI...\n")
    
    # 4. CALL THE API
    response = model.generate_content(prompt)
    
    # 5. DISPLAY RESULTS
    print(response.text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python reviewer.py <filename>")
    else:
        review_code(sys.argv[1])