#  QwenPrompt Lab

### An Interactive Prompt Engineering Application

QwenPrompt Lab is a Python and Streamlit application that demonstrates different prompt engineering techniques using the Qwen2.5 Large Language Model.

##  Features

- Interactive Streamlit interface
- Six prompting techniques: Zero-shot, One-shot, Few-shot, CoT, Manual CoT, and ToT
- Generated prompt preview
- Adjustable temperature and maximum tokens
- AI-generated responses using a local Qwen model

## Application link: https://qwenprompt-lab-gmgvfgdhjl5dhnk7qr2drg.streamlit.app/

## Application Preview
<img width="1355" height="711" alt="image" src="https://github.com/user-attachments/assets/483969b2-95b6-4d54-9131-0bdc8968bf91" />
<img width="1337" height="715" alt="image" src="https://github.com/user-attachments/assets/e53b64d2-f652-416a-8b0a-9e58203c5bdc" />
<img width="1362" height="694" alt="image" src="https://github.com/user-attachments/assets/cbe0c7f5-1467-4501-9f78-73436eff9064" />



  

##  Technologies Used

- Python
- Streamlit
- Ollama
- Qwen2.5
- Requests

##  Project Structure

```text
QwenPrompt-Lab/
├── app.py
├── llm.py
├── prompt_templates.py
├── requirements.txt
├── .gitignore
└── README.md
```

##  Installation and Usage

1. Install Python and [Ollama](https://ollama.com/download/windows).
2. Download the Qwen model:

   ```bash
   ollama pull qwen2.5:3b
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python -m streamlit run app.py
   ```

5. Open the displayed local URL in your browser.

##  Objective

To understand and experiment with different prompt engineering techniques and learn how they influence AI-generated responses.

##  Future Enhancements

- Compare responses from different techniques.
- Add prompt history and export options.
- Support additional language models.

##  Author

**R.NIKITHA**

