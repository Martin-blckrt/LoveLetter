from src.Game import initGame, computePoints


def main():
    play_again = True

    while play_again:
        """
        mis a part pour faciliter le debug
        
        player1_name = input("Player 1 , enter your name\n")
        player2_name = input("Player 2 , enter your name\n")
        """
        player1_name = "Hooman"
        player2_name = "Masheen"

        game = initGame(player1_name, player2_name)

        while game.player1.points < 6 and game.player2.points < 6:
            game.initRound()

            while game.endRound() and game.deck:

                print(f"\nLongueur du deck : {len(game.deck)-1} \n")
                print(f"\n\nTime for {player1_name} ({game.player1.gender}) to play!")

                game.player1.playTurn(game.deck)

                if game.player2.isAlive and game.player1.isAlive and game.deck:

                    print(f"\n\nTime for {player2_name}({game.player2.gender}) to play!")
                    game.player2.playTurn(game.deck)

                    # pour IA
                    # game.player2.playAiTurn(game.deck, game.isolatedCards)

            if not game.deck:
                game.player1.showdown()

            computePoints(game.player1)
            computePoints(game.player2)

        if game.player1.points >= 6:

            print(f"{player1_name} WINS THE GAME !")
            play_again = input("\nDo you want to play again ? (True/False)\n")

        elif game.player2.points >= 6:

            print(f"{player2_name} WINS THE GAME !")
            play_again = input("\nDo you want to play again ? (True/False)\n")

        else:
            print('DRAW')
            play_again = input("\nDo you want to play again ? (True/False)\n")


if __name__ == "__main__":
    main()
