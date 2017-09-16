from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect

from .models import Paragraph, Result
from .forms import ResultForm

# Create your views here.


class QuestionView(View):
    def get(self, request):
        if Paragraph.objects.filter(count=0).count() > 0:
            paragraph = Paragraph.objects.filter(count=0)[0]
        elif Paragraph.objects.filter(count=1).count() > 0:
            paragraph = Paragraph.objects.filter(count=1)[0]
        elif Paragraph.objects.filter(count=2).count() > 0:
            paragraph = Paragraph.objects.filter(count=2)[0]
        elif Paragraph.objects.filter(count=3).count() > 0:
            paragraph = Paragraph.objects.filter(count=3)[0]
        else:
            paragraph = Paragraph(id="nothing", paragraph="nothing", count=404)
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
                    result.paragraph_id = paragraph_id
                    result.paragraph = paragraph.paragraph
                    result.save()
                    return HttpResponseRedirect("/question/")
                else:
                    return render(request, "question.html", {"msg": "答案必须在文段中出现", "paragraph": paragraph})
            else:
                return render(request, "question.html", {"msg": "问题或答案不可为空", "paragraph": paragraph})
        else:
            return HttpResponseRedirect('/')
