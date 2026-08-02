





# Voice-to-Voice AI Assistant



## Description



A Voice-to-Voice AI Assistant that converts user speech into text using OpenAI Whisper, processes the text using Cohere to generate an AI response, and converts the response back into audio using gTTS.



## How It Works



The project consists of three main stages:



### 1. Speech-to-Text



The application receives an audio file from the user and uses OpenAI Whisper to convert the spoken audio into written text.



### 2. LLM Processing



The generated text is sent to the Cohere Large Language Model, which processes the user's input and generates an appropriate AI response.



### 3. Text-to-Speech



The AI-generated response is converted back into speech using gTTS and saved as an audio file.



## Technologies Used



- Python

- OpenAI Whisper

- Cohere

- gTTS

- FFmpeg



## Project Structure



```text

Voice-AI-Assistant/

├── app.py

├── requirements.txt

├── README.md

├── .gitignore

├── audio/

│   └── input.wav

└── src/

    ├── speech_to_text.py

    ├── llm.py

    └── text_to_speech.py

```



## Requirements



Before running the project, make sure you have:



- Python 3.13

- FFmpeg

- A Cohere API Key



## Installation



Clone the repository:



```bash

git clone YOUR_REPOSITORY_URL

```



Navigate to the project directory:



```bash

cd Voice-AI-Assistant

```



Install the required Python packages:



```bash

pip install -r requirements.txt

```



## FFmpeg



FFmpeg is required by Whisper to process audio files.



Make sure FFmpeg is installed and available through the system PATH.



You can verify the installation with:



```bash

ffmpeg -version

```



## Environment Variables



Create a `.env` file in the project root directory and add your Cohere API key:



```env

COHERE_API_KEY=your_api_key_here

```



Do not upload the `.env` file to GitHub.



## Input Audio



Place the input audio file inside the `audio` folder with the following name:



```text

audio/input.wav

```



The application uses this file as the user's voice input.



## Running the Project



Run the application using:



```bash

python app.py

```



The application will perform the following steps:



1. Convert the input audio to text using Whisper.

2. Send the text to Cohere.

3. Generate an AI response.

4. Convert the AI response to speech using gTTS.

5. Save the generated audio output.



## Example Workflow



```text

Input Audio

     ↓

Whisper

     ↓

Speech-to-Text

     ↓

Cohere LLM

     ↓

AI Response

     ↓

gTTS

     ↓

Audio Output

```



## Example



The user provides a WAV audio file containing speech.



Whisper converts the speech into text:



```text

User: Hello, how are you?

```



The text is sent to Cohere, which generates an AI response:



```text

AI: I'm doing well. How can I help you?

```



The response is then converted into an audio file using gTTS.



## Security



The Cohere API key is stored in the `.env` file and should never be uploaded to GitHub.



The `.gitignore` file is configured to prevent sensitive files and generated files from being uploaded.



## Author



Adel

```



