from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login


# Create your views here.
def home(request):
    return render(request, 'baseapp/index.html')

def donate(request):
    return render(request, 'baseapp/donate.html')

def requestfund(request):
    # try:
    #     if request.method=='POST':  
    #         p_name=request.POST.get('patientName')
    #         p_age=request.POST.get('age')
    #         p_gender=request.POST.get('gender')
    #         p_phone=request.POST.get('contactPatient')
    #         p_email=request.POST.get('emailPatient')
    #         p_bloodgroup=request.POST.get('bloodgroupPatient')
    #         p_healthissue=request.POST.get('healthissue')
    #         p_hospitalcondition=request.POST.get('hospitalCondition')
    #         p_fundamount=request.POST.get('fundAmount')
    #         p_drecommend=request.POST.get('drecommend')
    #         p_wrecommend=request.POST.get('wrecommend')

    #         d_name=request.POST.get('doctorName')
    #         d_hospitalname=request.POST.get('hospitalName')
    #         d_phone=request.POST.get('contactDoctor')
    #         d_email=request.POST.get('emailDoctor')
    #         d_specialization=request.POST.get('specialization')

    #         doctors=Doctor.objects.create(doctorName=d_name, hospitalName=d_hospitalname, contactDoctor=d_phone, emailDoctor=d_email, specialization=d_specialization)

    #         doctors.save()

    #         patients=Patient.objects.create(patientName=p_name, age=p_age, gender=p_gender, contactPatient=p_phone, emailPatient=p_email, bloodgroupPatient=p_bloodgroup,  healthissue=p_healthissue, hospitalCondition=p_hospitalcondition, fundAmount=p_fundamount, drecommend=p_drecommend, wrecommend=p_wrecommend)

    #         patients.save()

    # except:
    #     pass
    return render(request, 'baseapp/requestfund.html')

def about(request):
    return render(request,'baseapp/about.html')

def requestlanding(request):
    
        if request.method=='POST':  
            p_name=request.POST.get('patientName')
            p_age=request.POST.get('age')
            p_gender=request.POST.get('gender')
            p_phone=request.POST.get('contactPatient')
            p_email=request.POST.get('emailPatient')
            p_bloodgroup=request.POST.get('bloodgroupPatient')
            p_healthissue=request.POST.get('healthissue')
            p_hospitalcondition=request.POST.get('hospitalCondition')
            p_fundamount=request.POST.get('fundAmount')
            p_drecommend=request.POST.get('drecommend')
            p_wrecommend=request.POST.get('wrecommend')

            d_name=request.POST.get('doctorName')
            d_hospitalname=request.POST.get('hospitalName')
            d_phone=request.POST.get('contactDoctor')
            d_email=request.POST.get('emailDoctor')
            d_specialization=request.POST.get('specialization')

            doctors=Doctor.objects.create(doctorName=d_name, hospitalName=d_hospitalname, contactDoctor=d_phone, emailDoctor=d_email, specialization=d_specialization)

            doctors.save()

            patients=Patient.objects.create(patientName=p_name, age=p_age, gender=p_gender, contactPatient=p_phone, emailPatient=p_email, bloodgroupPatient=p_bloodgroup,  healthissue=p_healthissue, hospitalCondition=p_hospitalcondition, fundAmount=p_fundamount, drecommend=p_drecommend, wrecommend=p_wrecommend)

            patients.save()

            return redirect('requestlanding')

        else:
            return render(request, 'baseapp/requestfund.html')


def donatelanding(request):
    return render(request, 'baseapp/donatelanding.html')

def contact(request):
    return render(request, 'baseapp/contact.html')