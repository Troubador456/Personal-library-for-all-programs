import random
game = True
rps = ["rock", "paper", "scissors"]
def calcer(c,u):
    if c == u:
        return "draw!"
    for r in range(len(rps)):
        k = r + 1
        if r == 2:
            k = 0
        if c == rps[r] and u == rps[k]:
            return "User wins!"
        if c == rps[k] and u == rps[r]:
            return "Computer wins!"
while game == True:
    game = False
    print("Welcome to Rock, Paper, Scissors")
    play = input("1 or 2 Players? (enter 1 or 2): ")
    if play == "1":
        choice = random.randint(0,2)
        uChoice = (input("Rock, Paper, or Scissors?: ").lower())
        res = calcer(rps[choice], uChoice)
        print(res)
        print(f"Player: {uChoice}")
        print(f"Computer: {rps[choice]}")
    elif play == "2":
        print("Turn the computer to the person who is going first")
        fChoice = input("Rock, Paper, or Scissors?: ")
        print("Turn the computer to the person who is going second")
        sChoice = input("Rock, Paper, or Scissors?: ")
        res = calcer(fChoice, sChoice)
        if res == "Computer wins!":
            print("2nd Player wins!")
        else:
            print(res)
        print(f"First Player: {fChoice}")
        print(f"Second Player: {sChoice}")
        

