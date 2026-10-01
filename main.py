from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import recommend_learning_path


app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


@app.post("/qa", response_class=HTMLResponse)
async def qa(request: Request, question: str = Form(...)):
    result = answer_question(question)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "result": result
        }
    )


@app.post("/explain", response_class=HTMLResponse)
async def explain(request: Request, topic: str = Form(...)):
    result = explain_topic(topic)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "result": result
        }
    )


@app.post("/quiz", response_class=HTMLResponse)
async def quiz(request: Request, topic: str = Form(...)):
    result = generate_quiz(topic)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "result": result
        }
    )


@app.post("/summarize", response_class=HTMLResponse)
async def summarize(request: Request, text: str = Form(...)):
    result = summarize_text(text)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "result": result
        }
    )


@app.post("/learn/recommendations", response_class=HTMLResponse)
async def learning_path(request: Request, topic: str = Form(...)):
    result = recommend_learning_path(topic)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "result": result
        }
    )