#create a dictonary to hold all the bidders
all_bidders = {}
keep_playing = "yes"
#while loop to keep the game going
while keep_playing == "yes":
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))
    #add the name and the bid to the all_bidders dictionary
    all_bidders[name] = bid
    keep_playing = input("Any more people: ").lower()

print(f"all_bidders has {all_bidders}")
#find the highest bid from all the bidders
highest_bid = 0
highest_bidder = ""
for name in all_bidders:
    bid = all_bidders[name]
    if bid > highest_bid:
        highest_bid = bid
        print(f"Highest bidder is {name}")
        highest_bidder = name
print(f"The winner is {highest_bidder} with a bid of {highest_bid}")

