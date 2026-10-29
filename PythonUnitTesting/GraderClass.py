
class GraderClass:
    def calculate_average(self, grades):
        if not grades:
            raise ValueError("Grades cannot be empty")

        return sum(grades) / len(grades)

    def get_letter_grade(self, score):
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")

        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    def is_passing(self, score):
        return score >= 60
