import PyPDF2

# Ruta al archivo PDF que deseas abrir
pdf_file_path = r'C:\Users\ramon\OneDrive\Desktop\Tesseract\Portada.pdf'

# Inicializar una variable para almacenar el texto
text = ''

# Abrir el archivo PDF
with open(pdf_file_path, 'rb') as pdf_file:
    # Crear un objeto PdfReader en lugar de PdfFileReader
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Leer cada página del PDF
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

# Imprimir o almacenar el texto en una variable
print(text)

