#include <iostream>
using namespace std;
#include "include/casino.h"

Player::Player() {
    setNumber(0);
    setNumberRange({0,0});
    setParity("");
    setMoney(2500);
    setChoice(0);
}

void Player::update() {
    int choice = this->getChoice();

    if (choice == 1) {
        setNumber(this->getSingleNumber());
    }
    else if (choice == 2) {
        setNumberRange(this->getTwoNumbers());
    }
    else {
        setParity(this->getOddOrEven());
    }
}

void Player::display() {
    cout << "Player's color: " << this->getColor() << endl;
    cout << "Player's number: " << this->getNumber() << endl;
    cout << "Player's number range: ";
    this->printList(this->getNumberRange());
    cout << "Player's parity: " << this->getParity() << endl;
}

char Player::getColor() {
    return this->color;
}

void Player::setColor(char color) {
    this->color = color;
}

int Player::getMoney() {
    return this->money;
}

void Player::setMoney(int money) {
    this->money = money;
}

void Player::addMoney(int money) {
    this->money += money;
}

void Player::subMoney(int money) {
    this->money -= money;
}

int Player::getChoice() {
    return this->choice;
}

void Player::setChoice(int choice) {
    this->choice = choice;
}

int Player::getNumber() {
    return this->number;
}

void Player::setNumber(int number) {
    this->number = number;
}

vector<int> Player::getNumberRange() {
    return this->numberRange;
}

void Player::setNumberRange(vector<int> numberRange) {
    this->numberRange = numberRange;
}

string Player::getParity() {
    return this->parity;
}

void Player::setParity(string parity) {
    this->parity = parity;
}

int Player::bettingPrompt() {
    cout << "Choose between the following options: " << endl;
    cout << "\t1. Single Number" << endl;
    cout << "\t2. Number Range" << endl;
    cout << "\t3. Odd or Even" << endl;

    int number;
    bool isValid = false;

    while (isValid == false) {
        cin >> number;
        if (number == 1) {
            isValid = true;
            break;
        }
        else if (number == 2) {
            isValid = true;
            break;
        }
        else if (number == 3) {
            isValid = true;
            break;
        }
        else {
            if (cin.fail()) { // invalid input like a char or string
                cout << "Please enter a valid integer value." << endl;
                cout << "New selection: ";
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
            }
            else { // number is not equal to 1, 2, or 3
                cout << "Invalid choice. Please enter 1, 2, or 3" << endl;
                cout << "New selection: ";
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
            }
        }
    }
    return number;
}

char Player::getUserColor() {
    cout << "Choose red or black:" << endl;
    cout << "\tR for red" << endl;
    cout << "\tB for black" << endl;

    char color;

    while (color != 'R' && color != 'B') {
        cin >> color;
        color = toupper(color);
    }
    return color;
}

int Player::getSingleNumber() {

    int number = -1;

    while (number < 0 || number > 36) {
        cout << "Choose a number from 0 to 36: ";
        cin >> number;

        // if the user enters a character or string
        if (cin.fail()) {
            cout << "Invalid input. Please enter an integer value." << endl;
            number = -1;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }

        if (number < 0) {
            cout << "The number you chose is too low" << endl;
        }
        else if (number > 36) {
            cout << "The number you chose is too high" << endl;
        }

        // clear the cin for when the user enters a double/float
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    return number;
}

vector<int> Player::getTwoNumbers() {
    int num1 = 0;
    int num2 = 0;
    bool isValid = false;
    while (!isValid) {
        num1 = getSingleNumber();
        num2 = getSingleNumber();
        if (num2 < num1) {
            cout << "Upper bound must be greater than lower bound" << endl;
        }
        
        int difference = num2 - num1;
        if (difference > 6) {
            cout << "The max range you can bet is 6 numbers. You will have to enter two new numbers." << endl << endl;
        }
        else if (difference > 0 && difference <= 6) {
            if (difference == 1 || difference == 5) {
                cout << "Range difference must be equal to 2, 3, 4, or 6. You will have to enter two new numbers." << endl << endl;
            }
            else {
                isValid = true;
            }
        }
    }
    
    vector<int> nums = {num1, num2};
    return nums;
}

string Player::getOddOrEven() {
    cout << "Please enter odd or even: ";

    string parity;

    while (parity != "even" && parity != "odd") {
        cin.ignore();
        getline(cin, parity);
        // convert the word to all lowercase
        transform(parity.begin(), parity.end(), parity.begin(), ::tolower);
        if (parity != "even" && parity != "odd") {
            cout << "Invalid choice. Please enter the word odd or even: ";
        }
    }

    return parity;
}

int Player::betAmount() {
    cout << "Enter your bet amount: ";
    string input;
    int betAmount;
    int playerMoney = this->getMoney();
    bool isValid = false;
    while (!isValid) {
        getline(cin, input);
        try {
            betAmount = stoi(input);
            if (betAmount > playerMoney) {
                cout << "You only have $" << playerMoney << " to bet. Enter a lower value: ";
            }
            else if (betAmount <= 0) {
                cout << "You must enter a value greater than 0. Enter a new bet amount: ";
            }
            else {
                isValid = true;
            }
        } catch (const invalid_argument &e1) {
            cout << "Invalid input. Please enter a valid integer: ";
        } catch (const out_of_range &e2) {
            cout << "Integer out of range error. Enter a smaller magnitude number: ";
        }
    }
    return betAmount;
}

void Player::printList(vector<int> list) {
    cout << "[";
    for (int i = 0; i < list.size(); i++) {
        if (i < list.size() - 1) {
            cout << list[i] << ", ";
        }
        else {
            cout << list[i];
        }
    }
    cout << "]" << endl;
}