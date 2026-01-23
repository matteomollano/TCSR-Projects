#include <iostream>
using namespace std;
#include <vector>
#include "include/PasswordManager.h"

int main() {

    vector <PasswordManager> passwordManager;

    string website;
    string email;
    string username;
    string password;

    cout << "Enter the website you want to save a password for: ";
    getline(cin, website);

    cout << "Enter your email: ";
    getline(cin, email);

    cout << "Enter your username: ";
    getline(cin, username);

    cout << "Enter your password: ";
    getline(cin, password);
    cout << endl;

    PasswordManager pm(website, email, username, password);
    pm.display();
}
