print("TEST.PY IS RUNNING")

import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if api_key:
    print("GROQ KEY FOUND")
else:
    print("GROQ KEY NOT FOUND")