import requests

from controllers.ParticipantsChecker import ParticipantsChecker
from database import Database
from utils.constants import GET_CONTESTS


class ContestChecker:
    """Check contest related updates"""

    @staticmethod
    def fetch_contests():
        """Fetch all available contests from Codeforces."""
        response = requests.get(GET_CONTESTS)
        if response.status_code == 200:
            return response.json()
        raise RuntimeError("Response status for the contest fetch is not 200.")

    @staticmethod
    def new_contest_available():
        """Check if a new contest is available for sending updates to participants"""
        contests = ContestChecker.fetch_contests()
        num_contests = len(contests["result"])
        results = contests["result"]

        last_update = Database.get_document("contests", "last_update")

        for i in range(0, num_contests, 1):
            contest = results[i]
            if contest["id"] <= last_update["contest_number"]:
                break

            if contest["phase"] == "FINISHED":
                ParticipantsChecker.check_participants(contest["id"])
