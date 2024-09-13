import gspread
import json
from docassemble.base.util import get_config
from typing import Dict, Optional
from oauth2client.service_account import ServiceAccountCredentials
credential_info = json.loads(get_config('google').get('service account credentials'), strict=False)
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
__all__ = ['read_sheet','append_to_sheet']


def get_sheet(
    sheet_name: str,
    worksheet_index: Optional[int] = 0,
    worksheet_name: Optional[str] = None,
    credentials_path: Optional[str] = None,
) -> gspread.Worksheet:
    """
    Get the matching worksheet from the spreadsheet.

    Args:
        sheet_name (str): The name of the spreadsheet.
        worksheet_index (int, optional): The index of the worksheet.
        worksheet_name (str, optional): The name of the worksheet.
        credentials_path (str, optional): The path to the credentials file in global configuration.
    """
    if not credentials_path:
        credentials_path = "google"
    credential_json = get_config(credentials_path).get(
        "service account credentials", None
    )
    if credential_json is None:
        credential_info = None
    else:
        credential_info = json.loads(credential_json, strict=False)
    creds = ServiceAccountCredentials.from_json_keyfile_dict(credential_info, scope)

    client = gspread.authorize(creds)
    if worksheet_index is None and worksheet_name is None:
        worksheet_index = 0
    if worksheet_name:
        return client.open(sheet_name).worksheet(worksheet_name)
    else:
        return client.open(sheet_name).get_worksheet(worksheet_index)


def read_sheet(
    sheet_name: str,
    worksheet_index: Optional[int] = 0,
    worksheet_name: Optional[str] = None,
):
    sheet = get_sheet(sheet_name, worksheet_index, worksheet_name)
    return sheet.get_all_records()


def append_to_sheet(
    sheet_name,
    vals,
    worksheet_index=0,
    worksheet_name=None,
    credentials_path: Optional[str] = None,
):
    sheet = get_sheet(sheet_name, worksheet_index, worksheet_name, credentials_path)
    sheet.append_row(vals)
