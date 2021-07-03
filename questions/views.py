from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings

class QuestionView(TemplateView):
    template_name = 'questions/ask_question.html'
    print(template_name)

def send_question(request):
    if request.method == 'GET':
        return(request, 'questions/ask_question.html')
    else:
        print("EMAIL")
        print(request.POST)
        from_email = request.POST['email-address']
        subject = 'سوال ' + request.POST['full-name'] + ' - ' + from_email 
        message = request.POST['message']
        
        sender_email = settings.EMAIL_HOST_USER
        red = 'red'
        blue = 'blue'
        if request.POST['full-name'] == '' or message == '' or from_email == '':
            error_message = 'لطفا تمام خانه ها را پر نمایید'
            return render(request, 'questions/ask_question.html', {'message': error_message, 'color': red})
            
        try:
            send_mail(subject, message, sender_email, ['hayaatreciever@gmail.com'])
        except BaseException as e:
            print(e)
            error_message = 'خطا در سرور، لطفا بعدا کوشش نمایید'
            return render(request, 'questions/ask_question.html', {'message': error_message, 'color': red})

        success_message = 'سوال تان با موفقیت ارسال شد، سوال دیگر دارید؟'
        return render(request, 'questions/ask_question.html', {'message': success_message, 'color': blue})
    


