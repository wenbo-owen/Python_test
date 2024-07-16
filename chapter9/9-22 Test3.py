class Instrument():
    def __init__(self):
        pass
    def make_sound(self):
        pass

class Erhu(Instrument):

    def make_sound(self):
        print('二胡正在演奏')

class Piano(Instrument):

    def make_sound(self):
        print('钢琴正在演奏')

class Violin(Instrument):
    def make_sound(self):
        print('小提琴正在演奏')

def play(obj):
    obj.make_sound()

er = Erhu()
piano = Piano()
violin = Violin()

play(er)
play(piano)
play(violin)


