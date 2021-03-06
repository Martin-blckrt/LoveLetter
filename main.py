from src.Game import *


def main():

    play_again = True

    while play_again:
        player1_name = input("Player 1 , enter your name\n")
        player2_name = input("Player 2 , enter your name\n")
        game = initGame(player1_name, player2_name)

        while game.player1.points < 6 and game.player2.points < 6:
            game.initRound()

            while game.endRound() and game.deck:
                print(f"\n\nTime for {player1_name} ({game.player1.gender}) to play!")
                game.player1.playTurn(game.deck)

                if game.player2.isAlive and game.deck:
                    print(f"\n\nTime for {player2_name}({game.player2.gender}) to play!")
                    game.player2.playTurn(game.deck)

            if not game.deck:
                if game.player1.compare(game.player2) == 0:
                    game.player2.hasWon = True
                    print(f"{player2_name} wins the round !")
                elif game.player1.compare(game.player2) == 1:
                    game.player1.hasWon = True
                    print(f"{player1_name} wins the round !")
                else:
                    game.player1.hasWon = game.player2.hasWon = True
                    print("Tie")

            computePoints(game.player1)
            computePoints(game.player2)

        if game.player1.points == 6:
            print(f"{player1_name} wins the game !")
            play_again = input("Do you want to play again ? (True/False)")

        elif game.player2.points == 6:
            print(f"{player2_name} wins the game !")
            play_again = input("Do you want to play again ? (True/False)")

