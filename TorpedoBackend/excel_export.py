import xlrd
import xlwt
from xlutils.copy import copy


class ExcelExport:
    """
    Excel Export class.
    Use this class to help export data into an excel sheet.
    """

    curr_row = 1  # Row in which values are going to be written.
    sheet = None  # The current Excel sheet.

    def __init__(self, workbook_path):
        """
        Excel Export constructor.
        If the file exists in the workbook_path it will use that one. Otherwise it will create a new one after save().
        :param workbook_path: string
        """
        self.workbook_path = workbook_path
        try:
            self.workbook = copy(xlrd.open_workbook(workbook_path))  # If workbook exists, create a copy
        except FileNotFoundError:
            self.workbook = xlwt.Workbook()  # If the workbook does not exist, create a new one

    def add_sheet(self, name):
        """
        Creates a new Excel sheet and sets it as the current.
        :param name: string
        :return: None
        """
        try:
            self.sheet = self.workbook.add_sheet(name,cell_overwrite_ok=True)
            self.curr_row = 1
        except Exception:
            print('ERROR: The sheet \'%s\' already exists. Change the name of use select_sheet().' % (name, ))

    def add_headers(self, headers):
        """
        Adds the headers along the first row of the Excel sheet.
        :param headers: list
        :return: None
        """
        if self.sheet is None:
            print('ERROR: Cannot add headers. No sheet selected. Use add_sheet() or select_sheet().')
        else:
            for i in range(len(headers)):
                self.sheet.write(0, i, headers[i])
            self.curr_row += 1

    def add_values(self, values):
        """
        The values to add to the Excel sheet. Every time this function is called, it will automatically write the values
        in a new row. Must call save() in order for the changes to take effect.
        :param values: list
        :return: None
        """
        if self.sheet is None:
            print('ERROR: Cannot add values. No sheet selected. Use add_sheet() or select_sheet().')
        else:
            for i in range(len(values)):
                self.sheet.write(self.curr_row, i, values[i])
            self.curr_row += 1

    def add_hv_values(self, values):
        """
        The values to add to the Excel sheet. Every time this function is called, it will automatically write the values
        in a new row. Must call save() in order for the changes to take effect.
        :param values: list
        :return: None
        """
        if self.sheet is None:
            print('ERROR: Cannot add values. No sheet selected. Use add_sheet() or select_sheet().')
        else:
            for i in range(0,len(values)-1):
                self.sheet.write(i, 1, values[i])
            


    def get_sheet(self):
        """
        Returns the current Excel sheet
        :return:
        """
        return self.sheet

    def get_workbook(self):
        return self.workbook

    def select_sheet(self, name):
        """
        Switches Excel sheet.
        :param name: string
        :return: None
        """
        try:
            self.sheet = self.workbook.get_sheet(name)
            self.curr_row = len(self.sheet.get_rows())
        except Exception:
            print('ERROR: The sheet %s does not exist. Use add_sheet().' % (name, ))

    def save(self):
        """
        Saves/Creates the excel sheet.
        :param file_name: string
        :return: None
        """
        try:
            self.workbook.save(self.workbook_path)
            print('Workbook saved!')
        except IndexError:
            print('ERROR: Could not save workbook. No sheets created. Use add_sheet().')
