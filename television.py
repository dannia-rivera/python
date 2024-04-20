class Television:
    #class representing television

    min_volume = 0
    max_volume = 20
    min_channel = 0
    max_channel = 100

    def __init__(self):
        #setting up default values

        self.__statues = False
        self.__muted = False
        self.__volume = self.min_volume
        self.__channel = self.min_channel


