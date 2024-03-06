from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html')

def send_email(request):
    if request.method == 'POST':
        #name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # Rest of your code goes here
   
        ''' 
        send_mail('subject',
                  'message',
                  'grajesh2906@gmail.com',
                  ('email','grajesh2961@gmail.com'),
                  fail_silently=False)
        #return  HttpResponse("Email Sent")
        return render(request,'user_details.html') 
        '''
    
        send_mail(
            'Hey,There',  # subject
            'Im a Rajesh Gangadharam A Passionate Computer science student at Xyz Univercity',  # body
            'grajesh2906@gmail.com',  # sender Email Address
            ['grajesh2907@gmail.com', 'grajesh2961@gmail.com'],  # It will add CC to all members
            fail_silently=False
        )
    
    #return HttpResponse("Email sent Successfully")
    alert_message="Email sent successfully"
    return render(request, 'home.html',{'alert_message':alert_message})
