import xlsxwriter

class cls_sales_report():
    def set_report_type(self, value):
        self.__report_type = value

    def get_report_type(self):
        return self.__report_type


    def set_cust_name(self, value):
        self.__cust_name = value

    def get_cust_name(self):
        return self.__cust_name

    def set_bill_no(self, value):
        self.__bill_no = value

    def get_bill_no(self):
        return self.__bill_no

    def set_bill_date(self, value):
        self.__bill_date = value

    def get_bill_date(self):
        return self.__bill_date

    def set_bill_qty(self, value):
        self.__bill_qty = value

    def get_bill_qty(self):
        return self.__bill_qty

    def set_item_total(self, value):
        self.__item_total = value

    def get_item_total(self):
        return self.__item_total

    def set_less_amount(self, value):
        self.__less_amount = value

    def get_less_amount(self):
        return self.__less_amount

    def set_taxable_amt(self, value):
        self.__taxable_amt = value

    def get_taxable_amt(self):
        return self.__taxable_amt

    def set_cgst_amt(self, value):
        self.__cgst_amt = value

    def get_cgst_amt(self):
        return self.__cgst_amt

    def set_sgst_amt(self, value):
        self.__sgst_amt = value

    def get_sgst_amt(self):
        return self.__sgst_amt

    def set_bill_amount(self, value):
        self.__bill_amount = value

    def get_bill_amount(self):
        return self.__bill_amount

    def export_to_excel(self, workbookname:str, worksheetname:str, header1:list, data1:list):
        workbook = xlsxwriter.Workbook(workbookname)
        worksheet = workbook.add_worksheet(worksheetname)

        for index, row in enumerate(header1):
            worksheet.write(0, index, row)

        for i1, row1 in enumerate(data1):
            for i2, row2 in enumerate(header1):
                worksheet.write(i1+1, i2, row1[i2])

        workbook.close()




