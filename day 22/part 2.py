inp = [x for x in open("input.txt").read().split("\n\n")]
import time

player1Cards = []
player2Cards=[]
for l in inp[0].split("\n")[1:]:
    player1Cards.append(int(l))
for l in inp[1].split("\n")[1:]:
    player2Cards.append(int(l))
print(player1Cards)
print(player2Cards)



def gameRound(pl1subcards, pl2subcards):
    rounds = []
    while len(pl1subcards)>0 and len(pl2subcards) > 0:
        if (any( [r ==[pl1subcards,pl2subcards] for r in rounds])):
            return [True,pl1subcards,pl2subcards]
        else:
            rounds.append([pl1subcards.copy(),pl2subcards.copy()])
        pl1card = pl1subcards.pop(0)
        pl2card = pl2subcards.pop(0)
        if  (len(pl1subcards)>=pl1card and len(pl2subcards)>=pl2card):
            if(gameRound(pl1subcards[:pl1card], pl2subcards[:pl2card])[0]):
                pl1subcards.append(pl1card)
                pl1subcards.append(pl2card)
            else:
                pl2subcards.append(pl2card)
                pl2subcards.append(pl1card)
        elif pl1card>pl2card:
            pl1subcards.append(pl1card)
            pl1subcards.append(pl2card)
        else:
            pl2subcards.append(pl2card)
            pl2subcards.append(pl1card)
    return [True if len(pl1subcards)>0 else False, pl1subcards, pl2subcards]



[p1win, pl1, pl2] = gameRound(player1Cards, player2Cards)

winner = (player1Cards if p1win else player2Cards)
winner.reverse()
score = 0
for i, n in enumerate(winner):
    score += (i+1)*n
print(score)
