# from googlesheetsreader import GoogleSheetsReader
# from llama_index import GoogleSheetsReader
from llama_index import download_loader

# Replace with your own credentials
credentials = {
    "client_id": ".apps.googleusercontent.com",
    "client_secret": "",
    # "refresh_token": "YOUR_REFRESH_TOKEN",
}

# Replace with your own spreadsheet ID and range
spreadsheet_id = "1dAxVVbb4-1z307p3rrv83SahcJX7pH3nyP-xM_a8lP8"
range_name = "Algorithms"

# Create a GoogleSheetsReader instance
gs_reader = GoogleSheetsReader(credentials)

# Read data from the specified range in the spreadsheet
data = gs_reader.get_values(spreadsheet_id, range_name)

# Print the data
print(data)
