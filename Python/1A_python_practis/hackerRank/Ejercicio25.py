from collections import Counter

def minion_game(txt):
    vowels = "AEIOU"
    # your code goes here
    length = len(txt)
    score = Counter()
    for i, ch in enumerate(txt):
        points = length - i
        score[ch in vowels] += points
    print(score)

    if (kevin := score[True]) > (stuart := score[False]):
        print(f"Kevin {kevin}")
    elif stuart > kevin:
        print(f"Stuart {stuart}")
    else:
        print("Draw")

minion_game("BANANA")
minion_game("CURANDETA")
minion_game("MAMELOPIPE")
