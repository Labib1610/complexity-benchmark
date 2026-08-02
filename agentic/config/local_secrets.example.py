# Copy this file to local_secrets.py and fill in your real keys (local_secrets.py is gitignored).
# Local API keys. NOT committed - see .gitignore.
# Replace the placeholder strings below with real keys.

# Gemini (OpenAI-compatible endpoint).
# Currently used by: teacher, verifier, and the closed-source student.
GEMINI_API_KEY = "PASTE_GEMINI_KEY_HERE"

# Added later - leave as-is until used.
OPENAI_API_KEY = "PASTE_OPENAI_KEY_HERE"
ANTHROPIC_API_KEY = "PASTE_ANTHROPIC_KEY_HERE"
OPENROUTER_API_KEY = "PASTE_OPENROUTER_KEY_HERE"

# Optional: override the local Ollama endpoint.
OLLAMA_HOST = "http://localhost:11434"
