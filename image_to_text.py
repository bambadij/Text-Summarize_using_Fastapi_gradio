# Use a pipeline as a high-level helper
from transformers import pipeline
import gradio as gr
# Use a pipeline as a high-level helper
# import torch
# from PIL import Image
 
generated_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large") 
def image_to_text(image):
  # Pre-process image
    # pipeline_traduction = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")

    resultats_legende = generated_text(image)

    legende_anglaise = resultats_legende[0]['generated_text']
    # print(legende_anglaise)
    # legende_francaise = pipeline_traduction(legende_anglaise, max_length=512)
    # texte_francais = legende_francaise[0]['translation_text']
    return legende_anglaise

interface = gr.Interface(fn=image_to_text,
                        inputs=gr.Image(type="pil"),
                        outputs=gr.Textbox(),
                        title="Image to text")
if __name__ == "__main__":
    interface.launch()
