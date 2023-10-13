'''
Created on 2023/10/13

@author: t21cs038
'''
import random

def get_player_choice():
    while True:
        player_choice = input("じゃんけん！（1: グー, 2: チョキ, 3: パー）: ")
        if player_choice in ['1', '2', '3']:
            return int(player_choice)
        else:
            print("無効な選択です。1から3の数字を選んでください。")

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(player, computer):
    if player == computer:
        return "引き分け"
    elif (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
        return "プレイヤーの勝ち"
    else:
        return "コンピュータの勝ち"

while True:
    player = get_player_choice()
    computer = get_computer_choice()

    print(f"プレイヤー: {player}, コンピュータ: {computer}")

    result = determine_winner(player, computer)
    print(result)

    play_again = input("もう一度プレイしますか？ (y/n): ")
    if play_again.lower() != 'y':
        break
