import java.util.ArrayList;
import java.util.List;

public class GradeBook {

    private List<Double> scores = new ArrayList<>();
    private List<Integer> rollNumbers = new ArrayList<>();

    public void addScore(double score) {
        if (score < 0) {
            throw new IllegalArgumentException("Score cannot be negative");
        }

        scores.add(score);
    }

    public void addStudent(int rollNumber, double score) {
        if (rollNumbers.contains(rollNumber)) {
            throw new IllegalArgumentException("Roll number already exists");
        }

        if (score < 0) {
            throw new IllegalArgumentException("Score cannot be negative");
        }

        rollNumbers.add(rollNumber);
        scores.add(score);
    }

    public double calculateAverage() {
        if (scores.isEmpty()) {
            return 0.0;
        }

        double total = 0;

        for (double score : scores) {
            total += score;
        }

        return total / scores.size();
    }
}