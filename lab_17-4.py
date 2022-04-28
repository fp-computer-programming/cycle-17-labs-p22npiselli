# Nolan Piselli

#class
class TV_remote:
#functions
    def __init__(self):
        """ Initializing values """
        self.channel = 0
        self.volume = 0
        self.On = False
    def to_string(self):
        return "Channel:",self.channel,"Volume:",self.volume,"On:",self.On
    def turn_on(self):
        self.On = True
    def turn_off(self):
        self.On = False
    def volume_up(self):
        self.volume += 1
    def volume_down(self):
        self.volume -= 1
    def channel_up(self):
        self.channel += 1
    def channel_down(self):
        self.channel -= 1
        #test
tv = TV_remote()
print(tv.to_string())