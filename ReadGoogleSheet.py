import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_list_of_docs():
    # Set up credentials
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('ServiceAccountCredentials.json', scope)
    client = gspread.authorize(creds)

    # Open a worksheet from your Google Sheets account
    # sheet = client.open_by_key('18Y5uEyvitSvVcHI9amqQCeFqMFDBhTJGVw6EDYXx7kY').get_worksheet(0);
    sheet = client.open_by_key('1E38WHR8zeIpTJwUBsOmJ7RDUMPEk_b93wiFn1vQjO4s').get_worksheet(0);

    # Read data from the worksheet
    data = sheet.get_all_records()
    sortedData = sorted(data, key=lambda d: d['File-Type'])

    return sortedData

# print(get_list_of_docs())
