public class Dog {
    // properties
    String name;
    String furColor;
    String eyeColor;
    double height;
    double weight;

    // Default Constructor
    public Dog() {
        this.name = "Cooper";
        this.furColor = "golden";
        this.eyeColor = "blue";
        this.height = 24.2;
        this.weight = 68.3;
    }

    // Parameterized Constructor
    public Dog(String name, String furColor, String eyeColor, double height, double weight) {
        this.name = name;
        this.furColor = furColor;
        this.eyeColor = eyeColor;
        this.height = height;
        this.weight = weight;
    }

    public String getName() {
        return this.name;
    }

    public String getFurColor() {
        return this.furColor;
    }

    public String getEyeColor() {
        return this.eyeColor;
    }

    public double getHeight() {
        return this.height;
    }

    public double getWeight() {
        return this.weight;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setFurColor(String furColor) {
        this.furColor = furColor;
    }

    public void setEyeColor(String eyeColor) {
        this.eyeColor = eyeColor;
    }

    public void setHeight(double height) {
        this.height = height;
    }

    public void setWeight(double weight) {
        this.weight = weight;
    }

    @Override
    public String toString() {
        return String.format("Name: %s, Fur Color: %s, Eye Color: %s, Height: %.2f, Weight: %.2f", this.name, this.furColor, this.eyeColor, this.height, this.weight);
    }
}