#include <iostream>
using namespace std;
#include "GPA.h"

int getNumCourses();
double getGrade();
void displayGrades(vector<double> grades);

int main() {

    int numCourses = getNumCourses();
    // cout << "numCourses = " << numCourses << endl;
    
    double grade;
    vector<double> grades;
    for (int i = 0; i < numCourses; i++) {
        grade = getGrade();
        grades.push_back(grade);
    }
    // displayGrades(grades);

    GPA gpa(numCourses, grades);
    //cout << "numCourses class variable = " << gpa.getNumCourses() << endl;
    //cout << "grades class variable = "; 
    //displayGrades(gpa.getGrades());
    double avg = gpa.calculateGPA();
    cout << "\nYour grade point average is: " << avg << endl;

    double mastery = gpa.convertToMastery();
    cout << "Your grade on the mastery scale is " << mastery << endl;

    string letter = gpa.convertToLetter();
    cout << "Your letter grade is " << letter << endl;
}

int getNumCourses() {

    int numCourses;
    bool isValid = false;

    while (!isValid) {
        cout << "Please enter your number of courses: ";
        cin >> numCourses;

        cout << "numCourses = " << numCourses << endl;

        if (cin.fail()) { // invalid input
            cout << "Please enter a valid integer value." << endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }
        else { // valid integer value
            if (numCourses <= 0) {
                cout << "Please enter a positive integer value." << endl;
            }
            else if (numCourses > 30) {
                cout << "The course limit is 30." << endl;
            }
            else {
                isValid = true;
            }
        }
    }
    return numCourses;
}

double getGrade() {

    double grade;
    bool isValid = false;

    while (!isValid) {
        cout << "Enter your course grade: ";
        cin >> grade;

        if (cin.fail()) { // invalid input
            cout << "Please enter a valid double." << endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }
        else { // valid input
            if (grade >= 0 && grade <= 150) {
                isValid = true;
            }
            else { // value less than 0 or greater than 150
                cout << "Please enter a grade between 0 and 150" << endl;
            }
        }
    }
    return grade;
}

void displayGrades(vector<double> grades) {
    cout << "[";
    for (int i = 0; i < grades.size(); i++) {
        if (i == grades.size()-1) {
            cout << grades[i];
        }
        else {
            cout << grades[i] << ", "; 
        }
    }
    cout << "]" << endl;
}