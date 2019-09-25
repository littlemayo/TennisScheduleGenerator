import random

class Players:

    def __init__(self, id):
        self.id = id
        self.playedWith = []

    def add_player(self, playedWith):
        self.playedWith = playedWith

    def name(self, name):
        self.name = name

p1 = Players(1)
p2 = Players(2)
p3 = Players(3)
p4 = Players(4)
p5 = Players(5)
p6 = Players(6)
p7 = Players(7)
p8 = Players(8)
p9 = Players(9)
p10 = Players(10)
p11 = Players(11)
p12 = Players(12)

p1.name = "Chad"
p2.name = "Brad"
p3.name = "Rob"
p4.name = "Zack"
p5.name = "Phil"
p6.name = "Dan"
p7.name = "Vector"
p8.name = "Robert"
p9.name = "Ben"
p10.name = "Thomas"
p11.name = "Brendan"
p12.name = "Rick"

player = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]

random.shuffle(player)

dub1 = [player[0].name, player[1].name]
dub2 = [player[2].name, player[3].name]
dub3 = [player[4].name, player[5].name]
dub4 = [player[6].name, player[7].name]
dub5 = [player[8].name, player[9].name]
dub6 = [player[10].name, player[11].name]

dubpair1 = [dub1, dub2]
dubpair2 = [dub3, dub4]
dubpair3 = [dub5, dub6]

player[0].add_player(dub1)
player[1].add_player(dub1)
player[2].add_player(dub2)
player[3].add_player(dub2)
player[4].add_player(dub3)
player[5].add_player(dub3)
player[6].add_player(dub4)
player[7].add_player(dub4)
player[8].add_player(dub5)
player[9].add_player(dub5)
player[10].add_player(dub6)
player[11].add_player(dub6)

# First set of double pair created

random.shuffle(player)

testdub = [player[0], player[1]]

def secondRound():
    random.shuffle(player)
    duba1 = [player[0].name, player[1].name]
    duba2 = [player[2].name, player[3].name]
    duba3 = [player[4].name, player[5].name]
    duba4 = [player[6].name, player[7].name]
    duba5 = [player[8].name, player[9].name]
    duba6 = [player[10].name, player[11].name]

    if player[0].playedWith[1] in duba1[1]:
        secondRound()
    elif player[1].playedWith[1] in duba1[1]:
        secondRound()
    else:
        print "success"

secondRound()


