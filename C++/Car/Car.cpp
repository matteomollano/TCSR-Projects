#include <iostream>
#include <string>
using namespace std;
#include "Car.h"

// Constructor
Car::Car(string make, string model, string color, int year) {
    this->make = make;
    this->model = model;
    this->color = color;
    this->year = year;
}

// getter and setter methods
string Car::getMake() {
    return this->make;
}

void Car::setMake(string make) {
    this->make = make;
}

string Car::getModel() {
    return this->model;
}

void Car::setModel(string model) {
    this->model = model;
}

string Car::getColor() {
    return this->color;
}

void Car::setColor(string color) {
    this->color = color;
}

int Car::getYear() {
    return this->year;
}

void Car::setYear(int year) {
    this->year = year;
}

void Car::print() {
    cout << "Car Information:" << endl;
    cout << "Make: " + this->getMake() << endl;
    cout << "Model: " + this->getModel() << endl;
    cout << "Color: " + this->getColor() << endl;
    cout << "Year: " + to_string(this->getYear()) << endl;
}