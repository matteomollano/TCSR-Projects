#include <iostream>
#include <cstdlib>
#include <time.h>
using namespace std;
#include "rpsls.h"

Computer::Computer() {
    setChoices();
    setChoice("");
    setWins(0);
}

void Computer::setChoices() {
    this->choices.clear();
    this->choices.push_back("rock"); // append("rock")
    this->choices.push_back("paper");
    this->choices.push_back("scissors");
    this->choices.push_back("lizard");
    this->choices.push_back("spock");
}

vector<string> Computer::getChoices() {
    return this->choices;
}

void Computer::setChoice(string randomChoice) {
    this->choice = randomChoice;
}

string Computer::getChoice() {
    return this->choice;
}

string Computer::getRandomChoice() {
    vector<string> choices = getChoices(); // choices = ["rock", "paper", "scissors", "lizard", "spock"]

    int randomValue = rand() % choices.size(); // choices.size() == 5

    string randomChoice = choices[randomValue];

    return randomChoice;
}

void Computer::setWins(int wins) {
    this->wins = wins;
}

int Computer::getWins() {
    return this->wins;
}

void Computer::updateWins() {
    this->wins += 1;
}

void Computer::displayChoices() {
    vector<string> choices = this->getChoices();
    cout << "Choices vector: ";
    for (int i = 0; i < choices.size(); i++) {
        if (i == 0) {
            cout << "{";
        }

        if (i < choices.size() - 1) {
            cout << "\"" << choices[i] << "\"" << ", "; 
        }
        else {
            cout << "\"" << choices[i] << "\"" << "}" << endl;
        }
    }
}