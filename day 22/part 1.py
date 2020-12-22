inp = [x for x in open("input.txt").read().split("\n\n")]

player1Cards = []
player2Cards=[]
for l in inp[0].split("\n")[1:]:
    player1Cards.append(int(l))
for l in inp[1].split("\n")[1:]:
    player2Cards.append(int(l))
print(player1Cards)
print(player2Cards)

while len(player1Cards)>0 and len(player2Cards) > 0:
    pl1card = player1Cards.pop(0)
    pl2card = player2Cards.pop(0)
    if pl1card>pl2card:
        player1Cards.append(pl1card)
        player1Cards.append(pl2card)
    else:
        player2Cards.append(pl2card)
        player2Cards.append(pl1card)
    print()
    print(player1Cards)
    print(player2Cards)

winner = (player1Cards if len(player1Cards)>0 else player2Cards)
winner.reverse()
score = 0
for i, n in enumerate(winner):
    score += (i+1)*n
print(score)
