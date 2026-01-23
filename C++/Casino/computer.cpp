#include <iostream>
using namespace std;
#include "include/casino.h"

Computer::Computer() {
    setNumber(0);
    setColor('\0');
}

void Computer::update() {
    int randomNumber = generateValue();
    setNumber(randomNumber);

    if (randomNumber == 0) {
        setColor('G');
    }
    else {
        char randomColor = generateColor();
        setColor(randomColor);
    }
}

void Computer::display() {
    cout << "Computer's color: " << this->getColor() << endl;
    cout << "Computer's number: " << this->getNumber() << endl;
}

int Computer::getNumber() {
    return this->number;
}

void Computer::setNumber(int number) {
    this->number = number;
}

char Computer::getColor() {
    return this->color;
}

void Computer::setColor(char color) {
    this->color = color;
}

int Computer::generateValue() {
    int randomValue = rand() % 37;
    return randomValue;
}

char Computer::generateColor() {
    vector<char> colors = {'R', 'B'};
    int index = rand() % colors.size();
    return colors[index];
}