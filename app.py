import time

from controllers.ContestChecker import ContestChecker
from database import Database


def app():
    """Main function that runs the application"""
    while True:
        ContestChecker.new_contest_available()
        time.sleep(300)


if __name__ == "__main__":
    try:
        Database.init_database()
        app()
    except Exception as e:
        # TODO: Improve the exceptions
        print(f"sadly the application has crashed, error: {e}")
