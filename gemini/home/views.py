from django.shortcuts import render,redirect,get_object_or_404
import os
from . import forms,models
import google.generativeai as geminiAI
from PIL import Image
geminiAI.configure(api_key="")
TextModel=geminiAI.GenerativeModel('gemini-pro')
ImgModel = geminiAI.GenerativeModel('gemini-pro-vision')
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
def IMGModel(r):
    result=""
    if r.method=="POST":
        frm=forms.IMG(r.POST,r.FILES)
        if frm.is_valid():
            image=models.IMGModel(IMG=frm.cleaned_data["IMG"])
            image.save()
            img=get_object_or_404(models.IMGModel,pk=image.pk)
            Open=Image.open(img.IMG.path)
            result=ImgModel.generate_content([Open,frm.cleaned_data["text"]]).text
            img.delete()
            os.remove(image.IMG.path)
    frm=forms.IMG()
    return render(r,"img.html",{"form":frm,"result":result})