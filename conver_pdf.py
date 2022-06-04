import PyPDF2

# Leer solo una página

# obj_pdf=open("CONPES.pdf","rb")
# pdf_reader=PyPDF2.PdfFileReader(obj_pdf)
# x = pdf_reader.numPages
# # El metodo siguiente obtiene la información de una página específica
# page_obj = pdf_reader.getPage(x-2)
# text = page_obj.extractText()

# file = open(r"1.txt","a")
# file.writelines(text)
# file.close()




# Leer todas las paginas pero la lectura no es muy eficiente


# def convert_pdf():

#     obj_pdf=open("RUT.pdf","rb")
#     pdf_reader=PyPDF2.PdfFileReader(obj_pdf)
#     x = pdf_reader.numPages
#     print(x)

#     for i in range(0,x-1):
#         # El metodo siguiente obtiene la información de una página específica
#         page_obj = pdf_reader.getPage(i)
#         text = page_obj.extractText()
#         print(text)
#         file = open(r"rut.docx","a")
#         file.writelines(text)
#         file.close()


#     print("terminado")


# convert_pdf()



#leer con una librería más eficiente.


# import fitz # install using: pip install PyMuPDF

# with fitz.open("RUT.pdf") as doc:
#     text = ""
#     for page in doc:
#         text += page.get_text()

# print(text)






#combinación de las dos anteriores


import fitz
import PyPDF2


def convert_pdf():

    obj_pdf=open("RUT.pdf","rb")
    pdf_reader=PyPDF2.PdfFileReader(obj_pdf)
    x = pdf_reader.numPages
    print(x)

    # for i in range(0,x-1):
        # page_obj = pdf_reader.getPage(i)
        # text = page_obj.extractText()
        # print(text)
        # file = open(r"rut.docx","a")
        # file.writelines(text)
        # file.close()

    with fitz.open("RUT.pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()
        
        file = open(r"rut.text","a")
        file.writelines(text)
        file.close()


    print("terminado")


convert_pdf()