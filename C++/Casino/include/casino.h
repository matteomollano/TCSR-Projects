#include <vector>

class Computer {
    private:
        int number; // randomly generated value
        char color; // red or black
    public:
        Computer();
        void update();
        void display();

        int getNumber();
        void setNumber(int number);

        char getColor();
        void setColor(char color);

        int generateValue();
        char generateColor();
};

class Player {
    private:
        char color;
        int money;
        /*
            a) one number -> integer
            b) number ranges -> vector of two integers (upper and lower bounds)
            c) even or odd -> string
        */
       int choice; // store the user's betting choice as a number (1, 2, or 3)
       int number;
       vector<int> numberRange;
       string parity;

    public:
        Player();
        void update();
        void display();

        char getColor();
        void setColor(char color);

        int getMoney();
        void setMoney(int money);
        void addMoney(int money);
        void subMoney(int money);

        int getChoice();
        void setChoice(int choice);

        int getNumber();
        void setNumber(int number);

        vector<int> getNumberRange();
        void setNumberRange(vector<int> numberRange);
        void printList(vector<int> list);

        string getParity();
        void setParity(string parity);

        // user-input functions for three game options
        int bettingPrompt();
        char getUserColor();
        int getSingleNumber();
        vector<int> getTwoNumbers();
        string getOddOrEven();
        int betAmount();
};

// Game
class Game {
    private:

    public:
        void evaluateBet(Computer &computer, Player &player);
        bool betAgain();
};