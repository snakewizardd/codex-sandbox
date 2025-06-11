#!/usr/bin/env python3
"""
Codex, let's make a game!
Create a simple text-based game where:
1. The player is in a maze trying to find treasure
2. They can move with commands: north, south, east, west
3. There should be at least one trap and one treasure
4. Make it fun and surprising!

Bonus: Add something unexpected that makes me smile
"""

import random

def main():
    print("Welcome to the Codex Dungeon!")
    print("Type north, south, east or west to move.\n")

    size = 5  # 5x5 playing field
    player = [0, 0]

    # Randomly place trap and treasure, avoiding the starting cell
    cells = [(x, y) for x in range(size) for y in range(size) if (x, y) != tuple(player)]
    trap = random.choice(cells)
    cells.remove(trap)
    treasure = random.choice(cells)

    def draw_map() -> None:
        for y in range(size):
            row = []
            for x in range(size):
                if [x, y] == player:
                    row.append("P")
                else:
                    row.append(".")
            print(" ".join(row))

    def surprise() -> None:
        if random.random() < 0.1:  # 10% chance each turn
            print(random.choice([
                "A friendly gnome hands you a cookie and scurries away!",
                "You hear distant chiptune music echoing in the halls...",
                "A dancing ASCII unicorn prances by: \u2728 \uD83E\uDD84 \u2728",
            ]))

    while True:
        draw_map()
        move = input("Where to? ").strip().lower()

        if move == "quit":
            print("Thanks for playing!")
            break
        elif move == "dance":
            print("You bust out some moves: (\u30c4)/")
            continue
        elif move == "north":
            player[1] = max(0, player[1] - 1)
        elif move == "south":
            player[1] = min(size - 1, player[1] + 1)
        elif move == "west":
            player[0] = max(0, player[0] - 1)
        elif move == "east":
            player[0] = min(size - 1, player[0] + 1)
        else:
            print("I don't understand that.")
            continue

        if tuple(player) == trap:
            print("Oh no! You stepped on a trap door and fell into the abyss!")
            break
        if tuple(player) == treasure:
            print("You found the treasure chest overflowing with coins! \U0001f4b0")
            break

        surprise()
    
if __name__ == "__main__":
    main()