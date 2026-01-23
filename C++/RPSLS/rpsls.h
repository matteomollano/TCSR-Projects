#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Computer {
    private:
        // class attributes
        vector<string> choices; // choices = ["rock", "paper", "scissors", "lizard", "spock"]
        string choice; // "rock"
        int wins; // counts the number of times the computer wins

    public:
        // Constructor
        Computer();

        // getter and setter methods
        void setChoices(); // generate choices list
        vector<string> getChoices();
        
        void setChoice(string randomChoice); // update choice class variable
        string getChoice();

        void setWins(int wins);
        int getWins();

        string getRandomChoice();
        void updateWins();
        void displayChoices();
};


class Player {
    private:
        string choice;
        int wins; // counts the number of times the player wins

    public:
        // Constructor
        Player();

        // getter and setter methods
        void setChoice(string userChoice);
        string getChoice();

        void setWins(int wins);
        int getWins();

        void updateWins();
        string getUserChoice();       
};

class Game {
    private:
        unordered_map< string, vector<string> > winningChoices = {
            {"rock", {"scissors", "lizard"}},
            {"scissors", {"paper", "lizard"}},
            {"paper", {"rock", "spock"}},
            {"lizard", {"spock", "paper"}},
            {"spock", {"scissors", "rock"}}
        };
    public:
        void determineWinner(Computer &computer, Player &player);
        void displayTotalWins(Computer &computer, Player &player);
};