# Structuring Data  
- Scenarios requiring structured data exchange  
- We will use `output_schema` option  
- Note/Constraint: You can't use `output_schema` when using Tools or transfere info to other agents , but there are a soltuion by making the last agent in the workflow to use the `output_schema`  

- `output_key` : save the output to the session's state dictionary under this key (e.g., session.state[output_key] = agent_response_text). This is useful for passing results between agents or steps in a workflow.  

# Reference:
- https://google.github.io/adk-docs/agents/llm-agents/#structuring-data-input_schema-output_schema-output_key