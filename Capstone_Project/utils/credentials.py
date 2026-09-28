import os

class CredentialReader:

    @staticmethod
    def get_valid_password():
        password = os.getenv("TN_TEST_PASSWORD")

        if not password:
            raise RuntimeError(
                "TN_TEST_PASSWORD environment variable "
                "is not configured."
            )

        return password

    @staticmethod
    def get_invalid_password():
        return "invalid_test_password"