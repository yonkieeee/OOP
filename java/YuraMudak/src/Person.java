public class Person {
    protected final int height;
    protected final float weight;

    public Person(int height, float weight) {
        this.height = height;
        this.weight = weight;
    }

    void saySmth(String message) {
        System.out.println(message + height + weight);
    }

    Person() {this.height = 0; this.weight = 0;}
}
