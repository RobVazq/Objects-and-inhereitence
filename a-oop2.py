#Roberto Vazquez

class theboys:

    def __init__(self, name):
        self.name = name

    def saturday(self):
        return self.name

boy1 = theboys('AngryBeto')
boy2 = theboys('Wertyman8')
boy3 = theboys('JoSweaty')

x =  input("Saturday is for the _____.")

if x != 'boys':
    print("{} would be ashamed".format(boy3.saturday()))
else:
    print('{} and {} are proud you said that.'.format(boy2.saturday(), boy1.saturday()))

#saturday is for the boys
        


