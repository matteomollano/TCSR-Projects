import java.util.ArrayList;

/*
    List that stores multiple Expense objects
    How to create: Expense obj1 = new Expense();
    ArrayList -> [obj1, obj2, obj3, obj4]
*/
public class ExpenseTracker {
    // TODO: Declare an ArrayList to store Expense objects
    // This will be the main collection that holds all user expenses
    ArrayList<Expense> expenses;
    
    // TODO: Constructor - initialize the ArrayList for storing expenses
    public ExpenseTracker() {
        expenses = new ArrayList<Expense>();
    }
    
    // TODO: addExpense() method
    // - Takes an Expense object as a parameter
    // - Adds it to the collection
    public void addExpense(Expense expense) {
        this.expenses.add(expense);
    }
    
    // TODO: removeExpense() method
    // - Takes an identifier (expenseID) as parameter
    // - Removes the expense from the collection
    public void removeExpense(String expenseID) {
        for (Expense expense : this.expenses) {
            String id = expense.getExpenseID();
            if (expenseID.equals(id)) {
                this.expenses.remove(expense);
                break;
            }
        }
    }

    // TODO: displayExpenses() method
    // - Display all tracked expenses
    
    // TODO: displayTotalExpenses() method
    // - Calculates and displays the sum of all expense amounts
    
    // TODO: displayExpensesByCategory() method
    // - Takes a category as parameter
    // - Displays filtered expenses by that category
    
    // TODO: displayExpensesByDateRange() method
    // - Takes start and end dates as parameters
    // - Displays expenses within that date range
}
