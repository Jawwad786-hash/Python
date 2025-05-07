print("Mohd Jawwad Ali Farooqui,USN:1AY24AI070,SEC:O")
import random
NUMBER_OF_EXPERIMENTS = 10000
FLIPS_PER_EXPERIMENT = 100
STREAK_LENGTH = 6
def has_streak(coin_flips, streak_length):
    count = 1
    for i in range(1, len(coin_flips)):
        if coin_flips[i] == coin_flips[i - 1]:
            count += 1
            if count == streak_length:
                return True
        else:
            count = 1
    return False
def simulate():
    streaks_found = 0
    for _ in range(NUMBER_OF_EXPERIMENTS):
        flips = ['H' if random.randint(0, 1) == 1 else 'T' for _ in range(FLIPS_PER_EXPERIMENT)]
        if has_streak(flips, STREAK_LENGTH):
            streaks_found += 1
    percentage = (streaks_found / NUMBER_OF_EXPERIMENTS) * 100
    print(f'Chance of streak: {percentage:.2f}%')
simulate()
