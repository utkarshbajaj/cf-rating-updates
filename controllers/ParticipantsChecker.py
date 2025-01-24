import time

import requests

from controllers.SMTPEmailService import SmtpEmailService
from database import Database
from utils.constants import GET_RESULTS
from utils.ResultCalculator import ResultCalculator


class ParticipantsChecker:

    @staticmethod
    def fetch_contest_results(contest_id):
        """Fetch results for a particular contest from codeforces."""
        contests_uri = GET_RESULTS + str(contest_id)
        response = requests.get(contests_uri)
        if response.status_code == 200:
            result = response.json()
            return result["result"]
        raise RuntimeError("response status for the contest fetch is not 200.")

    @staticmethod
    def check_participants(contest_id):
        """Check if a user in the database is a particiapnt in the contest"""

        # TODO: Do we have to do this everytime?
        # Ideally we should do it everytime because there might be new users
        # But, there should be a way for checking that and storing the old ones.
        # (over engineering for this problem?)
        documents = Database.get_all_documents("users")

        app_users = {}

        for document in documents:
            app_users[document["name"]] = document["email"]

        start_time = time.time()

        contest_results = ParticipantsChecker.fetch_contest_results(contest_id)

        for user_result in contest_results:
            if user_result["handle"] in app_users:
                mail_subject = ResultCalculator.get_subject(
                    user_result["oldRating"], user_result["newRating"]
                )
                mail_body = ResultCalculator.get_message(user_result["newRating"])

                SmtpEmailService.send_email(
                    app_users[user_result["handle"]], mail_subject, mail_body
                )

        end_time = time.time()

        execution_time = end_time - start_time
        print(f"Time taken to run email routine: {execution_time:.4f} seconds")
