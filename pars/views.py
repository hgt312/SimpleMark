from random import randint

from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect

from .models import Paragraph, Result
from .forms import ResultForm

# Create your views here.


class QuestionView(View):
    def get(self, request):
        last = Paragraph.objects.count() - 1
        while True:
            index = randint(0, last)
            paragraph = Paragraph.objects.all()[index]
            if paragraph.count < 10:
                return render(request, "question.html", {"paragraph": paragraph})

    def post(self, request):
        if request.user.is_authenticated():
            result_form = ResultForm(request.POST)
            paragraph_id = request.POST.get("paragraph_id", "")
            paragraph = Paragraph.objects.get(id=paragraph_id)
            if result_form.is_valid():
                question = request.POST.get("question", "")
                answer = request.POST.get("answer", "")
                text = paragraph.paragraph
                if answer in text:
                    result = Result()
                    result.question = question
                    result.answer = answer
                    result.user = request.user
                    result.paragraph = paragraph
                    result.save()
                    return HttpResponseRedirect("/question/")
                else:
                    return render(request, "question.html", {"msg": "答案必须在文段中出现", "paragraph": paragraph})
            else:
                return render(request, "question.html", {"msg": "问题或答案不可为空", "paragraph": paragraph})
        else:
            return HttpResponseRedirect('/')
