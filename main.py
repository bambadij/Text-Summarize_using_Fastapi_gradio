#load package
from transformers import pipeline
from fastapi import FastAPI,HTTPException,status
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
        summary = summarize(input.text,max_length=50,min_length=30,do_sample=False)
        summary_text =summary[0].get('summary_text')
        print(f"[iNFO] Input data as text:\n{summary_text}")
        logger.info(f"[INFO] input data:{input.text}")
        logger.info(f"[INFO] Summary:{summary}")
        return {
            "summary_text" :summary_text,
            "len_input" : len(input.text),
            "len_output" :len(summary_text)
        }
         

    except ValueError as e:
        logger.error(f"valueError:{e}")
        return {"error ER":str(e)}
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Could not summarize the input text.")
    

if __name__ == "__main__":
    uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)
