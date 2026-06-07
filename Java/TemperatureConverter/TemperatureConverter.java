import java.util.Scanner;

public class TemperatureConverter {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("What temperature conversion do you wish to do?");
        System.out.println("1. Fahrenheit to Celsius");
        System.out.println("2. Celsius to Fahrenheit");
        System.out.println("3. Celsius to Kelvin");

        String user = sc.nextLine().strip();

        if (user.equals("1")) {
            System.out.println("What temperature in Fahrenheit do you wish to convert to Celsius?");
            Double f = sc.nextDouble();
            Double c = (f - 32) / 1.8;
            System.out.printf("%.2f degrees F = %.2f degrees C", f, c);
        }

        else if (user.equals("2")) {
            System.out.println("What temperature in Celsius do you wish to convert to Fahrenheit?");
            Double c = sc.nextDouble();
            Double f = (c * 1.8) + 32;
            System.out.printf("%.2f degrees C = %.2f degrees F", c, f);
        }

        else if (user.equals("3")) {
            System.out.println("What temperature in Celsius do you wish to convert to Kelvin?");
            Double c = sc.nextDouble();
            Double k = c + 273.15;
            System.out.printf("%.2f degrees C = %.2f K", c, k);
        }

        sc.close();
    }
}
