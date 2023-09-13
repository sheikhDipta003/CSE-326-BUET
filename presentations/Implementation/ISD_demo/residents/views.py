from django.shortcuts import render, redirect
from django.views import View
from nurses.models import Member, ResidentMedCond
from .models import MedCond

class DashboardView(View):
    template_name = 'residents/dashboard.html'

    def get(self, request, member_id, *args, **kwargs):
        try:
            # Fetch the resident's information
            member = Member.objects.get(Member_ID=member_id)

            # Fetch the resident's medical condition information
            resident_condition = ResidentMedCond.objects.get(Member_ID=member)

            # Fetch the condition details
            condition = MedCond.objects.get(Cond_ID=resident_condition.Cond_ID.Cond_ID)

            context = {
                'member': member,
                'condition': condition,
            }

            return render(request, self.template_name, context)
        except Member.DoesNotExist:
            # Handle the case where the member does not exist
            return render(request, self.template_name, {'error_message': 'Member not found'})
        except ResidentMedCond.DoesNotExist:
            # Handle the case where the resident's medical condition does not exist
            return render(request, self.template_name, {'error_message': 'Medical condition not found'})
