# Google Agents Development Kit (ADK)
Experimental and educational projects for the Google Agents Development Kit (ADK), ranging from simple implementations to advanced multi-agent systems.
# Setup
1. **Clone Project**
	- `git clone https://github.com/user/repo.git`
2. **Creating a virtual Python environment**
	- `python -m venv .venv`
3. **Activate the virtual environment** (==Activate each new terminal instance==)
	- `source .venv/bin/activate`
4. **Install Packages**
	- `pip install -r requirements.txt` → Install requirements at once 
5. **Verify your installation**
	- `pip show google-adk`
6. Add `.env` file for API Keys inside your agent directory:
	1. Google API Key → https://aistudio.google.com/app/apikey
	2. OpenAi API Key → https://platform.openai.com/api-keys
	3. Anthropic API Key → https://console.anthropic.com/settings/keys
```yaml title:env
# Set to False to use API keys directly (required for multi-model)
GOOGLE_GENAI_USE_VERTEXAI=FALSE
# --- Replace with your actual keys ---
GOOGLE_API_KEY=YOUR_ACTUAL_GOOGLE_API_KEY_HERE
ANTHROPIC_API_KEY=YOUR_ACTUAL_ANTHROPIC_API_KEY_HERE
OPENAI_API_KEY=YOUR_ACTUAL_OPENAI_API_KEY_HERE
# --- End of keys ---
```


# Gemini Available Models
https://ai.google.dev/gemini-api/docs/models