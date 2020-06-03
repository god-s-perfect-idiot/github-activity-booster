from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import base64

SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'

def main():

    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))

    # Call the Gmail API to fetch INBOX
    results = service.users().messages().list(userId='me',labelIds = ['INBOX']).execute()
    messages = results.get('messages', [])


    if not messages:
        pass
    else:
        message = messages[0]
        msg = service.users().messages().get(userId='me', id=message['id'], format='full').execute()
        decoded=base64.urlsafe_b64decode(msg['payload']['body']['data'].encode('ASCII'))
        decoded = str(decoded).split('Verification code')[1][2:8]
        return decoded

if __name__ == '__main__':
    main()
