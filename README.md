# AI ChatBot

Welcome to the AI ChatBot project! This application leverages the power of [Ollama](https://ollama.com/) and a simple yet effective user interface built with Python's Tkinter library. The chatbot is designed to engage in conversations by answering user questions based on the provided context, making it a perfect tool for a variety of use cases, from customer support to casual chat.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [License](#license)

## Features

- **Interactive GUI:** A user-friendly interface that allows you to chat with the AI seamlessly.
- **Contextual Responses:** The chatbot remembers the conversation history to provide relevant answers.
- **Download Chat:** Save the conversation to a text file for future reference.
- **Fullscreen Mode:** Toggle fullscreen mode for an immersive chatting experience.
- **Asynchronous Processing:** Non-blocking UI with background processing for smooth interactions.

## Installation

Follow the steps below to set up the project on your local machine:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/AI-ChatBot.git
    cd AI-ChatBot
    ```

2. **Create a Virtual Environment:**
    ```bash
    python -m venv chatbot
    ```

3. **Activate the Virtual Environment:**
    - On Windows:
      ```bash
      chatbot\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source chatbot/bin/activate
      ```

4. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Once the setup is complete, you can start the chatbot by running the `main.py` file:

```bash
python main.py
```

### How to Interact:

1. **Start Chatting:** Type your questions in the input field and press `Enter` or click the "Send" button.
2. **Toggle Fullscreen:** Press `F11` to toggle fullscreen mode. Press `Escape` to exit fullscreen.
3. **Download Conversation:** Click the "Download" button to save the chat history as a `.txt` file.

### Exiting the Application:

To exit the chatbot, simply type `exit` in the input field or close the window.

