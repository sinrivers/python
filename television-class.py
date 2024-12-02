class Television:
    # Class variables (constants)
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initialize a Television object with default settings.

        Default settings:
        - status (power): False (TV is off)
        - muted: False
        - volume: Minimum volume
        - channel: Minimum channel
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggle the power status of the television.

        Switches the TV between on and off states.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Toggle the mute status of the television.

        Only applies when the TV is on.
        When unmuting, restores the previous volume.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Increase the channel number when the TV is on.

        If at the maximum channel, wraps around to the minimum channel.
        """
        if self.__status:
            self.__channel = (self.__channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        """
        Decrease the channel number when the TV is on.

        If at the minimum channel, wraps around to the maximum channel.
        """
        if self.__status:
            self.__channel = (self.__channel - 1) % (self.MAX_CHANNEL + 1)

    def volume_up(self) -> None:
        """
        Increase the volume when the TV is on.

        If muted, unmute the TV.
        Volume cannot exceed the maximum volume.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            self.__volume = min(self.__volume + 1, self.MAX_VOLUME)

    def volume_down(self) -> None:
        """
        Decrease the volume when the TV is on.

        If muted, unmute the TV.
        Volume cannot go below the minimum volume.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            self.__volume = max(self.__volume - 1, self.MIN_VOLUME)

    def __str__(self) -> str:
        """
        Return a string representation of the Television's current state.

        Format: Power=[status], Channel=[channel], Volume=[volume]
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
