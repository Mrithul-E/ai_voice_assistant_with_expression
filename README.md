# ai_voice_assistant_with_expression


# AI Voice Assistant with Emotion and Web Browsing Capability

This project implements an AI voice assistant capable of emulating a friendly interaction with users, including various emotions. The assistant utilizes Google's Generative AI and integrates features such as web browsing and emotion recognition. Below are the key functionalities and instructions for using the voice assistant.

### Can used in respberry-pi with a little manipulation

## Features:

- **Natural Language Interaction:** Engages users in conversation, providing information from google palm2 *palm2 can make mistakes.
- **Emotion Recognition:** Understands and responds with different emotions, enhancing the interaction experience.
- **Web Browsing:** Opens web browsers and searches for topics specified by the user.
- **Speech Recognition:** Listens for user commands and responds accordingly.

## Setup and Requirements:

1. **Python Libraries:**
   - `google.generativeai`: Used for generating AI-driven responses.
   - `speech_recognition`: Allows the assistant to recognize speech input.
   - `pyttsx3`: Provides text-to-speech functionality.
   - `vlc`: Handles video playback.
   - `pygame`: Used for audio playback.
   - `webbrowser`: Enables opening web browser links.

   Install the required libraries using `pip`:
   ```
   pip install google-generativeai speech_recognition pyttsx3 vlc pygame
   ```

2. **Google Palm2 API Key:**
   Obtain an API key for Google Palm2 API and replace `"google palm2 api key"` with your actual API key in the code.
   Use Your API Key with Caution:
   Ensure that you use your API key responsibly and avoid sharing it publicly. API usage can have associated costs, and running out of API credits may disrupt the functionality of the voice assistan
   
   *Note:You can get api key for free from makersuite without credit card*

4. **Emotion Videos:**
   Ensure that emotion videos (e.g., `"happy.mp4"`, `"sad.mp4"`, `"angry.mp4"`, etc.) are available in the specified directory (`"./face for robot/"` in the code).

## Usage:

1. **Run the Script:**
   Run the Python script to start the voice assistant. It will listen for your commands and respond accordingly.

2. **Interact Naturally:**
   Feel free to ask questions, request information, or instruct the assistant. It will respond with relevant information and emotions.

3. **Note:**
   - Ensure a stable internet connection for accessing external resources.
   - Emotion videos should be appropriately named and placed in the designated directory.

Enjoy interacting with your AI Voice Assistant! If you encounter any issues or have further questions, feel free to ask.
