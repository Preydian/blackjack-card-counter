# Dictionary to get the value of a card
import cv2

card_values = {
    '1': 1,
    '2': 1,
    '3': 1,
    '4': 1,
    '5': 1,
    '6': 1,
    '7': 0,
    '8': 0,
    '9': 0,
    '10': -1,
    'J': -1,
    'Q': -1,
    'K': -1,
    'A': -1,
}

names = ["Ah", "Kh", "Qh", "Jh", "10h", "9h", "8h", "7h", "6h", "5h", "4h", "3h", "2h",
         "Ad", "Kd", "Qd", "Jd", "10d", "9d", "8d", "7d", "6d", "5d", "4d", "3d", "2d",
         "Ac", "Kc", "Qc", "Jc", "10c", "9c", "8c", "7c", "6c", "5c", "4c", "3c", "2c",
         "As", "Ks", "Qs", "Js", "10s", "9s", "8s", "7s", "6s", "5s", "4s", "3s", "2s"]

# Dictionary holding all the cards that have already been seen
# Maps a tuple representation of a card (rank, suit), to a boolean value which is always True
#
# Example
# - SEEN_CARDS = {(Jack, Hearts)} this means the Jack of Hearts has already been seen and the count has been updated
SEEN_CARDS = {}

# Dictionary holding all the cards detected in the last frame
# Maps a tuple representation of a card (rank, suit), to a boolean value which is always True
#
# Example
# - LAST_FRAME_CARDS = {(Jack, Hearts)} this means the Jack of Hearts has was detected in the last frame
LAST_FRAME_CARDS = {}

# Represents the last seen card, used to stop print statements in update_count()
LAST_CARD = (None, None)

# The number of cards in the last image, used to stop print statements in update_count()
LAST_NUM_CARDS = 0

# The number of decks currently in play
NUM_OF_DECKS_REMAINING = 1


def update_count(detections, running_count, true_count, number_of_cards_in_image):
    """
    Updates the black jack count based on the rank of the card.

    Parameters:
        detections (str): All the detections in a frame
        running_count (int): The current running count.
        true_count (int): The current true count.
        number_of_cards_in_image (int): The total number of cards in the image.

    Returns:
        int: The new count after updating.
    """

    global LAST_CARD
    global LAST_NUM_CARDS
    global LAST_FRAME_CARDS

    first_frame = LAST_FRAME_CARDS == {}
    for card in detections:
        rank, suit = names[int(card)][:-1], names[int(card)][-1]

        if first_frame:  # Check if this is the first time a card is being detected
            LAST_FRAME_CARDS[(rank, suit)] = 1
            continue

        # If the card hasn't been processed before, and it was in the last frame
        if (rank, suit) not in SEEN_CARDS and (rank, suit) in LAST_FRAME_CARDS:
            SEEN_CARDS[(rank, suit)] = True
            running_count += card_values[rank]
            true_count = round(running_count / NUM_OF_DECKS_REMAINING, 1)
            LAST_CARD = (rank, suit)
            LAST_NUM_CARDS = number_of_cards_in_image

            print(f"Rank: {rank}, Suit: {suit}")
            print(f"Running count: {running_count}")
            print(f"True count: {true_count}")

    if not first_frame:
        LAST_FRAME_CARDS = {}

    return running_count, true_count


def reset_cards():
    """
     Resets the dictionary of seen cards and the variable holding the most recently seen card
    """
    global SEEN_CARDS, LAST_CARD, LAST_NUM_CARDS
    SEEN_CARDS = {}
    LAST_CARD = None
    LAST_NUM_CARDS = 0

    print("Resetting counts back to 0")


def set_decks_remaining(number_of_decks):
    """
    Sets the remaining number of decks currently in play
    """
    global NUM_OF_DECKS_REMAINING
    NUM_OF_DECKS_REMAINING = number_of_decks

    print(f"Setting number of decks to: {number_of_decks}")
