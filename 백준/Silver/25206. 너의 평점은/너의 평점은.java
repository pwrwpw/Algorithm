import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        Map<String, Double> gradePoints = new HashMap<>();
        gradePoints.put("A+", 4.5);
        gradePoints.put("A0", 4.0);
        gradePoints.put("B+", 3.5);
        gradePoints.put("B0", 3.0);
        gradePoints.put("C+", 2.5);
        gradePoints.put("C0", 2.0);
        gradePoints.put("D+", 1.5);
        gradePoints.put("D0", 1.0);
        gradePoints.put("F", 0.0);
        gradePoints.put("P", 0.0);

        Map<String, String> subjects = new LinkedHashMap<>();
        Map<String, Double> credits = new LinkedHashMap<>();

        for (int i = 0; i < 20; i++) {
            String[] input = br.readLine().split(" ");
            String subject = input[0];
            double credit = Double.parseDouble(input[1]);
            String grade = input[2];
            subjects.put(subject, grade);
            credits.put(subject, credit);
        }

        double totalPoints = 0.0;
        double totalCredits = 0.0;

        for (String subject : subjects.keySet()) {
            String grade = subjects.get(subject);
            if(Objects.equals(grade, "P")) continue;
            if (gradePoints.containsKey(grade)) {
                totalPoints += gradePoints.get(grade) * credits.get(subject);
                totalCredits += credits.get(subject);
            }
        }

        double gpa = totalPoints / totalCredits;
        bw.write(String.format("%.6f", gpa));
        br.close();
        bw.close();
    }
}
