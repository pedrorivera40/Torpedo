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
    sheet = None

    def __init__(self, workbook_path=None):
        """
        Excel Export constructor. Leaving the workbook_path as None will create a new Excel file.
        :param sheet: string
        :param workbook_path: string
        """
        if workbook_path is None:
            self.workbook = xlwt.Workbook()
        else:
            self.workbook = copy(xlrd.open_workbook(workbook_path))

    def add_sheet(self, name):
        """
        Creates a new Excel sheet and sets it as the current.
        :param name: string
        :return: None
        """
        self.sheet = self.workbook.add_sheet(name)
        self.curr_row = 1

    def add_headers(self, headers):
        """
        Adds the headers along the first row of the Excel sheet.
        :param headers: list
        :return: None
        """
        for i in range(len(headers)):
            self.sheet.write(0, i, headers[i])

    def add_values(self, values):
        """
        The values to add to the Excel sheet. Every time this function is called, it will automatically write the values
        in a new row. Must call save() in order for the changes to take effect.
        :param values: list
        :return: None
        """
        for i in range(len(values)):
            self.sheet.write(self.curr_row, i, values[i])
        self.curr_row += 1

    def get_sheet(self):
        """
        Returns the current Excel sheet
        :return:
        """
        return self.sheet

    def get_workbook(self):
        return self.workbook

    def use_sheet(self, name):
        """
        Switches Excel sheet.
        :param name: string
        :return: None
        """
        self.sheet = self.workbook.get_sheet(name)
        self.curr_row = len(self.sheet.get_rows())

    def save(self, file_name='test_results.xls'):
        """
        Saves/Creates the excel sheet.
        :param file_name: string
        :return: None
        """
        self.workbook.save(file_name)
