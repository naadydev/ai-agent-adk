# Using Mulit LLM providers 
- You can work with different LLM providers through LiteLLM integration, so you have flexibility to choose the right model for each agent in your system.
- Make sure you installed LiteLLM package: `pip install litellm  
- https://docs.litellm.ai/docs/providers

### Using OpenRouter with LiteLlm
You can also use OpenRouter to switch between models using 1 same single API Key:
```python
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
model = LiteLlm(
 model="openrouter/openai/gpt-4.1",
 api_key=openrouter_api_key,
 )
```