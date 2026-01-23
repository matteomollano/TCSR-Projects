
public class Main {
    public static void main(String[] args) {
        Expense expense1 = new Expense("Cookies", 4.99f, "Baking", "01/03/2026");
        Expense expense2 = new Expense("PC", 1299.99f, "Technology", "01/22/2026");
        Expense expense3 = new Expense("Flour", 8.99f, "Baking", "01/16/2026");

        Tracker tracker = new Tracker();
        tracker.addExpense(expense1);
        tracker.addExpense(expense2);
        tracker.addExpense(expense3);

        tracker.displayExpensesByCategory("Baking");
    }
}
