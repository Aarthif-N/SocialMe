# SocialMe: Social Media Chat Assistant

SocialMe is a conversational AI assistant designed to provide an engaging chat experience. It uses OpenAI's GPT model to interact with users and help them with social media-related queries. This project is built using FastAPI, ensuring a robust and scalable backend.

---

## Features

- **Interactive Chat**: Chat with an AI assistant named SocialMe.
- **Customizable Responses**: Tailor responses using system prompts.
- **Modern UI**: User-friendly interface with a sleek design and background.
- **Supports Bullet Points and Lists**: Formats responses with lists dynamically.

---

## Steps to Run Locally

### Prerequisites

1. Have Python installed (version 3.8 or above).

### Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd social-me
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up the Environment**:
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key to the `.env` file:
     ```plaintext
     OPENAI_KEY=your_openai_api_key
     ```

4. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

5. **Start Chatting**:
   - Open your browser and navigate to `http://127.0.0.1:8000`.

---

## Project Structure

```plaintext
social-me/
├── main.py                # Entry point for the application
├── controllers/
│   └── api.py             # API logic for chat endpoints
├── models/
│   └── chatModel.py 
|   └── openaiModel.py 
├── utils/
│   └── openai.py         # Utility functions for OpenAI integration
├── templates/
│   └── index.html         # Frontend HTML file
├── .env                   # Environment variables (not committed to Git)
├── .gitignore             # Git ignore file
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---
