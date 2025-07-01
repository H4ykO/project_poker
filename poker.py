from classes import Deck, Player, Chip, ChipStack
from rules import evaluate_hand, HAND_RANKINGS

def get_chip_bet(player_stack):
    print("\nFichas disponíveis:")
    print(player_stack)
    
    while True:
        color = input("Cor da ficha (White/Red/Green/Blue/Black/Purple/Yellow): ").capitalize()
        try:
            quantity = int(input("Quantidade: "))
            removed_chips = player_stack.remove_chips(color, quantity)
            bet_value = sum(chip.value for chip in removed_chips)
            print(f"Apostou ${bet_value} em fichas {color}")
            return removed_chips
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")

def main():
    player = Player("Jogador", {'White': 10, 'Red': 5, 'Green': 2})
    deck = Deck()
    pot = ChipStack()

    player.hand = deck.deal(2)
    table_cards = deck.deal(5)  

    revealed_cards = []

    betting_rounds = [
        ("Pré-flop", 0),  
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

        if round_name == "Pré-flop":
            print("Sua mão:")
            for card in player.hand:
                print(card)
        
        if revealed_cards:
            print("\nCartas na mesa:")
            for i, card in enumerate(revealed_cards):
                print(f"{card}")
        
        bet_chips = get_chip_bet(player.stack)
        if bet_chips:
            for chip in bet_chips:
                pot.add_chips(chip.color, 1)
            print(f"Total no pote: ${pot.total_value}")

    all_cards = player.hand + table_cards
    result = evaluate_hand(all_cards)
    
    print("\n=== Resultado Final ===")
    print("Sua mão final:")
    for card in player.hand:
        print(card)
    print("\nCartas na mesa:")
    for card in table_cards:
        print(card)
    print(f"\nMelhor mão: {result[0]} (valor: {result[1]})")
    print(f"Você ganhou ${pot.total_value}!")

if __name__ == "__main__":
    main()