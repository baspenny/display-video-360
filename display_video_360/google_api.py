from google.oauth2 import service_account
from googleapiclient import discovery
from oauth2client.file import Storage
import httplib2


class GoogleAPI:
    def __init__(self, service_account=None, credentials=None):
        self.scopes = ['https://www.googleapis.com/auth/display-video']
        self.get_service(service_account, credentials)

    def get_service(self, service_account=None, credentials=None):
        creds = False
        if service_account:
            creds = self.__get_service_from_service_account(service_account_file=service_account)
        if credentials:
            creds = self.__get_service_from_credentials(credentials_file=credentials)

        self.service = discovery.build('displayvideo', 'v1', credentials=creds)
        if not creds:
            raise ValueError("No credentials were provided.")

    def __get_service_from_service_account(self, service_account_file):
        credentials = service_account.Credentials.from_service_account_file(
            service_account_file, scopes=self.scopes)
        return credentials

    def __get_service_from_credentials(self, credentials_file):
        storage = Storage(credentials_file)
        credentials = storage.get()
        if credentials is None or credentials.invalid:
            raise ValueError(
                f"The credentials in file {credentials_file} are not valid"
            )
        return credentials.authorize(httplib2.Http())
