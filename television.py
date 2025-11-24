class Television:
    """
    A class to represent a television.
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3
    
    def __init__(self) -> None:
        """
        Initialize a television object with default settings. 
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL
        
        self.__temp: int = 0
        
    def power(self) -> None:
        """
        Turns the power either on or off depending on the current state.
        """
        if self.__status == False:
            self.__status = True
        else: 
            self.__status = False
    
    def mute(self) -> None:
        """
        Toggle the mute status of the television
        When muted, stores current volume and sets volume to 0
        When unmuted, restores previous volume
        Does nothing if TV is off
        """
        if self.__status:
            if self.__muted == False:
                self.__muted = True
                self.__temp = self.__volume
                self.__volume = 0
            else: 
                self.__muted = False
                self.__volume = self.__temp
    
    def channel_up(self) -> None:
        """
        Increase the channel by 1.
        Goes to MIN_CHANNEL if at MAX_CHANNEL.
        Does nothing if TV is off
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decrease the channel by 1.
        Goes to MIN_CHANNEL if at MAX_CHANNEL.
        Does nothing if TV is off
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1
    
    def volume_up(self) -> None:
        """
        Increase the volume by 1.
        If muted, unmutes and goes back to previous volume before increasing.
        Does nothing if already at MAX_VOLUME or if TV is off.
        """
        if self.__status:
            if self.__muted == True:
                self.__muted = False
                self.__volume = self.__temp
            if self.__volume == Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
            else:
                self.__volume += 1
    
    def volume_down(self) -> None:
        """
        Decrease the volume by 1.
        If muted, unmutes and goes back to previous volume before decreasing.
        Does nothing if already at MIN_VOLUME or if TV is off.
        """
        if self.__status:
            if self.__muted == True:
                self.__muted = False
                self.__volume = self.__temp
            if self.__volume == Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME
            else:
                self.__volume -= 1
    
    def __str__(self) -> str:
        """
        Return a string representation of the television's current state.
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"