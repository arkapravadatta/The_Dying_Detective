🕵️ About "The Dying Detective" – A Sherlock Holmes Chatbot
The Dying Detective is a character-based chatbot built using LangChain, Streamlit, and GROQ's LLaMA3-70B language model. This bot takes on the persona of Sherlock Holmes, the legendary detective created by Sir Arthur Conan Doyle, delivering sharp, concise responses in true Holmesian fashion.

🔍 Features
Character Roleplay: Maintains the personality, tone, and style of Sherlock Holmes.

Streamlit Interface: Clean and interactive frontend for entering queries.

LLM Powered: Utilizes Groq's LLaMA3-70B model for fast and intelligent responses.

LangChain Pipeline: Combines prompt templates, Groq LLM, and output parsing.

LangSmith Tracing Enabled: Full request/response tracing is activated for debugging and performance analysis.

⚙️ Environment Setup
The project relies on environment variables stored in a .env file:

GROQ_API_KEY

LANGCHAIN_API_KEY

LANGSMITH_TRACING_V2=true

⚠️ Note: The .env file is not uploaded to this repository for security reasons. Please create your own .env file with valid API keys to run the application.
