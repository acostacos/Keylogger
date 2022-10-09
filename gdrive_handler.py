import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

SCOPES = ['https://www.googleapis.com/auth/drive.file']

class GDriveHandler:
    def __authenticate(self) -> None:
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('configuration.json', SCOPES)
                creds = flow.run_local_server(port=0)

            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        self.credentials = creds

    def upload_file(self, filename, mime_type, parent_folder_id) -> None:
        try:
            self.__authenticate()
            service = build('drive', 'v3', credentials=self.credentials)
            metadata = {
                'name': filename,
                'parents': [parent_folder_id] if parent_folder_id != None else [],
            }
            fileToUpload = MediaFileUpload(f'./{filename}', mimetype=mime_type)
            service.files().create(
                body=metadata,
                media_body=fileToUpload,
                fields='id'
            ).execute()

            
        except HttpError as error:
            # TODO(developer) - Handle errors from drive API.
            print(f'An error occurred: {error}')