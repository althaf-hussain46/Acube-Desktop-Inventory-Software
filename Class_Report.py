import xlsxwriter

class cls_report():
    def set_report_type(self, value):
        self.__report_type = value

    def get_report_type(self):
        return self.__report_type

    def set_grn_no(self, value):
        self.__grn_no = value

    def get_grn_no(self):
        return self.__grn_no

    def set_grn_date(self, value):
        self.__grn_date = value

    def get_grn_date(self):
        return self.__grn_date

    def set_supp_name(self, value):
        self.__supp_name = value

    def get_supp_name(self):
        return self.__supp_name

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
        return self.__cgst_taxable

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

    def export_to_excel(self, workbookname:str, worksheetname:str, header1:list, data1:list, title):
        workbook = xlsxwriter.Workbook(workbookname)
        worksheet = workbook.add_worksheet(worksheetname)


        worksheet.merge_range('A1:I1', title, workbook.add_format({'align' : 'center', 'font_size' : 25, 'bold':True, 'bg_color': '#5CACEE'}))
        for index, row in enumerate(header1):
            worksheet.write(2, index, row, workbook.add_format({'font_size':14, 'bold':True, 'bg_color': '#5CACEE'}))

        worksheet.set_column(0, 0, 25)#name
        worksheet.set_column(1, 1, 50)#add
        worksheet.set_column(2, 2, 20)#locality
        worksheet.set_column(3, 3, 15)#city
        worksheet.set_column(4, 4, 9)#pincode
        worksheet.set_column(5, 6, 11)#state and phone
        worksheet.set_column(7, 7, 32)#email
        worksheet.set_column(8, 8, 17)#gst

        for i1, row1 in enumerate(data1):
            for i2, row2 in enumerate(header1):
                if (i1+3)%2 == 0:
                    worksheet.write(i1+3, i2, row1[i2], workbook.add_format({'bg_color': '#B0E2FF'}))
                else:
                    worksheet.write(i1 + 3, i2, row1[i2], workbook.add_format({'bg_color': 'white'}))
        workbook.close()






