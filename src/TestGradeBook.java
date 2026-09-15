public class TestGradeBook {
    public static void main(String[] args) {

        GradeBook gb = new GradeBook();

        try {
            gb.addScore(0);
            System.out.println("PASS: Minimum score 0 was accepted");
        } catch (Exception e) {
            System.out.println("FAIL: Minimum score 0 was rejected");
        }
    }
}