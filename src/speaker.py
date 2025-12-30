import pyttsx3

class Speaker:
    def __init__(self, rate=150, volume=1.0, voice_index=1):
        """
        Initializes the TTS engine.
        :param rate: Speed of speech (default 150)
        :param volume: Volume level 0.0 to 1.0
        :param voice_index: 0 for Male, 1 for Female (usually)
        """
        self.engine = pyttsx3.init()
        
        # Set Properties
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
        
        # Set Voice
        voices = self.engine.getProperty('voices')
        if len(voices) > voice_index:
            self.engine.setProperty('voice', voices[voice_index].id)

    def save_audio(self, text, output_path):
        """
        Converts text to an MP3 file.
        """
        try:
            if not text or text.startswith("Error"):
                print("Invalid text provided for audio conversion.")
                return False

            print("Starting synthesis...")
            self.engine.save_to_file(text, output_path)
            self.engine.runAndWait()
            return True
        except Exception as e:
            print(f"Speech synthesis failed: {e}")
            return False