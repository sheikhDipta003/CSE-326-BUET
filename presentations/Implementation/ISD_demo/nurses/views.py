from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from datetime import date  # Import the datetime module
from .models import Member,Nurse
from .models import Medicine, MedicineChart,Dosage,CheckupSchedule,SpecialCheckupScheduletwo,SpecialCheckupItem
from residents.models import CheckupItem
from doctors.models import Doctor
def getSugarRiskrate(sugar):
    riskrate = 0
    if (sugar >= 5 and sugar <= 6.5):
        riskrate = 0
    elif (sugar >= 6.5 and sugar <= 6.9):
        riskrate = 1
    elif (sugar >= 7 and sugar <= 12):
        riskrate = 2
    elif (sugar >= 12):
        riskrate = 3
    return riskrate

def getBpRiskrate(systolic_bp, diastolic_bp):
    riskrate = 0
    if systolic_bp >= 115 and systolic_bp <= 125 and diastolic_bp >= 75 and diastolic_bp <= 85:
        riskrate = 0
    elif systolic_bp >= 125 and systolic_bp <= 135 and diastolic_bp >= 85 and diastolic_bp <= 90:
        riskrate = 1
    elif systolic_bp >= 135 and systolic_bp <= 160 and diastolic_bp >= 90 and diastolic_bp <= 100:
        riskrate = 2
    elif systolic_bp >= 160 and diastolic_bp >= 100:
        riskrate = 3
    return riskrate
class DashboardView(View):
    template_name = 'nurses/dashboard.html'
    # Dynamically get today's date
    # current_date = date.today().strftime("%Y-%m-%d")
    current_date='2023-09-05'

    def get(self, request, nurse_id, *args, **kwargs):
        
        # Fetch all members assigned to the nurse
        members = Member.objects.filter(Assigned_nurse=nurse_id)

        # Create a list to store medication information for each member
        medication_info = []

        # Loop through the members and fetch medication info for each
        for member in members:
            # Fetch medication chart for the member
            medicine_charts = MedicineChart.objects.filter(Member_ID=member.Member_ID)

            for chart in medicine_charts:
                # Fetch dosages for each chart
                dosages = Dosage.objects.filter(Chart_id=chart.Chart_id)

                for dosage in dosages:
                    # Fetch medicine details
                    medicine = Medicine.objects.get(Medicine_id=dosage.Medicine_id_id)

                    # Create a dictionary to store medication info
                    medication_data = {
                        'member_name': member.Name,
                        'member_room_no': member.Room_no,
                        'medicine_name': medicine.Name,
                        'medicine_mg': medicine.Mg,
                        'medicine_company': medicine.Company,
                        'medicine_available': medicine.Available,
                        'chart_date': chart.Date,
                        'dosage_time': dosage.Exact_time,
                        'dosage_quantity': dosage.Quantity,
                    }

                    # Append the medication info to the list
                    medication_info.append(medication_data)

        # Fetch checkup data for all members
        checkup_data = self.getCheckupSchedule(members)
        checkup_data_special=self.getSpecialCheckupSchedule(members)
        # Render the template with the medication and checkup info
        return render(request, self.template_name, {'medication_info': medication_info, 'checkup_data': checkup_data, 'checkup_data_special': checkup_data_special,'nurse_id': nurse_id})

    def getCheckupSchedule(self, members):
        current_date='2023-09-05'
        # Initialize an empty list to store checkup data
        checkup_data = []

        # Loop through the members and fetch checkup data for each
        for member in members:
            # Fetch checkup schedule for the member
            checkup_schedules = CheckupSchedule.objects.filter(Member_Id=member.Member_ID, Date=current_date,Completed=False)
            for schedule in checkup_schedules:
                # Fetch the corresponding checkup item
                checkup_item = CheckupItem.objects.get(Checkup_Id=schedule.Checkup_Id_id)
                items=[]
                if checkup_item.Blood_Pressure :
                    items.append("Blood pressure check")
                if checkup_item.Sugar:
                    items.append("Sugar check")
                if checkup_item.Heartrate:
                    items.append("Heartrate check")
                
                # Create a dictionary to store checkup data
                checkup_data.append({
                    'member_id': member.Member_ID,
                    'member':member.Name,
                    'items': items,
                    'time': schedule.Exact_time,
                    'checkup_id':schedule.Checkup_Id_id
                })

        return checkup_data
    def getSpecialCheckupSchedule(self, members):
        current_date='2023-09-07'
        # Initialize an empty list to store checkup data
        checkup_data = []

        # Loop through the members and fetch checkup data for each
        for member in members:
            print("aurin")
            # Fetch checkup schedule for the member
            checkup_schedules = SpecialCheckupScheduletwo.objects.filter(Member_Id=member.Member_ID, Date=current_date,Completed=False)
            print(checkup_schedules)
            for schedule in checkup_schedules:
                # Fetch the corresponding checkup item
                # print('charu')
                # checkup_item = SpecialCheckupItem.objects.get(Special_Checkup_Item_Id=schedule.Special_Checkup_Id)
                # items=[]
                # if checkup_item.Blood_Pressure :
                #     items.append("Blood pressure check")
                # if checkup_item.Sugar:
                #     items.append("Sugar check")
                # if checkup_item.Heartrate:
                #     items.append("Heartrate check")
                
                # Create a dictionary to store checkup data
                    
                checkup_data.append({
                    'member_id': member.Member_ID,
                    'member':member.Name,
# 'items': items,
# 'time': checkup_schedules.Exact_time,
                    'date':schedule.Date,
                    'checkup_id':schedule.Special_Checkup_Id,
                    'frequency':schedule.Frequency
            # 'checkup_sched':checkup_schedules.Frequency
                })

        return checkup_data
    

class CheckupDataEntryView(View):
    template_name = 'nurses/addCheckupData.html'  # Update with your actual template name
    
    def get(self, request, checkup_id, *args, **kwargs):
        return render(request, self.template_name, {'checkup_id':checkup_id})
    
    

    def post(self, request, checkup_id, *args, **kwargs):
        if request.method == 'POST':
            # Get data from the POST request
            bp_input = request.POST.get('Blood_pressure')
            sugar = float(request.POST.get('Sugar'))
            hr = int(request.POST.get('Heartrate'))

            # Split the blood pressure input into systolic and diastolic values
            systolic_bp, diastolic_bp = map(int, bp_input.split('/'))
            bpRisk = self.getBpRiskrate(systolic_bp, diastolic_bp)
            sugarRisk = self.getSugarRiskrate(sugar)
            risk = max(bpRisk, sugarRisk)
            
            # Create CheckupItem
            checkup=CheckupSchedule.objects.get(Checkup_Id=checkup_id)
            checkupItem = CheckupItem.objects.get(Checkup_Id=checkup_id)
            
            checkupItem.Blood_Pressure=bp_input
            checkupItem.Sugar=sugar
            checkupItem.Heartrate=hr
            checkupItem.save()
            
            checkup.Risk_rate=risk
            checkup.Completed=True
            checkup.save()
            # Retrieve the Member and Nurse instances
            member = Member.objects.get(Member_ID=checkup.Member_Id_id)
            
            member.riskrate=risk
            member.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'error': 'Invalid request'})
class CheckupDataSpecialEntryView(View):
    template_name = 'nurses/addCheckupData_Special.html'  # Update with your actual template name

    def get(self, request, checkup_id, *args, **kwargs):
        return render(request, self.template_name, {'checkup_id': checkup_id})

    def post(self, request, checkup_id, *args, **kwargs):
        if request.method == 'POST':
            # Get data from the POST request
            bp_input = request.POST.get('Blood_pressure')
            sugar = float(request.POST.get('Sugar'))
            hr = int(request.POST.get('Heartrate'))

            # Split the blood pressure input into systolic and diastolic values
            
            systolic_bp, diastolic_bp = map(int, bp_input.split('/'))
            
            bpRisk = getBpRiskrate(systolic_bp, 90)
            sugarRisk = getSugarRiskrate(sugar)
            risk = max(bpRisk, sugarRisk)

            # Create CheckupItem
            checkup = SpecialCheckupScheduletwo.objects.get(Special_Checkup_Id=checkup_id)
            # checkupItems=SpecialCheckupItem.objects.filter(Schedule_Id=checkup.Special_Checkup_Id)
                
            checkupItem = SpecialCheckupItem.objects.create(Schedule_Id=checkup,Blood_Pressure=bp_input,Sugar=sugar,Heartrate=hr)

            
            checkupItem.save()

            checkup.Risk_rate = risk
            checkup.Frequency=checkup.Frequency-1
            
            if checkup.Frequency==0:
                checkup.Completed=True

            checkup.save()
            # Retrieve the Member and Nurse instances
            member = Member.objects.get(Member_ID=checkup.Member_Id_id)

            member.riskrate = risk
            member.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'error': 'Invalid request'})
# fetches all the checkup data for all members and sorts them according to BloodPressure, Sugar and Heartrate as the user desires
class CheckupDataListView(View):
    template_name = 'nurses/checkup_data_list.html'  # Update with your actual template name

    def get_checkup_data(self, order_by):
        # Fetch all checkup data and join it with Member and CheckupItem
        checkup_data = CheckupSchedule.objects.select_related('Member_Id', 'Checkup_Id').all()

        # Sort the data based on the selected ordering
        if order_by == 'riskrate':
            checkup_data = sorted(checkup_data, key=lambda item: item.Checkup_Id.Risk_rate)
        elif order_by == 'blood_pressure':
            checkup_data = sorted(checkup_data, key=lambda item: item.Checkup_Id.Blood_Pressure)
        elif order_by == 'sugar':
            checkup_data = sorted(checkup_data, key=lambda item: item.Checkup_Id.Sugar)
        elif order_by == 'heartrate':
            checkup_data = sorted(checkup_data, key=lambda item: item.Checkup_Id.Heartrate)
        # print(checkup_data)
        return checkup_data

    def get(self, request, *args, **kwargs):
        # Get the sorting option from the query parameters (e.g., ?order_by=blood_pressure)
        order_by = request.GET.get('order_by', 'blood_pressure')  # Default to sorting by blood pressure

        # Get the sorted checkup data
        sorted_checkup_data = self.get_checkup_data(order_by)

        context = {
            'checkup_data': sorted_checkup_data,
            'order_by': order_by,
        }

        return render(request, self.template_name, context)

class ResidentConditionView(View):
    template_name = 'nurses/residentCondition.html'  # Update with your actual template name

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def retrieveData(self, request, nurse_id, *args, **kwargs):
        checkups = CheckupSchedule.objects.filter(Nurse_id=nurse_id, Completed=True)
        rows = []
        for checkup in checkups:
            checkup_item = CheckupItem.objects.filter(Checkup_id=checkup.Checkup_Id)
            data=[]
            if checkup_item.Blood_Pressure:
                data.append({'bp': checkup_item.Blood_pressure})
            if checkup_item.Sugar:
                data.append({'sugar': checkup_item.Sugar})
            if checkup_item.Heartrate:
                data.append({'sugar': checkup_item.Heartrate})

            data.append({'memid':checkup.Member_id})
            data.append({'checkupid':checkup.Checkup_id})
            data.append({'riskrate': checkup.Risk_rate})
            rows.append(data)
        sorted_rows = sorted(rows, key=lambda row: row['riskrate'])
        return sorted_rows

    # def reportDoctor(self, request, member_id,*args, **kwargs):
