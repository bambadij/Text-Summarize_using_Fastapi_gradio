#load package
from transformers import pipeline
from fastapi import FastAPI,HTTPException,status,UploadFile
from pydantic import BaseModel
import uvicorn
import logging



#Additional information
 
Informations = """ 
-text : Texte à resumé

output:
- Text summary : texte resumé
"""



app =FastAPI(
    title='Text Summary',
    description =Informations
)

#class to define the input text
logging.basicConfig(level=logging.INFO)
logger =logging.getLogger(__name__)
summarize =pipeline('summarization', model="facebook/bart-large-cnn")
generated_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large") 
translation_pieline =pipeline("translation_en_to_fr",model="Helsinki-NLP/opus-mt-en-fr")
classify_zero_shot = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

class TextSummary(BaseModel):
    text:str

#ENDPOINT

@app.get("/")
async def home():
    return 'STN BIG DATA'


@app.post("/summary")
async def summary_text_bart(input:TextSummary):
    "add text to summarize"
    try:
        summary = summarize(input.text,do_sample=False)
        summary_text =summary[0].get('summary_text')
        result = classify_zero_shot(
                summary_text,
                candidate_labels=["En Cours", "Non traiter", "Terminer"],
                hypothesis_template="Cet Resumé est sur {}."
            )
        print(f"[iNFO] Input data as text:\n{summary_text}")
        logger.info(f"[INFO] input data:{input.text}")
        logger.info(f"[INFO] Summary:{summary}")
        formatted_result = [
            f"{label}: {score:.2f}" for label, score in zip(result['labels'], result['scores']*100)
        ]
        return {
            "summary_text" :summary_text,
            "Statut":formatted_result,
            # "format":formatted_result,
            "len_input" : len(input.text),
            "len_output" :len(summary_text)

        }
         

    except ValueError as e:
        logger.error(f"valueError:{e}")
        return {"error ER":str(e)}
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Could not summarize the input text.")
    
# @app.post("/image_to_text")
# async def image_to_text(file:UploadFile):
#     "Televerser une image"
#     try:
#         content =await file.read()
#         image =Image.open(io.BytesIO(content))
#         resultat_legend =generated_text(image)
#         result_on_translate=translation_pieline(resultat_legend[0]['generated_text'])
        
#         extract_text = result_on_translate[0]['translation_text']
#         return {"text-generate":extract_text}
#     except ValueError as e:
#         logger.error(f"valueError:{e}")
#         return {"error ER":str(e)}

#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Could not work.")

if __name__ == "__main__":
    uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)




