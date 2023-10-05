import pyttsx3

def generate_speech(text):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()
    
    # Set properties for the speech output
    # You can customize these properties as per your preference
    engine.setProperty('rate', 150)  # Speed of speech (words per minute)
    engine.setProperty('volume', 0.8)  # Volume (0.0 to 1.0)
    
    # Generate speech from the given text
    engine.say(text)
    engine.runAndWait()

# Example usage
text_content = "Hello, how are you? This is a sample text for speech generation."
generate_speech(text_content)
