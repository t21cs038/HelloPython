'''
Created on 2023/10/13

@author: t21cs038
'''


import random

def janken_choice():
    return random.randint(0, 2)

def main():
    num_players = int(input("プレイヤーの人数を入力してください（3人以上）: "))
    if num_players < 3:
        print("3人以上のプレイヤーが必要です。")
        return

    player_wins = [0] * num_players

    while True:
        choices = [janken_choice() for _ in range(num_players)]
        print("各プレイヤーの選択:", choices)

        winners = []

        for i in range(num_players):
            for j in range(i + 1, num_players):
                if (choices[i] - choices[j]) % 3 == 1:
                    player_wins[i] += 1
                    winners.append(i)
                elif (choices[j] - choices[i]) % 3 == 1:
                    player_wins[j] += 1
                    winners.append(j)

        for i in range(num_players):
            if player_wins[i] >= 3:
                print(f"プレイヤー {i} が3回勝利しました！")
                return

        if winners:
            print("今回の勝者:", winners)

if __name__ == "__main__":
    main()

