import fitz
from PIL import Image
import pytesseract
from transformers import pipeline
import gradio as gr

def extract_text_from_file(file):
    file_path = file
    print('*****print*****',file)
    if file_path is None:
         return extract_text_from_image(file_path)
    # elif file_path.endswith('.pdf'):
    #     return extract_text_from_pdf(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a PDF or image file.")

def extract_text_from_image(image_path):
    image =Image.open(image_path)
    text =pytesseract.image_to_string(image)

    return text

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        page =doc.load_page(page_num)
        text += page.get_text()

        return text
    
def summarize_text(text):
    summarizer = pipeline('summirization')
    summary =summarizer(text,max_length=150,min_length=25,do_sample=False)
    return summary[0]['summary_text']

def process_file(file_path):
    text =extract_text_from_file(file_path)
    summary =summarize_text(text)

    return summary
def gradio_interface(file):
    gradio_summary =process_file(file)
    return gradio_summary

input_file =gr.Image(type="pil"),
output_text = gr.Textbox(label="Summary")

interface = gr.Interface(
    fn=gradio_interface,
    inputs=gr.Image(type="pil"),
    outputs=output_text,
    title="Text Extract and Summarization"
)

interface.launch()
