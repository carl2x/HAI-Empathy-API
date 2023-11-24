import time
from furhat_controller import FurhatController
from swagger_client.models.status import Status


class Dummy:
    def __init__(self) -> None:
        self.furhat = FurhatController()
        self.furhat.connect()

    def speak_text(self, text: str, times: int = 1, pause: int = 0):
        """
        Make the Furhat robot say the given text.

        :param text: A string depicting a utterance the robot should say.
        :param times: The number of times the robot should say the text.
        :param pause: The number of seconds to pause between each utterance.
        """
        for i in range(times):
            print(f"Speaking: {text}")
            print(
                f"Estimated reading time: {self.estimate_reading_time(text):.2f} seconds"
            )
            self.furhat.say(mode="text", text=text)
            time.sleep(self.estimate_reading_time(text))

            print(f"Pausing for {pause} seconds\n")
            time.sleep(pause)
        print("Done speaking\n------------------")

    def speak_url(self, url: str):
        """
        Make the Furhat robot say the given text.

        :param url: A url link to a audio file (.wav)
        """
        print(f"Speaking: {url}")
        self.furhat.say(mode="url", url=url)
        print("Done speaking\n------------------")

    def estimate_reading_time(self, text: str):
        """
        Estimate the reading time of a text in seconds.

        :param text: A string depicting a utterance the robot should say.
        :param wpm: The number of words per minute the robot reads at. 140 is the estimate.
        """
        wpm = 150
        return len(text.split(" ")) / wpm * 60

    def listen(self):
        """
        Make the Furhat robot listen for speech.
        """
        print("Listening...")
        ret = self.furhat.listen()
        assert type(ret) == Status
        print(f"Heard {ret}\n------------------")
        return ret.message


if __name__ == "__main__":
    dummy = Dummy()
    dummy.speak_text("Hello, my name is Furhat. I am a social robot.", times=1, pause=1)
    
    message = dummy.listen()  
    assert message is not None
    if "how are you" in message.lower():
        dummy.speak_text("I am fine, thank you.")
