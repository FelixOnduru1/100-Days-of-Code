print("Welcome to the Secret auction program.")

bidding_status = True
bids = {}
max_bid = 0
max_bidder = ""
while bidding_status:
    bidder = input("What is your name?\n")
    bid = int(input("What's your bid? $"))
    bids[bidder] = bid

    more_bidders = input("Are there any more bidders? Type 'yes' or 'no':")
    if more_bidders == "no":
        bidding_status = False
        for bidder in bids:
            if bids[bidder] > max_bid:
                max_bid = bids[bidder]
                max_bidder = bidder
        print(f"{max_bidder} won the auction. The winning bid was ${max_bid}.")
