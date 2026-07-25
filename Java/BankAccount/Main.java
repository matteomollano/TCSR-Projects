import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("What is your name? ");
        String ownerName = sc.nextLine(); 

        System.out.println("What would you like your pin code to be? ");
        int pin = sc.nextInt();

        Account acc = new Account(ownerName, pin);

        acc.deposit(100);
        acc.withdraw(50);
        System.out.println(acc);

        sc.close();
    }
}
