# TEXT SUMMARIZE USING GRADIO AND API CREATION WITH FASTAPI


## Description

**Text summary** Text Summary is an application created as an effective tool for resuming texts automatically and quickly, which selects the most relevant information from your books or texts and will allow you to optimize your time.: 
- In this project we use the Facbook model Bart on Hugging Face : ['huggingface'](https://huggingface.co/facebook/bart-large-cnn)

## FastAPI Setup

Install des Packages.

You need to have [`Python 3`](https://www.python.org/) on your system (**Python version 3.11 was used**). Then you can clone this repo and being at the repo's `root :: repository_name> ...`  follow the steps below:

- Clone 
        git clone https://github.com/bambadij/Text-Summarize_using_Fastapi_gradio.git
        cd Text-Summarize_using_Fastapi_gradio

- Activate de virtual Environnement
- Windows:
        
        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

- Linux & MacOs:
        
        python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

The two long command-lines have the same structure. They pipe multiple commands using the symbol ` ; ` but you can manually execute them one after the other.

1. **Create the Python's virtual environment** that isolates the required libraries of the project to avoid conflicts;
2. **Activate the Python's virtual environment** so that the Python kernel & libraries will be those of the isolated environment;
3. **Upgrade Pip, the installed libraries/packages manager** to have the up-to-date version that will work correctly;
4. **Install the required libraries/packages** listed in the `requirements.txt` file so that they can be imported into the python script and notebook without any issue.

**NB:** For MacOs users, please install `Xcode` if you have an issue.

## Run FastAPI

- Run the API (being at the repository root):
        
  FastAPI:
    
    - Main

          uvicorn main:app --reload 

    <!-- - Sepsis prediction

          uvicorn src.main:app --reload  -->


  - Go to your browser at the following address, to explore the API's documentation :
        
      http://127.0.0.1:8000/docs

## Run Gradio 
    -App 
        python app.py

    -Go to your browser at the following address, to explore the API's documentation :
        http://127.0.0.1:7860/

## FastAPI  and Gradio Preview

Below is a preview showcasing some features of the FastAPI:

<div style="display: flex; align-items: center;">
    <div style="flex: 33.33%; text-align: center;">
        <p>FastAPI Top</p>
             <img src="https://github.com/bambadij/Text-Summarize_using_Fastapi_gradio/blob/main/image/fastapi.PNG" alt="Middle" width="90%"/>
    </div>
    <div style="flex: 33.33%; text-align: center;">
        <p>FastAPI Input</p>
             <img src="https://github.com/bambadij/Text-Summarize_using_Fastapi_gradio/blob/main/image/output.PNG" alt="Top" width="90%"/>
        </div>
    <div style="flex: 33.33%; text-align: center;">
        <p>GRADIO Preview</p>
        <img src="https://github.com/bambadij/Text-Summarize_using_Fastapi_gradio/blob/main/image/gradio.PNG" alt="Middle" width="90%"/>
        </div>
</div>

