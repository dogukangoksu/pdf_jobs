# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 00:25:06 2020

@author: Dogukan
"""

from PyPDF2 import PdfFileMerger

pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()