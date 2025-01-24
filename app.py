import time

from controllers.ContestChecker import ContestChecker
from database import Database


def app():
    while True:
        ContestChecker.new_contest_available()
        time.sleep(300)


if __name__ == "__main__":
    try:
        Database.init_database()
        app()
    except:
        print("app crashed :/")
