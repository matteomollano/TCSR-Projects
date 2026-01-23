#include <iostream>
using namespace std;
#include "include/casino.h"

void Game::evaluateBet(Computer &computer, Player &player) {
    // get the Computer's number and color
    int computerNumber = computer.getNumber();
    char computerColor = computer.getColor();

    // get the Player's choice
    int playerChoice = player.getChoice();
    char playerColor = player.getColor();
    int betAmount = player.betAmount();

    if (playerChoice == 1) { // user chooses a single number
        int playerNumber = player.getNumber();

        // Player wins bet
        if (playerNumber == computerNumber && playerColor == computerColor) {
            int moneyToAdd = betAmount * 38;
            player.addMoney(moneyToAdd);
            cout << "You won the bet and earned $" << moneyToAdd << endl;
            cout << "Your total money is now $" << player.getMoney() << endl << endl;
        }
        else { // Player loses bet
            player.subMoney(betAmount);
            cout << "You lost the bet and lost $" << betAmount << endl;
            cout << "Your total money is now $" << player.getMoney() << endl << endl;
        }
    }
    else if (playerChoice == 2) { // user chooses a number range
        vector<int> playerRange = player.getNumberRange();

        int lowerBound = playerRange[0];
        int upperBound = playerRange[1];

        // Player wins the bet
        if ( (computerNumber >= lowerBound && computerNumber <= upperBound)
            && (playerColor == computerColor)) {
                // 2 numbers = 22
                // 3 numbers = 16
                // 4 numbers = 12
                // 6 numbers = 10

                int multiplier = 0;
                int difference = upperBound - lowerBound;

                if (difference == 2) {
                    multiplier = 22;
                }
                else if (difference == 3) {
                    multiplier = 16;
                }
                else if (difference == 4) {
                    multiplier = 12;
                }
                else if (difference == 6) {
                    multiplier = 10;
                }

                int moneyToAdd = betAmount * multiplier;
                player.addMoney(moneyToAdd);
                cout << "You won the bet and earned $" << moneyToAdd << endl;
                cout << "Your total money is now $" << player.getMoney() << endl << endl;
        }
        else { // Player loses the bet
            player.subMoney(betAmount);
            cout << "You lost the bet and lost $" << betAmount << endl;
            cout << "Your total money is now $" << player.getMoney() << endl << endl;
        }
    }
    else { // user chooses parity
        string playerParity = player.getParity();
        string computerParity;

        if (computerNumber % 2 == 0) {
            computerParity = "even";
        }
        else {
            computerParity = "odd";
        }

        // Player wins bet
        if (playerParity == computerParity && playerColor == computerColor) {
            int moneyToAdd = betAmount * 4;
            player.addMoney(moneyToAdd);
            cout << "You won the bet and earned $" << moneyToAdd << endl;
            cout << "Your total money is now $" << player.getMoney() << endl << endl;
        }
        else { // Player loses bet
            player.subMoney(betAmount);
            cout << "You lost the bet and lost $" << betAmount << endl;
            cout << "Your total money is now $" << player.getMoney() << endl << endl;
        }
    }
}

bool Game::betAgain() {
    cout << "Would you like to bet again? (y/n) ";

    string choice;

    while (choice != "y" && choice != "n") {
        getline(cin, choice);
        // convert the word to all lowercase
        transform(choice.begin(), choice.end(), choice.begin(), ::tolower);
        if (choice != "y" && choice != "n") {
            cout << "Invalid choice. Please enter y or n: ";
        }
    }

    if (choice == "y") {
        return true;
    }
    else {
        return false;
    }
}