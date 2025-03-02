#include <iostream>
using namespace std;

int main() {
    double num1, num2;
    int choice;

    while (true) {
        cout << "Enter the first number: ";
        cin >> num1;
        cout << "Enter the second number: ";
        cin >> num2;
      
        cout << "\nChoose an operation:" << endl;
        cout << "1. Addition" << endl;
        cout << "2. Subtraction" << endl;
        cout << "3. Multiplication" << endl;
        cout << "4. Division" << endl;
        cout << "5. Exit" << endl;
        cout << "Make your choice (1/2/3/4/5): ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Result: " << num1 + num2 << endl;
                break;
            case 2:
                cout << "Result: " << num1 - num2 << endl;
                break;
            case 3:
                cout << "Result: " << num1 * num2 << endl;
                break;
            case 4:
                if (num2 != 0) {
                    cout << "Result: " << num1 / num2 << endl;
                } else {
                    cout << "Division by zero is not allowed!" << endl;
                }
                break;
            case 5:
                cout << "Exiting... Goodbye!" << endl;
                return 0;
            default:
                cout << "Invalid input, please try again." << endl;
        }
        cout << "\n";
    }

    return 0;
}
