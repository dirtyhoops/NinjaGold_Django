from django.shortcuts import render, redirect
import random, datetime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'goldlog' not in request.session:
        request.session['goldlog'] = []
    goldsession = {
        "gold": request.session['gold'],
        "goldlog": request.session['goldlog']
    }
    return render(request, 'first_app/index.html', goldsession)

def process_money(request):
    if request.method == 'POST':
        pcolor = "gold"
        now = datetime.datetime.now()
        place = request.POST.get("building")
        
        if place == "farm":
            goldamount = random.randrange(10, 21)
            request.session['gold'] += goldamount
            request.session['goldlog'].append(" Earned " + str(goldamount) + " golds from the " + place + "! (" + now.strftime("%Y-%m-%d %H:%M") + ")")
        elif place == "cave":
            goldamount = random.randrange(5, 11)
            request.session['gold'] += goldamount
            request.session['goldlog'].append(" Earned " + str(goldamount) + " golds from the " + place + "! (" + now.strftime("%Y-%m-%d %H:%M") + ")")
        elif place == "house":
            goldamount = random.randrange(2, 6)
            request.session['gold'] += goldamount
            request.session['goldlog'].append(" Earned " + str(goldamount) + " golds from the " + place + "! (" + now.strftime("%Y-%m-%d %H:%M") + ")")
        elif place == "casino":
            goldamount = random.randrange(-50, 51)
            request.session['gold'] += goldamount
            if goldamount > 0:
                request.session['goldlog'].append(" Earned " + str(goldamount) + " golds from the " + place + "! (" + now.strftime("%Y-%m-%d %H:%M") + ")")
            else: 
                request.session['goldlog'].append(" Entered a casino and lost " + str(goldamount) + " golds... Ouch...! (" + now.strftime("%Y-%m-%d %H:%M") + ")")

        return redirect('/')

def clear(request):
    if request.method == 'POST':
        request.session['gold'] = 0
        request.session['goldlog'] = []

        return redirect('/')