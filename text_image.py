import gradio as gr
from transformers import pipeline

summarize =pipeline('summarization',model="facebook/bart-large-cnn")
generated_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large") 
translation_pieline =pipeline("translation_en_to_fr",model="Helsinki-NLP/opus-mt-en-fr")
#function resume
def summarize_text(text):
    if text.strip() == "":
        return "Veuillez entrer un texte"
    summary =summarize(text,max_length=50,min_length=50,do_sample=False)
    summary_text =summary[0].get('summary_text')
    return summary_text

#function to load image
def image_load(image):
    if image is None:
        return "Veuillez televerser une image"
    result =generated_text(image)
    result_generate = translation_pieline(result[0]['generated_text'])

    return result_generate[0]['translation_text']

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