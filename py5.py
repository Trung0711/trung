'''
from tkinter import*
win= Tk()

win.mainloop()
'
from docx import Document

document = Document('G:\Downloads\Documents\qt.docx')

Dictionary = {'sea': "ocean"}

sections = document.sections
for section in sections:
    print(section.start_type)
'''
from dcm import*
