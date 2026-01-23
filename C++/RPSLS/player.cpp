#include <iostream>
#include <set>
#include <sstream>
using namespace std;
#include "rpsls.h"

Player::Player() {
    setChoice(""); // player's choice is empty before game begins
    setWins(0); // set's the player's wins to 0 before game begins
}

void Player::setChoice(string userChoice) {
    this->choice = userChoice;
}

string Player::getChoice() {
    return this->choice;
}

string Player::getUserChoice() {

    set<string> validChoices = {"rock", "paper", "scissors", "lizard", "spock"};
    string userChoice;

    while (true) {
        cout << "Select your object (rock, paper, scissors, lizard, or spock)" << endl;
        cout << "Your choice: ";

        // read the entire line
        string userInput;
        getline(cin, userInput);

        // use a stringstream to extract the first word
        stringstream ss(userInput);
        ss >> userChoice;

        for (char& c : userChoice) {
            c = tolower(c);
        }

        if (validChoices.count(userChoice) > 0) {
            // Valid input
            break;
        } 
        else {
            cout << "Invalid selection. Please choose from rock, paper, scissors, lizard, or spock." << endl << endl;
        }
    }

    return userChoice;
}

void Player::setWins(int wins) {
    this->wins = wins;
}

int Player::getWins() {
    return this->wins;
}

void Player::updateWins() {
    this->wins += 1;
}