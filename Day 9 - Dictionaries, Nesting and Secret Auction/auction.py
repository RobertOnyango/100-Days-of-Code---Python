# A program that simulates a Blind Auction between 2 or more parties
import art

#Logo
print(art.logo)

# Bids dictionary
bids = {}
#Variable to hold new bid state
new_bid = True
# Largest bid
largest_bid = 0
# Largest bidder
largest_bidder = ""

while new_bid:
    # TODO-1: Ask the user for input
    player_name = input("What is your name?")
    player_bid = int(input("What's your bid in USD? $"))

    # TODO-2: Save data into dictionary {name: price}
    bids[player_name] = player_bid

    # TODO-3: Whether if new bids need to be added
    bid_status = input("Are there any other bidders? Type 'yes' or no\n").lower()

    if bid_status == "yes":
        # clear screen
        print("\n" * 20)
    # End taking bidders
    elif bid_status == "no":
        new_bid = False
        # TODO-4: Compare bids in dictionary
        # Checkout max() function
        for key in bids:
            if bids[key] > largest_bid:
                # Store largest bid in variable
                largest_bid = bids[key]
                largest_bidder = key

        print(f"The winner is {largest_bidder} with a bid of ${largest_bid}.")
    else:
        print("Incorrect input.\n")

