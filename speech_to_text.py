import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to record audio from the microphone
def record_audio(duration=5, filename="recorded_audio.wav"):
    with sr.Microphone() as source:
        print("Recording...")
        audio_data = recognizer.record(source, duration=duration)

    # Save the recorded audio to a file
    with open(filename, "wb") as f:
        f.write(audio_data.get_wav_data())

    print("Audio recorded and saved as", filename)

# Function to convert audio to text
def audio_to_text(audio_file):
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

        # Recognize the speech using Google Speech Recognition
        # try:
            # Use Google Speech Recognition
        text = recognizer.recognize_google(audio_data)
            # print("Text:", text)
        # except sr.UnknownValueError:
            # print("Google Speech Recognition could not understand the audio.")
        # except sr.RequestError as e:
            # print("Could not request results from Google Speech Recognition service; {0}".format(e))

        return str(text)

# Record audio from microphone and save it
# record_audio()

# # Convert recorded audio to text
# audio_file = "recorded_audio.wav"
# audio_to_text(audio_file)