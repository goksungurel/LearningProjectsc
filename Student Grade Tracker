#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Functions
double calculateAverage(vector<double> grades) {
    double sum = 0;
    for (double grade : grades) {
        sum += grade;
    }
    return sum / grades.size();
}

string getStatus(double grade) {
    return (grade >= 60) ? "Passed" : "Failed";
}

int main() {
    string studentName;
    int numOfCourses;

    // Get student's name
    cout << "Enter the student's name: ";
    getline(cin, studentName);

    // Ask how many courses
    cout << "How many courses will you enter grades for? ";
    cin >> numOfCourses;

    vector<string> courseNames(numOfCourses);
    vector<double> courseGrades(numOfCourses);

    // Get course names and grades
    for (int i = 0; i < numOfCourses; i++) {
        cout << "Enter the name of course " << i + 1 << ": ";
        cin.ignore();
        getline(cin, courseNames[i]);

        cout << "Enter the grade for " << courseNames[i] << ": ";
        cin >> courseGrades[i];
    }

    // Display the success status of each course
    cout << "\nStudent's Success Status:\n";
    for (int i = 0; i < numOfCourses; i++) {
        cout << courseNames[i] << " course: " << courseGrades[i] << " - " 
             << getStatus(courseGrades[i]) << endl;
    }

    // Calculate the general success status (average grade)
    double average = calculateAverage(courseGrades);
    cout << "\nStudent's General GPA: " << average << endl;

    // Display overall success
    cout << "The student is " << (average >= 60 ? "Passed" : "Failed") << "." << endl;

    return 0;
}
