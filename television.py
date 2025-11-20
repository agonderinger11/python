class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3
    
    def __init__(self) -> None:
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL
        
        self.__temp: int = 0
        
    def power(self) -> None:
        if self.__status == False:
            self.__status = True
        else: 
            self.__status = False
    
    def mute(self) -> None:
        if self.__status == False:
            return
        
        if self.__muted == False:
            self.__muted = True
            self.__temp = self.__volume
            self.__volume = 0
        else: 
            self.__muted = False
    
    def channel_up(self) -> None:
        if self.__status == False:
            return
        
        if self.__channel == self.MAX_CHANNEL:
            self.__channel = self.MIN_CHANNEL
        else:
            self.__channel += 1

    def channel_down(self) -> None:
        if self.__status == False:
            return
        
        if self.__channel == self.MIN_CHANNEL:
            self.__channel = self.MAX_CHANNEL
        else:
            self.__channel -= 1
    
    def volume_up(self) -> None:
        if self.__status == False :
            return
        elif self.__muted == True:
            self.__muted = False
            self.__volume = self.__temp
        
        if self.__volume == self.MAX_VOLUME:
            self.__volume = self.MAX_VOLUME
        else:
            self.__volume += 1
    
    def volume_down(self) -> None:
        if self.__status == False:
            return
        elif self.__muted == True:
            self.__muted = False
            self.__volume = self.__temp
        
        if self.__volume == self.MIN_VOLUME:
            self.__volume = self.MIN_VOLUME
        else:
            self.__volume -= 1
    
    def __str__(self) -> str:
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"