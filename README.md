# YouTube Video Summarizer

The **YouTube Video Summarizer** is a tool designed to help students, educators, and lifelong learners extract concise notes from educational or lecture videos. By leveraging the power of AI, this project takes a video transcript and generates a summarized version, making it easier to review and retain key information.

## Features

- **Transcript Summarization**: Converts lengthy video transcripts into concise, easy-to-read notes.
- **Educational Focus**: Optimized for educational and lecture-style videos.
- **Local AI Model**: Uses a local AI model (`qwen2.5`) for privacy and offline functionality.


## Prerequisites

Before using the YouTube Video Summarizer, ensure you have the following installed:

1. **Ollama**: A tool to manage and run local AI models.
2. **Python**: The project is built using Python, so ensure you have it installed.

## Installation

1. **Install Ollama**:
   - Download and install Ollama from the official website: [Ollama](https://ollama.ai/).

2. **Pull the AI Model**:
   - Run the following command to download the `qwen2.5` model:
     ```bash
     ollama pull qwen2.5
     ```

3. **Download the Project**:
   - Clone or download the YouTube Video Summarizer project from the repository.

4. **Install Dependencies**:
   - Navigate to the project directory and install the required dependencies using `uv`:
     ```bash
     uv pip install requirements.txt
     ```

## Usage

**Run the Streamlit App**:
   - After installing the dependencies, start the Streamlit web app by running:
     ```bash
     uv run streamlit run app.py
     ```
   - This will launch the app in your default web browser.

## Model Information

The project uses the `qwen2.5` model, a local AI model optimized for text summarization.
