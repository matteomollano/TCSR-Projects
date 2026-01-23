#include <iostream>
using namespace std;

class PasswordManager {
    private:
        string website;
        string email;
        string username;
        string password;
    public:
        PasswordManager(string website, string email, string username, string password);

        string getWebsite();
        void setWebsite(string website);

        string getEmail();
        void setEmail(string email);

        string getUsername();
        void setUsername(string username);

        string getPassword();
        void setPassword(string password);

        void display();
};
