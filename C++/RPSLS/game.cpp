#include <iostream>
using namespace std;
#include "rpsls.h"

void Game::determineWinner(Computer &computer, Player &player) {
    unordered_map< string, vector<string> > winningChoices = this->winningChoices;

    string computerChoice = computer.getChoice();
    string playerChoice = player.getChoice();

    if (computerChoice == playerChoice) {
        cout << "Computer played " << computerChoice << " and you played " << playerChoice << endl;
        cout << "It's a tie!" << endl << endl;
    }
    else {
        // use the key (computerChoice) to get its corresponding value (vector of options it wins against)
        vector<string> options = winningChoices[computerChoice];
        bool found = false;

        // loop through the options vector, and see if it contains the player's choice
        for (string& option : options) {
            if (option == playerChoice) {
                found = true;
                break;
            }
        }

        if (found == true) {
            cout << "Computer played " << computerChoice << " and you played " << playerChoice << endl;
            cout << "Computer wins the round!" << endl << endl;
            computer.updateWins();
        }
        else {
            cout << "Computer played " << computerChoice << " and you played " << playerChoice << endl;
            cout << "You win the round!" << endl << endl;
            player.updateWins();
        }
    }
}

void Game::displayTotalWins(Computer &computer, Player &player) {
    int computerWins = computer.getWins();
    int playerWins = player.getWins();

    cout << "Total Wins:" << endl;
    cout << "Computer Wins: " << computerWins << endl;
    cout << "Player Wins: " << playerWins << endl << endl << endl;
}