# AI Voice Assistant with Emotion and Web Browsing Capability

## Project Overview:

Welcome to our AI Voice Assistant project, designed to provide users with a seamless and friendly interaction experience. This advanced assistant not only engages in natural language conversations but also recognizes and responds with various emotions, enhancing the overall interaction. Additionally, it offers web browsing capabilities, enabling users to explore topics of interest effortlessly.

### Compatibility: 
This project is Raspberry Pi compatible with minimal adjustments, making it accessible to a wide range of users.

## Key Features:

- **Natural Language Interaction:** Engages users in meaningful conversations, providing accurate and relevant information sourced from Google's Generative AI. Please note that while the assistant utilizes Google's Generative AI, occasional mistakes might occur.
  
- **Emotion Recognition:** Enhances user experience by understanding and responding with different emotions. This feature adds a human touch to interactions, making the experience more relatable and engaging.
  
- **Web Browsing:** Seamlessly opens web browsers and conducts searches based on user-specified topics. Stay updated with the latest information without leaving the conversation.
  
- **Speech Recognition:** Listens attentively to user commands and responds promptly. The assistant is designed to accurately recognize speech inputs, ensuring a smooth interaction process.
  
- **Auto Speech Listening Turn-off:** Cognizant of internet usage, the assistant automatically turns off speech listening after three consecutive instances of user inactivity, optimizing resources and enhancing efficiency.

## Setup and Requirements:

### 1. Python Libraries:

Ensure you have the following Python libraries installed:

- `google.generativeai`: Utilized for generating AI-driven responses.
- `speech_recognition`: Enables speech recognition functionality.
- `pyttsx3`: Provides text-to-speech capabilities.
- `vlc`: Handles video playback.
- `pygame`: Used for audio playback.
- `webbrowser`: Facilitates web browser operations.

Install the required libraries using the following command:

```
pip install google-generativeai speech_recognition pyttsx3 vlc pygame
```

### 2. Google Palm2 API Key:

Obtain an API key for Google Palm2 API and replace `"google palm2 api key"` with your actual API key in the code. We emphasize the importance of responsible API usage to avoid any disruptions in the functionality of the voice assistant.

*Note: You can obtain a free API key from MakerSuite without the need for a credit card.*

### 3. Emotion Videos:

Ensure emotion videos (e.g., `"happy.mp4"`, `"sad.mp4"`, `"angry.mp4"`, etc.) are available in the specified directory (`"./face for robot/"` in the code). Proper naming and placement of these videos are crucial for the assistant to accurately convey emotions during interactions.

## Usage:

1. **Run the Script:**
   Execute the Python script to initiate the voice assistant. The assistant will be ready to listen to your commands and respond promptly.

2. **Interact Naturally:**
   Engage in natural conversations, ask questions, request information, or provide instructions. The assistant will respond with relevant information and convey emotions, creating a personalized and immersive experience.

3. **Important Notes:**
   - Ensure a stable internet connection for seamless access to external resources.
   - Verify that emotion videos are appropriately named and placed in the designated directory to enable emotion recognition.

Enjoy the interactive experience with your AI Voice Assistant! Should you encounter any issues or have further inquiries, please do not hesitate to reach out. Your seamless interaction is our priority.

source of files in "robot expression folder" : [https://www.youtube.com/watch?v=S79FH99aQWk](https://www.youtube.com/watch?v=S79FH99aQWk)
