import json
import win32print
from reportlab.pdfgen import canvas
from datetime import datetime
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import sys
import os


class LabelGenerator:
    def __init__(self, ui, template_file=None):
        self.ui = ui
        self.template_file = template_file if template_file else self.get_default_template_path()
        self.template = self.load_template()
        pdfmetrics.registerFont(TTFont('Aerial', self.get_font_path()))

    def get_base_dir(self):
        if getattr(sys, 'frozen', False):  # Приложение запущено в скомпилированном виде
            return os.path.dirname(sys.executable)
        else:  # Приложение запущено как скрипт на Python
            current_path = os.path.abspath(__file__)
            return os.path.dirname(os.path.dirname(current_path))

    def get_default_template_path(self):
        base_dir = self.get_base_dir()
        return os.path.join(base_dir, 'print_label', 'label_template.json')

    def get_font_path(self):
        base_dir = self.get_base_dir()
        print(base_dir)
        return os.path.join(base_dir, 'templates', 'times.ttf')

    def load_template(self):
        with open(self.template_file, 'r') as f:
            return json.load(f)

    def create_label(self, current_nomenclature, weight, output_file='label.pdf'):
        page_size = self.template.get('page_size')
        c = canvas.Canvas(output_file, pagesize=page_size)
        c.setFont("Aerial", 12)

        # Используем шаблон для размещения данных
        c.drawString(self.template['layout']['title']['x'], self.template['layout']['title']['y'],
                     self.template['title'])
        c.drawString(self.template['layout']['product_name']['x'], self.template['layout']['product_name']['y'],
                     self.template['fields']['product_name'].format(product_name=current_nomenclature))
        c.drawString(self.template['layout']['weight']['x'], self.template['layout']['weight']['y'],
                     self.template['fields']['weight'].format(weight=weight))

        c.showPage()
        c.save()
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        self.print_to_pdf(output_file, f'C:\\Users\\user\\Pictures\\labels\\1_{timestamp}.pdf')

    def print_to_pdf(self, input_file, output_file):
        # Открытие принтера
        printer_name = self.ui.chosePrinterPortionLabelComboBox.currentText()
        printer = win32print.OpenPrinter(printer_name)

        # Создание задания на печать
        job_id = win32print.StartDocPrinter(printer, 1, (output_file, None, "RAW"))
        win32print.StartPagePrinter(printer)

        with open(input_file, "rb") as f:
            pdf_data = f.read()
            win32print.WritePrinter(printer, pdf_data)

        win32print.EndPagePrinter(printer)
        win32print.EndDocPrinter(printer)
        win32print.ClosePrinter(printer)
