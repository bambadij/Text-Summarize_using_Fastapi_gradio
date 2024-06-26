# Use a pipeline as a high-level helper
from transformers import pipeline
import gradio as gr
# Use a pipeline as a high-level helper
import torch

 

def summarize_text_bart_(text):
    summarize =pipeline('summarization',model="facebook/bart-large-cnn")

    summary = summarize(text,do_sample=False)
    summary_text =summary[0].get('summary_text')
    return summary_text

interface = gr.Interface(fn=summarize_text_bart_, 
                        # inputs="textbox",
                        inputs=gr.Textbox(lines=10, placeholder="Entrer votre Texte ici..."),
                        outputs="textbox",
                        title="Résumé des Plaintes")
interface.launch()
