
public class Account {
    String ownerName;
    double balance;
    int pin;

    public Account(String ownerName, int pin) {
        this.ownerName = ownerName;
        this.balance = 0;
        this.pin = pin;
    }

    public boolean checkPin(int pin) {
        return this.pin == pin;
    }

    public void deposit(double amount) {
        if (amount <= 0) {
            this.balance = 0;
            System.out.println("You must enter a positive deposit amount.");
            return;
        }
        this.balance += amount;
    }

    public void withdraw(double amount) {
        if (amount <= 0) {
            this.balance = 0;
            System.out.println("You must enter a positive withdraw amount.");
            return;
        }
        if (amount > this.balance) {
            System.out.println("Your withdraw amount exceeds your balance.");
            return;
        }
        this.balance -= amount;
    }

    public String toString() {
        return String.format("""
        Owner: %s
        Balance: $%.2f""", this.ownerName, this.balance);
    }
}
