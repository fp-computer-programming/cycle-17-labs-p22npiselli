# Nolan Piselli

class TV_remote():
    channel = 0
    volume_level = 0
    on = False
    def to_string():
        return TV_remote
print(TV_remote.to_string())
#class
class TV_remote:
    #functions
    def __init__(self):
        self.channel = 0
        self.volume = 0
        self.On = False
    def to_string(self):
        return "Channel:",self.channel,"Volume:",self.volume,"On:",self.On
#test
tv = TV_remote()
print(tv.to_string())