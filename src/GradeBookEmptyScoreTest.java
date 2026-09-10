public class GradeBookEmptyScoreTest {

    public static void main(String[] args) {
        GradeBook gradeBook = new GradeBook();

        double average = gradeBook.calculateAverage();

        if (average == 0.0) {
            System.out.println("PASS: Empty score list returns 0.0");
        } else {
            System.out.println("FAIL: Expected 0.0");
        }
    }
}