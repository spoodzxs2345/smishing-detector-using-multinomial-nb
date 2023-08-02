# Smishing Detection Model Using MultinomialNB
![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/AI-Pandas-informational?style=flat&logo=pandas&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/AI-ScikitLearn-informational?style=flat&logo=scikitlearn&logoColor=white&color=2bbc8a)

> *Note: I did not include the model/pickle in the `.gitignore` so that the Streamlit demo will work.*

This model is for detection of smishing messages. You can use the [demo](https://smishing-detector-using-multinomial-nb-demo.streamlit.app/) to have some glimpse on how the model works.

# 📖 Storytime
This project was made for my internship. I was not required to do it, but I thought maybe I can use my tip-of-the-iceberg data science skill in my role (security governance). The reason is that there was this one time where the whole company was affected by a smishing attack. There was a response, sure, but I see it as too late. A victim was alrady prompted to click the link included in the smishing message. Seeing that, I thought, what if they have this AI model embedded in their messaging apps that can detect smishing messages? What if there's an AI integration in reporting smishing attacks to the Cyber Incident Response Group? And so, I made this smishing detection model.

# 🤖 About the model
I used **Multinomial Naive Bayes** for my classification algorithm. MultinomialNB is a probabilistic learning method that is mostly used in text classification. I also used **CountVectorizer** to convert the text messages into a matrix of token counts. These tokens are words or phrases that are used as features of the text messages. I have also pipelined the model so that the preprocessing will be consistent and the inference will be easier.

# 💻 Suggested Use Cases
- **Implementation on messaging apps** - This model can be used to block or automatically report smishing messages to the Cybersecurity Department in advance for immediate actians.
- **Background Application** - This model can be integrated in a background application that detects smishing messages.
