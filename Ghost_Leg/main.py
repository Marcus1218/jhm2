import random
from typing import List, Dict

def create_board(players: int, ladders: int) -> List[List[str]]:
    board = []
    for i in range(ladders):
        row = ["{0:02d}".format((i * players + j + 1)) for j in range(players)]
        board.append(row)
    return board

def print_board(board: List[List[str]], players: int) -> None:
    player_labels = " | ".join([f"P{i+1}" for i in range(players)])
    print(f"| {player_labels} |")
    for row in board:
        row_with_walls = " | ".join(row)
        print(f"| {row_with_walls} |")

def update_board(board: List[List[str]]) -> None:
    selected_numbers = set()
    while True:
        update = input("Enter a number to update the board (or 'n' to stop): ").strip()
        if update.lower() == 'n':
            break
        elif update.isdigit():
            found = False
            for row in board:
                if update in row and update not in selected_numbers:
                    index = row.index(update)
                    row[index] = "_"
                    found = True
                    selected_numbers.add(update)
                    if index > 0:
                        selected_numbers.add(row[index - 1])
                    if index < len(row) - 1:
                        selected_numbers.add(row[index + 1])
                    break
            if not found:
                print("Invalid input or number already selected. Try again.")
        else:
            print("Invalid input. Try again.")

def calculate_results(board: List[List[str]], players: int) -> Dict[str, str]:
    positions = list(range(players))
    for row in board:
        for i in range(len(row) - 1):
            if row[i] == "_" and row[i + 1] != "_":
                positions[i], positions[i + 1] = positions[i + 1], positions[i]
    return {f"P{i+1}": f"P{positions.index(i) + 1}" for i in range(players)}

def display_results(results: Dict[str, str]) -> None:
    print("\nResults:")
    for start, end in results.items():
        print(f"{start} -> {end}")

def ghost_leg_game() -> None:
    try:
        players = int(input("Enter number of players: "))
        ladders = int(input("Enter number of ladders: "))
    except ValueError:
        print("Invalid input. Please enter integers for players and ladders.")
        return

    board = create_board(players, ladders)
    print_board(board, players)
    update_board(board)
    print("\nUpdated board:")
    print_board(board, players)

    results = calculate_results(board, players)
    display_results(results)

if __name__ == "__main__":
    ghost_leg_game()