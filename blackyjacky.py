# Importing libraries
import pydealer
import sys

print("Welcome to Blackjack!")

#Initializing to find how many times the user won, lost, and drew
global streak
streak = {"win": 0, "loss": 0, "draw": 0}

# Collects chips for user chip balance
global cred
while True:
  cred = input("How many chips would you like to give?: ")
  if cred.isnumeric():
    cred = int(cred)
    break
card_points = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 1
}

global times
times = 0
# Finds the amount of points when given a card
def convert(card):
  card = card.split(" ")[0]
  return card_points[card]
# Finds the result of the blackjack round
def result(k,bet,credsie):
  if k == "loss":
    streak["loss"] += 1
    credsie -= bet
    return ["m",credsie]
  elif k == "win":
    credsie += bet
    streak["win"] += 1
    return ["m",credsie]
  elif k == "draw":
    streak["draw"] += 1
    return ["m",credsie]
  else:
    return "n"
class Blackjack:
  #Initalizing the deck
  def __init__(self):
    self.times = times
    self.turn = 0
    self.userSum = 0
    self.dealerSum = 0
    self.userDeck = []
    self.dealerDeck = []
    # Assign the shuffled deck to self.deck

  #Deals to the user
  def hit(self,cred):
    self.turn += 1
    self.deck = pydealer.Deck()
    self.deck.shuffle()
    self.userHand = pydealer.Stack()
    self.dealerHand = pydealer.Stack()
    dealt_user = self.deck.deal(1)
    dealt_dealer = self.deck.deal(1)
    self.userHand.add(dealt_user)
    self.dealerHand.add(dealt_dealer)
    self.userDeck.append((str(dealt_user)))
    self.dealerDeck.append((str(dealt_dealer)))
    #Outputs the cards of the user and the dealer
    print("DEALERS CARDS: ")
    for i in range(len(self.dealerDeck)):
      print(f"{i+1}. {str(self.dealerDeck[i])}")
    print("YOUR CARDS: ")
    for i in range(len(self.userDeck)):
      print(f"{i+1}. {str(self.userDeck[i])}")
    # Gets the point value and adds it to the points each player has
    self.userNum = convert(self.userHand.cards[0].value)
    self.dealerNum = convert(self.dealerHand.cards[0].value)
    if self.userNum is not None:
      self.userSum += self.userNum
    if self.dealerNum is not None:
      self.dealerSum += self.dealerNum
    # Returns message based on result
    if self.userSum > 21:
      print("You busted! Dealer wins!")
      cred -= self.bet
      return "loss"
    if self.dealerSum > 21:
      print("You win!")
      cred += self.bet
      return "win"
    if self.userSum == 21:
      print("You win!")
      cred += self.bet
      return "win"
    if self.dealerSum == 21:
      print("Dealer wins!")
      cred -= self.bet
      return "loss"
    if self.userSum == 21 and self.dealerSum == 21:
      print("Draw!")
      return "draw"
  # Gets the user's bet on their chip balance  
  def better(self):
    self.bet = input("How much would you like to bet?: ")
    while True:
      if self.bet.isnumeric():
        self.bet = int(self.bet)
        if self.bet > cred:
          print("You don't have enough credits!")
          self.bet = input("How much would you like to bet?: ")
        else:
          break
      else:
        print("Hey, that's not a number!")
        self.bet = input("How much would you like to bet?: ")
  # Gives user the ability to stand  
  def stand(self):
    self.turn += 1

# Added line to print the dealer's hand

while True:
  global t
  t = ""
  global m
  m = ""
  # Initializes class
  user = Blackjack()
  user.better()
  user.bet = int(user.bet)
  while True:
    if m == "skip":
      break
    # Asks if the user is hitting or standing
    hitOrStand = (input("Would you like to hit or stand?: ")).lower()
    if hitOrStand == "hit":
      k = user.hit(cred)
      if result(k,user.bet,cred)[0] == "m":
        cred = result(k,user.bet,cred)[1]
        t = "k"
        break
    elif hitOrStand == "stand":
      user.stand()
      t = "k"
      break
    else:
      print("Hey, that's not an option!")
  if user.turn == 5:
    print("Lost on amount of turns")
    t = "k"
    break
  if t == "k":
    times +=1
    if cred <= 0:
      print("You lost all your credits!")
      sys.exit("Womp Womp")
    while True:
      again = input("Would you like to play again?(y/n): ")
      if again == "y":
        print(f"You have {cred} credits")
        del user
        m = "skip"
        break
      elif again == "n":
        print(f"You have {cred} credits")
        print(
            f"{streak['win']} win(s) {streak['draw']} draw(s) ,{streak['draw']} loss(es)")
        print("Thanks for playing!")
        sys.exit()
