import java.util.Scanner;

public class TemperatureConverter {

    public static Double getValue(Scanner sc, String unit) {
        // Kelvin = 0 to infinity
        // Celsius = -273.15 to infinity
        // Fahrenheit = -459.67 to infinity
        String strValue = sc.nextLine();
        unit = unit.toLowerCase();
        try {
            Double doubleValue = Double.valueOf(strValue);
            
            if (unit.equals("f")) {
                if (doubleValue < -459.67) {
                    System.out.println("Fahrenheit value cannot be below the minimum threshold (-459.67).");
                    return getValue(sc, unit);
                }
            }

            else if (unit.equals("c")) {
                if (doubleValue < -273.15) {
                    System.out.println("Celsius value cannot be below the minimum threshold (-273.15).");
                    return getValue(sc, unit);
                }
            }

            else if (unit.equals("k")) {
                if (doubleValue < 0) {
                    System.out.println("Kelvin value cannot be below absolute zero (0 Kelvin).");
                    return getValue(sc, unit);
                }
            }
            
            return doubleValue;
        }
        catch (NumberFormatException e) {
            System.out.println("You must only enter a number.");
            return getValue(sc, unit);
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("What temperature conversion do you wish to do?");
            System.out.println("1. Fahrenheit to Celsius");
            System.out.println("2. Celsius to Fahrenheit");
            System.out.println("3. Celsius to Kelvin");
            System.out.println("4. Kelvin to Celsius");
            System.out.println("5. Quit");
            System.out.print("Your choice: ");
            String user = sc.nextLine().strip();

            if (user.equals("1")) {
                System.out.println("What temperature in Fahrenheit do you wish to convert to Celsius?");
                Double f = getValue(sc, "f");
                Double c = (f - 32) / 1.8;
                System.out.printf("%.2f degrees F = %.2f degrees C", f, c);
            }

            else if (user.equals("2")) {
                System.out.println("What temperature in Celsius do you wish to convert to Fahrenheit?");
                Double c = getValue(sc, "c");
                Double f = (c * 1.8) + 32;
                System.out.printf("%.2f degrees C = %.2f degrees F", c, f);
            }

            else if (user.equals("3")) {
                System.out.println("What temperature in Celsius do you wish to convert to Kelvin?");
                Double c = getValue(sc, "c");
                Double k = c + 273.15;
                System.out.printf("%.2f degrees C = %.2f K", c, k);
            }

            else if (user.equals("4")) {
                System.out.println("What temperature in Kelvin do you wish to convert to Celsius?");
                Double k = getValue(sc, "k");
                Double c = k - 273.15;
                System.out.printf("%.2f K = %.2f degrees C", k, c);
            }

            else if (user.equals("5")) {
                System.out.println("Exiting...");
                break;
            }

            System.out.println("\n");
        }

        sc.close();
    }
}
