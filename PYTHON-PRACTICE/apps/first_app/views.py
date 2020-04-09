from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
# the index function is called when root is visited
def index(request):
    context= {
        "first_name" : request.session['first_name'],
        "last_name" : request.session['last_name']
    }
    return render(request, "first_app/index.html", context)

def create(request):
    print '*'*50
    print 'button was pressed'
    request.session['first_name'] = request.POST["first_name"]
    request.session['last_name'] = request.POST["last_name"]
    return redirect('/')

def survey(request):
    context = {
        "first_name" : request.session['first_name'],
        "last_name" : request.session['last_name'],
    }
    return render(request, "first_app/survey.html", context)

def survey_form(request):
    request.session['genre'] = request.POST['genre']
    request.session['language'] = request.POST['language']
    context = {
        "genre" : request.session['genre'].title(),
        "language" : request.session['language'].title(),
        "first_name" : request.session['first_name'],
        "last_name" : request.session['last_name']
    }
    return render(request, "first_app/survey_results.html", context)

def survey_results(request):
    context = {
        "genre" : request.session['genre'],
        "language" : request.session['language'],
        "first_name" : request.session['first_name'],
        "last_name" : request.session['last_name']
    }
    return render(request, "first_app/survey_results.html", context)

def random(request):
    request.session['counter'] = request.session['counter']
    request.session['random_word'] = request.session['random_word']
    context= {
        "first_name" : request.session['first_name'],
        "last_name" : request.session['last_name'],
        "count" : request.session['counter'],
        "random_word" : request.session['random_word']
    }
    return render(request, "first_app/random.html", context)

def generate(request):
    request.session['counter'] = request.session['counter'] + 1
    request.session['random_word'] = get_random_string(length=7)
    print request.session['counter']
    print request.session['random_word']
    return redirect("/random")

def clear(request):
    request.session['counter'] = 0
    request.session['random_word'] = ""
    return redirect("/random")

def session_words(request):
    context = {
        "first_name" : request.session['first_name'],
        "last_name" : request.session['last_name']
    }
    return render(request, "first_app/session_words.html", context)

def add_word(request):
    if request.method == "POST":
        # time = strftime("%H:%M%p, %Y-%m-%d", gmtime())
        text =  request.POST['new_word']
        color = request.POST['color']
        # if checkbox in not check the we  pass a default value using get
        font = request.POST.get('font', 'small')
        request.session['info'] = {'new_word':text, 'color':color, 'font':font}

        if 'history' not in request.session:
            request.session["history"] = []
        request.session["history"] += [request.session['info']]
        print request.session["history"]
    return redirect("/session_words")

def clear_words(request):
    request.session["history"] = []
    return redirect("/session_words")

# AMADON!!!
def amadon_homepage(request):
    context = {
    "first_name" : request.session['first_name'],
    "last_name" : request.session['last_name']
    }
    return render(request, "first_app/amadon.html", context)

def buy(request):
    request.session['grand_total'] = request.session['grand_total']
    if request.POST['product_id'] == '1':
        request.session['product_price'] = 4.99
        request.session['quantity'] = float(request.POST['quantity'])
        request.session['total'] = request.session['product_price']*request.session['quantity']
        request.session['grand_total'] = request.session['grand_total'] + request.session['total']
        request.session['name'] = 'Apple'
    elif request.POST['product_id'] == '2':
        request.session['product_price'] = 2.99
        request.session['quantity'] = float(request.POST['quantity'])
        request.session['total'] = request.session['product_price']*request.session['quantity']
        request.session['grand_total'] = request.session['grand_total'] + request.session['total']
        request.session['name'] = 'Banana'
    elif request.POST['product_id'] == '3':
        request.session['product_price'] = 3.99
        request.session['quantity'] = float(request.POST['quantity'])
        request.session['total'] = request.session['product_price']*request.session['quantity']
        request.session['grand_total'] = request.session['grand_total'] + request.session['total']
        request.session['name'] = 'Orange'
    print request.session['product_price']
    return redirect('/amadon_cart')

def amadon_cart(request):
    price = request.session['product_price']
    quantity = request.session['quantity']
    total = request.session['total']
    print request.session['grand_total']
    print total
    context = {
    "name" : request.session['name'],
    "first_name" : request.session['first_name'],
    "last_name" : request.session['last_name'],
    "grand_total": request.session['grand_total'],
    "price": price,
    "quantity": int(quantity),
    "total": total
    }
    return render(request, "first_app/amadon_cart.html", context)

def logout(request):
    request.session['first_name'] = ""
    request.session['last_name'] = ""
    request.session['counter'] = 0
    request.session['random_word'] = ""
    request.session['grand_total'] = 0.0
    print "User has been logged out"
    return redirect('/')
