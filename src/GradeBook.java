import java.util.ArrayList;
import java.util.List;

public class GradeBook {

    private List<Double> scores = new ArrayList<>();

    public void addScore(double score) {
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