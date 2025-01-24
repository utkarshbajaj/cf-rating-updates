class ResultCalculator:
    """Calculations based on the result of the contest for a participant"""

    @staticmethod
    def get_subject(old_rating, new_rating):
        """Subject of the email update to be sent."""
        if old_rating < new_rating:
            return "Congratulations!"
        return "Better luck next time!"

    @staticmethod
    def get_message(new_rating):
        """Body of the email update to be sent."""
        return f"Your new Codeforces Rating is: {new_rating} \nRegards,\nCodeforces Rating Updates"
