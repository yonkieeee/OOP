public class Student extends Person {
    private final int course;

    Student(int height, float weight, int course) {
        super(height, weight);
        this.course = course;
    }

    void sayCourse(){
        System.out.println(this.course);
    }
}
