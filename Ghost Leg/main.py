import random
#create a board that user had input
def create_board(players, ladders):
    board = []
    for i in range(ladders):
        row = ["{0:02d}".format((i * players + j + 1)) for j in range(players)]
        board.append(row)
    return board
#Print out the bored and players
def print_board(board, players):
    player_labels = " | ".join([f"P{i+1}" for i in range(players)])
    print(f"| {player_labels} |")
    for row in board:
        row_with_walls = " | ".join(row)
        print(f"| {row_with_walls} |")
#Enter a number to update the board
def update_board(board, players):
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
#caculate the result
def calculate_results(board, players):
    positions = list(range(players))
    for row in board:
        for i in range(len(row) - 1):
            if row[i] == "_" and row[i + 1] != "_":
                positions[i], positions[i + 1] = positions[i + 1], positions[i]
    return {f"P{i+1}": f"P{positions.index(i) + 1}" for i in range(players)}
#Show the result
def display_results(results):
    print("\nResults:")
    for start, end in results.items():
        print(f"{start} -> {end}")
#main()
def ghost_leg_game():
    players = int(input("Enter number of players: "))
    ladders = int(input("Enter number of ladders: "))

    board = create_board(players, ladders)
    print_board(board, players)
    update_board(board, players)
    print("\nUpdated board:")
    print_board(board, players)

    results = calculate_results(board, players)
    display_results(results)

ghost_leg_game()
