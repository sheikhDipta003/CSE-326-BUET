from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from nurses.models import MemberAppoint, MedicineChart,Medicine,Dosage, SpecialCheckupScheduletwo, CheckupSchedule,ResidentMedCond,Member
from residents.models import CheckupItem,MedCond
from django.shortcuts import render
from django.views import View

class DashboardView(View):
    template_name = 'doctors/dashboard.html'  # Update with your actual template name

    def getAppointments(self, doctor_id, order_by_date=False):
        appointments = MemberAppoint.objects.filter(Doctor_ID=doctor_id)
        if order_by_date:
            appointments = appointments.order_by('Date')
        return appointments

    def getCheckups(self, doctor_id, order_by_date=False):
        checkups = CheckupSchedule.objects.filter(Doctor_ID=doctor_id, Completed=False)
        special_checkups = SpecialCheckupScheduletwo.objects.filter(Doctor_ID=doctor_id, Completed=False)
        if order_by_date:
            checkups = checkups.order_by('Date')
            special_checkups = special_checkups.order_by('Date')
        return checkups, special_checkups

    def get(self, request, doctor_id, *args, **kwargs):
        order_by_date = request.GET.get('order_by_date')

        # Get appointments and checkups
        appointments = self.getAppointments(doctor_id, order_by_date)
        regular_checkups, special_checkups = self.getCheckups(doctor_id, order_by_date)

        return render(request, self.template_name, {
            'appointments': appointments,
            'regular_checkups': regular_checkups,
            'special_checkups': special_checkups,
            'order_by_date': order_by_date,
        })

class addSuggesions(View):
    template_name = 'doctors/addPrescription.html'  # Update with your actual template name
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def addPrescription(self, request, member_id):
        if request.method == 'POST':
            # Get data from the POST request
            medicine_name = request.POST.get('medicine_name')
            time = request.POST.get('time')
            quantity = request.POST.get('quantity')
            duration= request.POST.get('duration')
            date = request.POST.get('date')

            medicine_id = Medicine.objects.filter(Name=medicine_name)

            new_instance = MedicineChart(Member_id=member_id, Date=date)
            new_instance.save()

            chart_id=new_instance.Chart_id

            instance = Dosage(Chart_id=chart_id, Medicine_id=medicine_id, Time=time, Quantity=quantity)
            instance.save()
            return redirect('success_page')
    
class createAppointment(View):
    template_name = 'doctors/createAppointment.html'  # Update with your actual template name
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def addAppointment(self, request, doctor_id,member_id):
        if request.method == 'POST':
            # Get data from the POST request
            member_id = request.POST.get('member_id')
            time = request.POST.get('time')
            date = request.POST.get('date')

            new_instance = MemberAppoint(Member_ID=member_id, Doctor_ID=doctor_id)
            new_instance.save()
            return redirect('success_page')
    def addSpecialCheckup(self, request,doctor_id,member_id):
        if request.method == 'POST':
            # Get data from the POST request
            bp = request.POST.get('blood_pressure')
            sugar = request.POST.get('sugar')
            hr = request.POST.get('heartrate')
            frequency = request.POST.get('frequency')
            date = request.POST.get('date')
            time = request.POST.get('time')

            member = Member.objects.filter(Member_Id=member_id)
            checkup = SpecialCheckupScheduletwo(Member_Id=member_id, Doctor_ID=doctor_id,Nurse_Id=member.Assigned_nurse,
                                              Date=date,Frequency=frequency,Completed=False, Exact_time=time)
            checkup.save()
        
            checkupItem=CheckupItem(Checkup_Id=checkup.Checkup_Id,Blood_Pressure=bp,Sugar=sugar,Heartrate=hr)
            checkupItem.save()

class checkup_report_status_view(View):
    template_name = 'doctors/CheckupReportStatus.html'  # Update with your actual template name
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class member_condition_view(View):
    template_name = 'doctors/member_condition.html'  # Update with your actual template name
    def get(self, request,member_id, *args, **kwargs):
        member_info=Member.objects.get(Member_ID=member_id)
        conditions=ResidentMedCond.objects.filter(Member_ID=member_id)
        
        data=[]
        for condition in conditions:
            med_cond=MedCond.objects.get(Cond_ID=condition.Cond_ID_id)
            print(med_cond)
            data.append({
                'name':med_cond.Name,
                'advice':med_cond.Advice,
                'guideline':med_cond.Guideline
            })
            
        checkups=CheckupSchedule.objects.filter(Member_Id=member_id)
        checkupItems=[]
        for checkup in checkups:
            checkup_item=CheckupItem.objects.get(Checkup_Id=checkup.Checkup_Id_id)
            checkupItems.append({
                'bp':checkup_item.Blood_Pressure,
                'sugar':checkup_item.Sugar,
                'hr':checkup_item.Heartrate,
                'date':checkup.Date
            })
            
        return render(request, self.template_name,{'conditions':data,'checkup_results':checkupItems,'member_info':member_info})

class nurse_schedule_view(View):
    template_name = 'doctors/NursesSchedule.html'  # Update with your actual template name
    def get(self, request,member_id, *args, **kwargs):
        info=Member.objects.get(Member_ID=member_id)
        return render(request, self.template_name,{'info':info})
    
    def post(self, request,member_id, *args, **kwargs):
        if request.method == 'POST':
            # Get data from the POST request
            id = request.POST.get('Member_ID')
            date = request.POST.get('Date')
            freq = request.POST.get('Frequency')

            member = Member.objects.get(Member_ID=id)
            print(member)
            # nurse_id=member.objects.
            checkup = SpecialCheckupScheduletwo.objects.create(Member_Id=member, Doctor_ID=member.Assigned_doctor,Nurse_Id=member.Assigned_nurse,
                                              Date=date,Frequency=freq,Completed=False)
            # checkup = SpecialCheckupScheduletwo(Member_Id=member, Doctor_ID=member.Assigned_doctor,Nurse_Id=member.Assigned_nurse,
            #                                   Date=date,Frequency=freq,Completed=False)
            checkup.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'error': 'Invalid request'})
    
class prescription_view(View):
    template_name = 'doctors/Prescription.html'  # Update with your actual template name
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class resident_status_view(View):
    template_name = 'doctors/ResidentStatus.html'  # Update with your actual template name

    def getMembers(self):
        members=Member.objects.filter(Assigned_doctor=1).order_by('riskrate')
        return members

    def get(self, request, *args, **kwargs):
        members=self.getMembers()
        return render(request, self.template_name, {'members': members})