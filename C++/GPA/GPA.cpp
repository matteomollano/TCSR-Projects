#include <iostream>
using namespace std;
#include "GPA.h"

GPA::GPA(int numCourses, vector<double> grades) {
    setNumCourses(numCourses);
    setGrades(grades);
}

double GPA::getGPA() {
    return this->gpa;
}

void GPA::setGPA(double gpa) {
    this->gpa = gpa;
}

int GPA::getNumCourses() {
    return this->numCourses;
}

void GPA::setNumCourses(int numCourses) {
    this->numCourses = numCourses;
}

vector<double> GPA::getGrades() {
    return this->grades;
}

void GPA::setGrades(vector<double> grades) {
    this->grades = grades;
}

double GPA::calculateGPA() {
    vector<double> grades = this->getGrades();
    int numCourses = this->getNumCourses();

    double total = 0;
    for (int i = 0; i < numCourses; i++) {
        total += grades[i];
    }

    return total / numCourses;
}

double GPA::convertToMastery() {
    double gpa = this->calculateGPA();
    double mastery;

    if (gpa >= 97) {
        mastery = 4.33;
    }
    else if (gpa >= 93) {
        mastery = 4.0;
    }
    else if (gpa >= 90) {
        mastery = 3.67;
    }
    else if (gpa >= 87) {
        mastery = 3.33;
    }
    else if (gpa >= 83) {
        mastery = 3.0;
    }
    else if (gpa >= 80) {
        mastery = 2.67;
    }
    else if (gpa >= 77) {
        mastery = 2.33;
    }
    else if (gpa >= 73) {
        mastery = 2.0;
    }
    else if (gpa >= 70) {
        mastery = 1.67;
    }
    else if (gpa >= 67) {
        mastery = 1.33;
    }
    else if (gpa >= 65) {
        mastery = 1.0;
    }
    else {
        mastery = 0;
    }
    return mastery;
}

string GPA::convertToLetter() {
    double gpa = this->calculateGPA();
    string letter;

    if (gpa >= 97) {
        letter = "A+";
    }
    else if (gpa >= 93) {
        letter = "A";
    }
    else if (gpa >= 90) {
        letter = "A-";
    }
    else if (gpa >= 87) {
        letter = "B+";
    }
    else if (gpa >= 83) {
        letter = "B";
    }
    else if (gpa >= 80) {
        letter = "B-";
    }
    else if (gpa >= 77) {
        letter = "C+";
    }
    else if (gpa >= 73) {
        letter = "C";
    }
    else if (gpa >= 70) {
        letter = "C-";
    }
    else if (gpa >= 67) {
        letter = "D+";
    }
    else if (gpa >= 65) {
        letter = "D";
    }
    else {
        letter = "F";
    }
    return letter;
}