# translation\Scripts\activate
from django.http import HttpResponse
from django.shortcuts import render
from googletrans import Translator
def index (request) :
    # translator = Translator()
    # translations = {}
    # translations = translator.translate('मख्खन लाल').text
    # print(translations)
    # return HttpResponse("Hello Geeks")
    if request.method == 'POST':
        val=request.POST['your_name']
        translator = Translator()
        translations = {}
        translations = translator.translate(val).text
        context = {"result1":translations}
        return render(request,'index.html',context)
    else:
        return render(request,'index.html')

