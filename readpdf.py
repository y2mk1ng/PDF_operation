import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
import sys, os

def extract_pdf(pdf_path):
    with open(pdf_path, 'rb') as fp:
        pdf_read = PdfFileReader(fp)
        info = pdf_read.getDocumentInfo()
        page_num = pdf_read.getNumPages()
    t = f"""
    =====Begin information about {pdf_path}=====

    Author: {info.author}
    Creator: {info.creator}
    Producer: {info.producer}
    Subject: {info.subject}
    Title: {info.title}
    Number of pages: {page_num}

    ======End information about {pdf_path}======
    """
    print(t)
    return(info)
def split_pdf(pdf_path, name_of_split):
    pdf_read = PdfFileReader(pdf_path)
    pdf_writer = PdfFileWriter()
    page_num = pdf_read.getNumPages()
    for page in range(page_num):
        pdf_writer.addPage(pdf_read.getPage(page))
        output = f'{name_of_split}{page}_new.pdf'
        with open(output, 'wb') as out_pdf:
            pdf_writer.write(out_pdf)
if __name__ == '__main__':
    path = '/home/asuka/Downloads/Q1_GYL.pdf'
    extract_pdf(path)
    split_pdf(path, 'p')
