#include "include/PasswordManager.h"

PasswordManager::PasswordManager(string website, string email, string username, string password) {
    setWebsite(website);
    setEmail(email);
    setUsername(username);
    setPassword(password);
}

string PasswordManager::getWebsite() {
    return this->website;
}

void PasswordManager::setWebsite(string website) {
    this->website = website;
}

string PasswordManager::getEmail() {
    return this->email;
}

void PasswordManager::setEmail(string email) {
    this->email = email;
}

string PasswordManager::getPassword() {
    return this->password;
}

void PasswordManager::setPassword(string password) {
    this->password = password;
}

string PasswordManager::getUsername() {
    return this->username;
}

void PasswordManager::setUsername(string username) {
    this->username = username;
}

void PasswordManager::display() {
    cout << "Website: " << this->getWebsite() << endl;
    cout << "Email: " << this->getEmail() << endl;
    cout << "Username: " << this->getUsername() << endl;
    cout << "Password: " << this->getPassword() << endl;
}
