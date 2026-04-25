from flask import Flask,render_template,url_for,request,jasonify
import os
from dotenv import load_env
from openai import OpenAI
load_env()
api_key=os.getenv("OPEN_AI_API")

client=OpenAI(api_key=api_key)

app=Flask(__name__)
@app.route("/")
def hello_world():
    return render_template("index.html")
@app.route("/ask" ,methods=["POST"])
def ask():
    question=request.form.get("question")
    response=client.responses.create(
        model="gpt-5.4",
        input=[
            {"role":"system","content":"Act like a personal helpful assistant."},
            {"role":"user","content":question}
        ],temperature=0.7,
        max_output_tokens=512
    )
    answer=response.output_text.strip()
    return jasonify({"response":answer}),200
@app.route("/summarise" ,methods=["POST"])
def summarise():
    email_text=request.form.get("email")
    prompt=f"Summarise the following email in 2-3 lines :{email_text}"
    response=client.responses.create(
        model="gpt-5.4",
        input=[
            {"role":"system","content":"Act like an personal email summarizer"},
            {"role":"user","content":prompt}
        ],temperature=0.3,
        max_output_tokens=512
    )
    answer=response.output_text.strip()
    return jasonify({"response":answer}),200
if __name__=="__main__":
    app.run(debug=True)
    