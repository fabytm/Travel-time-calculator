import gspread
from oauth2client.service_account import ServiceAccountCredentials


def get_sheet(key, sheetID):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name(key, scope)

    gc = gspread.authorize(credentials) #Authentification

    with open(sheetID) as sheet_ID_file:
        sheet_ID = sheet_ID_file.read()

    return gc.open_by_key(sheet_ID).sheet1 #opens the sheet to which we are going to append

