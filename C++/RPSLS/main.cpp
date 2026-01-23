#include <iostream>
using namespace std;
#include "rpsls.h"

int main() {
    // initialize the random number generator
    srand(time(0));
    cout << "Welcome to Rock, Paper, Scissors, Lizard, Spock!" << endl << endl;

    // create the three objects for the game
    Computer computer;
    Player player;
    Game game;

    string computerChoice;
    string playerChoice;
    int round = 1;

    while (true) {

        // display the round number
        cout << "Round " << round << endl;

        // get a random choice for the computer
        computerChoice = computer.getRandomChoice();
        // update the computer's choice variable
        computer.setChoice(computerChoice);

        // ask the user for a choice
        playerChoice = player.getUserChoice();
        // update the player's choice variable
        player.setChoice(playerChoice);

        // determine the winner of the round
        game.determineWinner(computer, player);
        // display total wins for each player
        game.displayTotalWins(computer, player);

        // go to next round
        round++;
    }
}