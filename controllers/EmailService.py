from abc import ABC, abstractmethod


class EmailService(ABC):
    @staticmethod
    @abstractmethod
    def send_email(to: str, subject: str, body: str):
        """Send an email to the specified recepient"""
        pass
