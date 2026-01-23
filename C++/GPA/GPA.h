#include <vector>
using namespace std;

class GPA {
    private:
        double gpa;
        int numCourses;
        vector<double> grades;
    public:
        GPA(int numCourses, vector<double> grades);

        double getGPA();
        void setGPA(double gpa);

        int getNumCourses();
        void setNumCourses(int numCourses);

        vector<double> getGrades();
        void setGrades(vector<double> grades);

        double calculateGPA();
        double convertToMastery();
        string convertToLetter();
};