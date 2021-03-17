from django.shortcuts import render
from models_exercise.models import User


# Create your views here.
def index(request):
    return render(request, 'models_exercise/index.html')


def users(request):
    users_list = User.objects.order_by('last_name')
    user_dictionary ={'user_records': users_list}
    return render(request, 'models_exercise/users.html', context=user_dictionary)
