from furhat_remote_api import FurhatRemoteAPI


class FurhatController:
    def __init__(self) -> None:
        self.furhat = None
        self.voices = []
        self.gestures = []

    def connect(self, address: str = "localhost"):
        """
        Connect to the Furhat robot or the SDK running the virtual robot.

        :param address: The address of the robot or the SDK.
        """
        self.furhat = FurhatRemoteAPI(address)
        self.voices = self.furhat.get_voices()
        self.furhat.set_voice(name="Matthew")
        self.gestures = self.furhat.get_gestures()

    def set_voice(self, name: str):
        """
        Set the voice of the Furhat robot.

        :param name: The name of the voice to set.
        """
        assert self.furhat is not None, "Furhat not connected"
        self.furhat.set_voice(name=name)

    def say(
        self,
        mode: str,
        text: str = "",
        url: str = "",
        blocking: bool = False,
        lipsync: bool = True,
        abort: bool = False,
    ):
        """
        Make the Furhat robot say the given text.

        :param mode: The mode of the say command (text or url).
        :param text: A string depicting a utterance the robot should say.
        :param url: A url link to a audio file (.wav)
        :param blocking: Whether to block execution before completion
        :param lipsync: If a URL is provided, indicate if lipsync files should be generated/looked for.
            It uses a .pho file hosted on the same url, or generates phonemes by itself.
        :param abort: Stops the current speech of the robot.
        """
        assert self.furhat is not None, "Furhat not connected"
        assert mode is not None, "Please set mode to text or url"
        if mode == "text":
            self.furhat.say(text=text, lipsync=lipsync, blocking=blocking, abort=abort)
        elif mode == "url":
            self.furhat.say(url=url, lipsync=lipsync, blocking=blocking, abort=abort)

    def say_stop(self):
        """
        Stops the current speech of the robot.
        """
        assert self.furhat is not None, "Furhat not connected"
        self.furhat.say_stop()

    def listen(self):
        """
        Make the Furhat robot listen for speech.

        :return: A string depicting the utterance the robot heard.
        """
        assert self.furhat is not None, "Furhat not connected"
        return self.furhat.listen()

    def listen_stop(self):
        """
        Stops the current listening of the robot.
        """
        assert self.furhat is not None, "Furhat not connected"
        self.furhat.listen_stop()

    def get_users(self):
        """
        Get a list of users currently in the Furhat robot's vision.

        :return: A list of users.
        """
        assert self.furhat is not None, "Furhat not connected"
        return self.furhat.get_users()

    def attend(
        self, mode: str, user: str = "CLOSEST", userid: str = "", location: str = ""
    ):
        """
        Make the Furhat robot attend to a user.

        :param mode: The mode of the attend command (user, userid, or location).
        :param user: Attend user based on enum (CLOSEST, OTHER or RANDOM).
        :param userid: Attend user based on it's id (can be retrieved by using get_users()).
        :param location: Attend location based on coordinates (x,y,z)
        """
        assert self.furhat is not None, "Furhat not connected"
        if mode == "user":
            self.furhat.attend(user=user)
        elif mode == "userid":
            self.furhat.attend(userid=userid)
        elif mode == "location":
            self.furhat.attend(location=location)

    def gesture(self, name: str):
        """
        Make the Furhat robot perform a gesture.

        :param name: The name of the gesture to perform.
        """
        assert self.furhat is not None, "Furhat not connected"
        self.furhat.gesture(name=name)
