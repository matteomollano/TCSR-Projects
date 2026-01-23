#include <iostream>
using namespace std;
#include "include/casino.h"

int main() {
    srand(time(0));

    Computer computer;
    Player player;

    Game game;
    bool game_playing = true;
    int betNumber = 1;

    while (game_playing) {
        cout << "BET " << betNumber << endl;
        computer.update();
        cout << endl;

        char color = player.getUserColor();
        cout << endl;
        player.setColor(color);

        int choice = player.bettingPrompt();
        cout << endl;
        player.setChoice(choice);

        player.update();
        // player.display();
        // cout << endl;

        cout << endl;
        game.evaluateBet(computer, player);
        cout << "These were the winning conditions: " << endl;
        computer.display();
        cout << endl;

        if (player.getMoney() >= 2147483647) {
            cout << "You were arrested for suspicions of defrauding the casino. All you assets were siezed. You now have $0." << endl;
            player.setMoney(0);
        }

        if (player.getMoney() == 0) {
            cout << "You were kicked out of the casino for having no money!" << endl;
            break;
        }

        if(!game.betAgain()) {
            game_playing = false;
        }
        else {
            betNumber++;
            cout << endl << endl;
        }
    }

    return 0;
}