from django.shortcuts import render
from .models import  Member

def index(request):
    members = Member.objects.all().order_by('pk')


    return render(
        request,
        'member/index.html',
        {
            'members': members,
        }
    )
def single_member_page(request, pk):
    member = Member.objects.get(pk=pk)

    return render(
        request,
        'member/single_member_page.html',
        {
            'member' : member,
        }
    )