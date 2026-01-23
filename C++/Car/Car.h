#include <iostream>
#include <string>
using namespace std;

class Car {
    private:
        string make;
        string model;
        string color;
        int year;
    public:
        // constructor
        Car(string make, string model, string color, int year);

        // getter/setter methods
        string getMake();
        void setMake(string make);
        string getModel();
        void setModel(string model);
        string getColor();
        void setColor(string color);
        int getYear();
        void setYear(int year);

        // other methods
        void print();    
};