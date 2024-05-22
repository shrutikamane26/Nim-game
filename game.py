def print_piles(piles):
    print("Current piles:")
    for i, pile in enumerate(piles):
        print(f"Pile {i + 1}: {pile}")
    print()

def get_valid_move(piles):
    while True:
        try:
            pile_num = int(input("Enter the pile number: "))
            if pile_num < 1 or pile_num > len(piles):
                raise ValueError
            num_stones = int(input(f"Enter the number of stones to remove from pile {pile_num}: "))
            if num_stones < 1 or num_stones > piles[pile_num - 1]:
                raise ValueError
            return pile_num - 1, num_stones
        except ValueError:
            print("Invalid input! Please enter a valid pile number and number of stones.")

def is_game_over(piles):
    return all(pile == 0 for pile in piles)

def main():
    piles = [3, 4, 5]  # Initial number of stones in each pile
    
    print("Welcome to Nim!")
    
    while not is_game_over(piles):
        print_piles(piles)
        
        player = "Player 1" if sum(piles) % 2 == 0 else "Player 2"
        print(f"{player}'s turn:")
        
        pile_num, num_stones = get_valid_move(piles)
        
        piles[pile_num] -= num_stones
        
        print(f"{player} removes {num_stones} stones from pile {pile_num + 1}.\n")
    
    winner = "Player 1" if sum(piles) % 2 == 0 else "Player 2"
    print(f"{winner} wins!")

if __name__ == '__main__':
    main()
