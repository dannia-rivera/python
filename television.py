class Television:
    #class representing television

    min_volume: int = 0
    max_volume: int = 20
    min_channel:int  = 0
    max_channel: int = 100

    def __init__(self) -> None:
        '''
        setting up default values
        '''
        self.__status = False
        self.__muted = False
        self.__volume: int = Television.min_volume
        self.__channel: int = Television.min_channel

    def power(self):
        '''
        setting for the television on/off
        '''
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        '''
        This function mutes and unmutes the television when its on
        '''
        if self.__status:
            if self.__muted is False:
                self.__muted = True
            else:
                self.__muted = False
        else:
            self.__volume = Television.min_volume



    def channel_up(self) -> None:
        '''
        This function makes tv channel go up when the tv in on
        '''
        if self.__status:
            if self.__channel < Television.max_channel:
                self.__channel += 1
            else:
                self.channel = Television.min_channel

    def channel_down(self) -> None:
        '''
        This function makes tv channel go down when the tv in on
        '''
        if self.__status:
            if self.__channel > Television.min_channel:
                self.__channel -= 1
            else:
                self.__channel = Television.max_channel

    def volume_up(self) -> None:
        '''
        this function increases the volume for the tv and unmutes the tv
        '''
        if self.__status:
            self.__muted = False
            if self.__volume < Television.max_volume:
                self.__volume += 1
            else:
                pass

    def volume_down(self) -> None:
        '''
        This function decrease tv volume and unmutes if tv is muted
        '''
        if self.__status:
            self.__muted = False
            if self.__volume > Television.min_volume:
                self.__volume -= 1
            else:
                pass

    def __str__(self):
        '''
        This function makes sure that if the tv is mutes it returns the values like power, channel, and volume
        '''
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.min_volume}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'




