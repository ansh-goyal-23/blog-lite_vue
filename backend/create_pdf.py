from jinja2 import Template
from weasyprint import HTML
import uuid


def format_report(template_file, data={}):
    with open(template_file) as file_:
        template = Template(file_.read())
        return template.render(data=data)

def create_pdf_report(data):
    message = format_report("report-template.html", data=data)
    html = HTML(string=message)
    file_name = str(data['name']) + ".pdf"
    
    html.write_pdf(target=file_name) 
    return file_name


