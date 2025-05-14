import fitz
import pytesseract
from PIL import Image
import io

# Configurar tesseractor con la siguiente linea solamente si no lo tienes en PATH
# pytesseract.pytesseract.tesseract_cmd = r'<ruta tesseract>

def extract_text_from_pdf_images(pdf_path):
    pdf = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(pdf)):
        page = pdf.load_page(page_num)
        images = page.get_images(full=True)
        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = pdf.extract_image(xref)
            image_bytes = base_image["image"]
            image = Image.open(io.BytesIO(image_bytes))
            extracted_text = pytesseract.image_to_string(image, lang='spa')
            text += f"\nTexto de imagen {img_index+1} en pagina {page_num +1}:\n{extracted_text}\n"
    return text

pdf_path = "documento.pdf"
extracted_text = extract_text_from_pdf_images(pdf_path)
print(extracted_text)

