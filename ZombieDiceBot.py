
print("Mohd.Jawwad Ali Farooqui, USN:1AY24AI070, SEC:O")

import random

DICE_POOL = {
    'green': ['brain', 'brain', 'brain', 'footsteps', 'footsteps', 'shotgun'],
    'yellow': ['brain', 'brain', 'footsteps', 'footsteps', 'shotgun', 'shotgun'],
    'red': ['brain', 'footsteps', 'footsteps', 'shotgun', 'shotgun', 'shotgun']
}

ALL_DICE = ['green'] * 6 + ['yellow'] * 4 + ['red'] * 3

def roll_die(color):
    return random.choice(DICE_POOL[color])

def draw_dice(dice_pool, n=3):
    return [dice_pool.pop(random.randint(0, len(dice_pool)-1)) for _ in range(min(n, len(dice_pool)))]

def zombie_bot_turn(name="Bot"):
    dice_pool = ALL_DICE.copy()
    random.shuffle(dice_pool)

    brains = 0
    shotguns = 0
    footprints = []

    print(f"\n{name}'s turn begins!")
    while True:
        needed = 3 - len(footprints)
        drawn_dice = footprints + draw_dice(dice_pool, needed)
        footprints = []

        print(f"\nRolling: {drawn_dice}")
        roll_results = [roll_die(color) for color in drawn_dice]

        for i, result in enumerate(roll_results):
            print(f"Rolled a {drawn_dice[i]} die: {result}")
            if result == 'brain':
                brains += 1
            elif result == 'shotgun':
                shotguns += 1
            else:
                footprints.append(drawn_dice[i])

        print(f"Current: {brains} brains, {shotguns} shotguns")

        if shotguns >= 3:
            print(f"{name} got blasted! Turn over. No brains this round.")
            return 0  # Lost all collected brains this turn

        if brains >= 2 or shotguns == 2:
            print(f"{name} decides to stop and bank {brains} brains.")
            return brains

def simulate_game():
    scores = {'Bot A': 0, 'Bot B': 0}
    turn = 0
    players = list(scores.keys())

    while max(scores.values()) < 13:
        player = players[turn % 2]
        gained = zombie_bot_turn(player)
        scores[player] += gained
        print(f"{player} total score: {scores[player]}")
        turn += 1

    winner = max(scores, key=scores.get)
    print(f"\n🏆 {winner} wins with {scores[winner]} brains!")

if __name__ == "__main__":
    simulate_game()
