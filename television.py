class Television:
    '''class representing television'''

    min_volume = 0
    max_volume = 20
    min_channel = 0
    max_channel = 100

    def __init__(self):
        '''setting up default values'''

        self.__status = False
        self.__muted = False
        self.__volume = self.min_volume
        self.__channel = self.min_channel

    def power(self):
        '''setting for the television on/off'''

        self.__status = not self.__status

    def mute(self):
        '''mute and unmute setting'''
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        '''tv channel goes up'''

        if self.__status:
            if self.__channel == self.max_channel:
                self.__channel = self.min_channel
            else:
                self.channel += 1

    def channel_down(self):
        '''tv channel goes down'''

        if self.__status:
            if self.__channel == self.min_channel:
                self.__channel = self.max_channel
            else:
                self.channel -= 1

    def volume_up(self):
        '''this increases the volume for the tv'''

        if self.__status:
            if self.__volume < self.max_volume:
                self.__volume += 1
                self.__muted = False

    def volume_down(self):
        '''decrease tv volume'''

        if self.__status:
            if self.__volume > self.min_volume:
                self.__volume -= 1
                self.__muted = False

    def __str__(self):
        '''returning string to tv'''

        return f'Power={self.__status}, Channel={self.__channel},Volume={self.__volume}'




