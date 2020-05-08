import xlrd
import xlwt
from xlutils.copy import copy


class ExcelExport:

    """
    Excel Export class.
    Use this class to help export data into an excel sheet.
    """

    headers = []
    curr_row = 1


    def __init__(self, sheet, headers, workbook_path=None):
        """
        Excel Export constructor. Leaving the workbook_path as None will create a new Excel file.
        :param sheet: string
        :param headers: list
        :param workbook_path: string
        """
        if workbook_path is None:
            self.workbook = xlwt.Workbook()
            sheet = self.workbook.add_sheet(sheet)
        else:
            old_workbook_read = xlrd.open_workbook(workbook_path)
            self.workbook = copy(old_workbook_read)
            sheet = self.workbook.get_sheet(sheet)
            self.curr_row = len(sheet.get_rows())
        self.headers = headers
        for i in range(len(headers)):
            sheet.write(0, i, headers[i])
        self.sheet = sheet

    def add_values(self, values):
        """
        The values to add to the Excel sheet. Every time this function is called, it will automatically write the values
        in a new row. Must call save() in order for the changes to take effect.
        :param values: list
        :return:
        """
        for i in range(len(values)):
            self.sheet.write(self.curr_row, i, values[i])
        self.curr_row += 1

    def get_sheet(self):
        return self.sheet

    def get_workbook(self):
        return self.workbook

    def save(self, file_name='test_results.xls'):
        """
        Saves/Creates the excel sheet.
        :param file_name: string
        :return: None
        """
        self.workbook.save(file_name)

