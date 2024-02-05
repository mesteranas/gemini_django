from django.shortcuts import render,redirect
from . import forms
import google.generativeai as geminiAI
geminiAI.configure(api_key="AIzaSyA_u8y8SJNAyai76DWLDin5mWi3VPemOgY")
TextModel=geminiAI.GenerativeModel('gemini-pro')
# Create your views here.
def home_(r):
    return render(r,"home.html")
def Contect(r):
    return render(r,"contect.html")
def about(r):
    return render(r,"about.html")
def text(r):
    result=""
    if r.method=="POST":
        try:
            message=r.POST["message"]
            result=TextModel.generate_content(message).text
        except:
            result="error"
    return render(r,"text.html",{"result":result})