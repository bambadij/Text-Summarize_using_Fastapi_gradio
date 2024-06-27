import gradio as gr
from transformers import pipeline
from pytesseract import image_to_string 
from PIL import Image
from io import BytesIO
import pytesseract

summarize =pipeline('summarization',model="facebook/bart-large-cnn")
# generated_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large") 
# translation_pieline =pipeline("translation_en_to_fr",model="Helsinki-NLP/opus-mt-en-fr")
#function resume


def summarize_text(text,image):
    if text.strip() == "":
        return "Veuillez entrer un texte"
    if image is None:
        return "Veuillez televerser une image"
    summary =summarize(text,do_sample=False)
    summary_text =summary[0].get('summary_text')
    return summary_text


# def image_load(image):
#     if image is None:
#         return "Veuillez téléverser une image"
#     try:
#         image_open = Image.open(image)
#         raw_text = pytesseract.image_to_string(image_open)
#         return raw_text
#     except Exception as e:
#         return str(e)

    # result =pytesseract.image_to_string(image_open)
    # result =generated_text(image)
    # result_generate = translation_pieline(result[0]['generated_text'])

    #  return result
def image_load(image):
    try:
        image_open = Image.open(BytesIO(image.read()))
        raw_text = pytesseract.image_to_string(image_open, lang='fra')
        # summary = summarizer(raw_text, do_sample=False)
        # summary_text = summary[0].get('summary_text')
        return raw_text
    except Exception as e:
        return str(e)


#function to handle the input
def handle_input(text_input,image_input,mode):
    if mode == "Summary" :
        return summarize_text(text_input)
    elif mode == "Image":
        return image_load(image_input)
    else:
        return "Selectionner une option valide"
    
#let's create our gradio interface

with gr.Blocks() as iface:
    gr.Markdown("## Selection une options")
    mode =gr.Radio(choices=["Summary","Image"],label="Mode")
    text_input =gr.Textbox(label="Entrée de texte")
    image_input =gr.Image(label="Televerser une image",type="pil")

    #create a sum                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       bit bouton
    submit_btn =gr.Button("Soumettre")

    output =gr.Textbox(label="Resultat") 

    def update_inputs(mode_select):
        if mode_select =="Summary":
            return gr.update(visible=True),gr.update(visible=False)
        
        elif mode_select == "Image":
            return gr.update(visible=False),gr.update(visible=True)

    mode.change(fn=update_inputs,inputs=mode,outputs=[text_input,image_input])
    submit_btn.click(fn=handle_input,inputs=[text_input,image_input,mode],outputs=output)

if __name__ == "__main__":
    iface.launch()