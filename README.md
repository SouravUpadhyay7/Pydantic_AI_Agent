# Pydantic_AI_Agent
<div align="center">
  
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pydantic](https://img.shields.io/badge/Pydantic-2.0+-yellow.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.12+-red.svg)
![Groq](https://img.shields.io/badge/Groq-API-green.svg)
![Tavily](https://img.shields.io/badge/Tavily-API-purple.svg)
![License](https://img.shields.io/badge/License-MIT-blue.svg)
[![Google Colab](https://img.shields.io/badge/Google%20Colab-Open-orange.svg)](https://colab.research.google.com/)
</div>

## 🎥 Demo Video
<video width="800" height="450" controls>
  <source src="videos/Untitled video - Made with Clipchamp (2).mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## 📌 Overview
Pydantic_AI_Agent is a versatile AI agent framework that leverages type-safe data structures using Pydantic alongside state-of-the-art LLM APIs. The agent can be deployed either through Google Colab for quick experimentation or as a local Streamlit application for a more integrated experience.

## 📸 Screenshots
<img src="images/Screenshot 2025-06-10 102327.png" alt="Streamlit Interface" width="600"/>

<img src="images/Screenshot 2025-06-10 102420.png alt="working screenshot" width="600"/>

## ✨ Features
- 🤖 Structured AI interactions using Pydantic validation
- 🔍 Integration with Tavily for enhanced search capabilities
- 🧠 Groq API for fast LLM inference
- 📊 Streamlit UI for interactive use
- 📓 Google Colab notebook for quick prototyping
- 🐍 Modular Python codebase for easy extension
## 🛠️ Technology Stack
- **Python**: Core programming language
- **Pydantic**: Type validation and settings management
- **Groq API**: LLM service for natural language processing
- **Tavily API**: Search augmentation
- **Streamlit**: UI framework for the web application
- **Google Colab**: Hosted Jupyter notebook environment
## 🚀 Getting Started
### Prerequisites
- Python 3.8+
- Groq API key
- Tavily API key
### Installation
1. Clone the repository:
   ```
   git clone https://github.com/SouravUpadhyay7/Pydantic_AI_Agent.git
   cd Pydantic_AI_Agent
   ```
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Set up your environment variables:
   ```
   export GROQ_API_KEY="your_groq_api_key"
   export TAVILY_API_KEY="your_tavily_api_key"
   ```
## 🖥️ Usage
### Option 1: Run locally with Streamlit
```
streamlit run app.py
```
This will start a local server, typically at `http://localhost:8501`, where you can interact with the AI agent through a web interface.
### Option 2: Run in Google Colab
Open the `pydantic_ai_agent.ipynb` file in Google Colab and follow the instructions within the notebook. You'll need to provide your API keys in the designated cells.
## 📁 Project Structure
- `README.md`: Project documentation
- `requirements.txt`: Required Python packages
- `agent_utils.py`: Utility functions for the AI agent
- `app.py`: Streamlit application
- `pydantic_ai_agent.ipynb`: Google Colab notebook
## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
MIT License
Copyright (c) 2025 Sourav Upadhyay
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
