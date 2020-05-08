import xlrd
import xlwt
from xlutils.copy import copy


class Export:

    headers = []
    curr_row = 1

    def __init__(self, sheet, headers, workbook_path=None):
        if workbook_path is None:
            self.workbook = xlwt.Workbook()
        else:
            self.workbook = copy(xlrd.open_workbook(workbook_path))
        sheet = self.workbook.add_sheet(sheet)
        self.headers = headers
        for i in range(len(headers)):
            sheet.write(0, i, headers[i])
        self.sheet = sheet

    def add_values(self, values):
        for i in range(len(values)):
            self.sheet.write(self.curr_row, i, values[i])
        self.curr_row += 1

    def get_sheet(self):
        return self.sheet

    def get_workbook(self):
        return self.workbook

    def save(self, file_name='test_results.xls'):
        self.workbook.save(file_name)

