from furhat_remote_api import FurhatRemoteAPI


class FurhatController:
    def __init__(self) -> None:
        self.furhat = None
        self.voices = []

    def connect(self, address: str):
        """
        Connect to the Furhat robot or the SDK running the virtual robot.

        :param address: The address of the robot or the SDK.
        :type address: str
        """
        self.furhat = FurhatRemoteAPI(address)
        self.voices = self.furhat.get_voices()
        self.furhat.set_voice(name='Matthew')

    def set_voice(self, voice: str):
        """
        Set the voice of the Furhat robot.

        :param voice: The name of the voice to set.
        :type voice: str
        """
        assert self.furhat is not None, "Furhat not connected"
        self.furhat.set_voice(name=voice)

    def say_text(self, text: str, lipsync: bool = True):
        """
        Make the Furhat robot say the given text.

        :param text: The text to say.
        :type text: str
        :param lipsync: Whether to enable lip synchronization or not.
        :type lipsync: bool
        """
        assert self.furhat is not None, "Furhat not connected"
        self.furhat.say(text=text, lipsync=lipsync)

    def say_url(self, url: str, lipsync: bool = True):
        """
        Make the Furhat robot say the text from the given URL.

        :param url: The URL to get the text from. Must be in .wav format.
        :type url: str
        :param lipsync: Whether to enable lip synchronization or not.
        :type lipsync: bool
        """
        assert self.furhat is not None, "Furhat not connected"
        self.furhat.say(url=url, lipsync=lipsync)