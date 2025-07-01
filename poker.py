from classes import Deck, Player, Chip, ChipStack
from rules import evaluate_hand, HAND_RANKINGS

def get_chip_bet(player_stack):
    print("\nAvaliable Chips:")
    print(player_stack)
    
    while True:
        color = input("Chip color (White/Red/Green/Blue/Black/Purple/Yellow): ").capitalize()
        try:
            quantity = int(input("Quantity: "))
            removed_chips = player_stack.remove_chips(color, quantity)
            bet_value = sum(chip.value for chip in removed_chips)
            print(f"Bet ${bet_value} {color} chips")
            return removed_chips
        except ValueError as e:
            print(f"Error: {e}. Try again.")

def main():
    player = Player.create_player()
    deck = Deck()
    pot = ChipStack()

    player.hand = deck.deal(2)
    table_cards = deck.deal(5)  

    revealed_cards = []

    betting_rounds = [
        ("Initial bet", 0),  
        ("Flop", 3),      
        ("Turn", 1),      
        ("River", 1)      
    ]

    for round_name, new_cards_count in betting_rounds:
        print(f"\n=== {round_name} ===")
        
        if new_cards_count > 0:
            start_idx = len(revealed_cards)
            end_idx = start_idx + new_cards_count
            revealed_cards.extend(table_cards[start_idx:end_idx])

        if round_name == "Initial bet":
            print("Hand:")
            for card in player.hand:
                print(card)
        
        if revealed_cards:
            print("\nCards on table:")
            for i, card in enumerate(revealed_cards):
                print(f"{card}")
        
        bet_chips = get_chip_bet(player.stack)
        if bet_chips:
            for chip in bet_chips:
                pot.add_chips(chip.color, 1)
            print(f"Total no pote: ${pot.total_value}")

    all_cards = player.hand + table_cards
    result = evaluate_hand(all_cards)
    
    print("\n=== Showdown ===")
    print("Final Hand:")
    for card in player.hand:
        print(card)
    print("\nCards on table:")
    for card in table_cards:
        print(card)
    print(f"\nBest hand: {result[0]} (value: {result[1]})")
    print(f"You won ${pot.total_value}!")

if __name__ == "__main__":
    main()