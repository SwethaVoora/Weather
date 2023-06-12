from flask import render_template, Blueprint, request, redirect, url_for, flash
import requests
from .models import City
from . import db

views = Blueprint('views', __name__)



def get_weather_data(city):
    api_key = '5de1e3333b17b52781ee7cd55e08d196'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ city }&units=imperial&appid=' + api_key
    r = requests.get(url).json()
    # print(city,r)
    return r



@views.route('/')
def index_get():
    cities = City.query.all()

    # api_key = '5de1e3333b17b52781ee7cd55e08d196'
    # below is the API endpoint.
    # q stands for query
    # {} gets city value and units=imperial gives us the temp in fahrenheit
    # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=' + api_key
    # city = 'Las Vegas'
    weather_data = []

    for city in cities:

      # r = requests.get(url.format(city.name)).json()
      r = get_weather_data(city.name)
    #   print(city.name, r)

      weather = {
          'city': city.name ,
          'temperature': r['main']['temp'],
          'description': r['weather'][0]['description'],
          'icon': r['weather'][0]['icon']
      }

      weather_data.append(weather)
    #   print(weather)

    # return render_template('weather.html', weather=weather)
    return render_template('weather.html', weather_data=weather_data)

@views.route('/', methods = ['POST'])
def index_post():
    err_msg=''
    new_city = request.form.get('city')
    print(new_city)

    if new_city != '':
        existing_city = City.query.filter_by(name=new_city).first()

        if not existing_city:
            new_city_data = get_weather_data(new_city)
            if new_city_data['cod'] == 200:
                new_city_obj = City(name=new_city)
                db.session.add(new_city_obj)
                db.session.commit()
            else:
                err_msg = 'Invalid City'
                print(err_msg)
        else:
            # flash('The weather details of this city are already displayed.', category = 'error')
            err_msg = 'City already exists'
            print(err_msg)
    else:
        err_msg = 'Invalid City'
        print(err_msg)
        
    if err_msg:
        flash(err_msg, category='error')
    else:
        flash('City added successfully', category='success')
    
    return redirect(url_for('views.index_get'))

@views.route('/delete/<name>')
def delete_city(name):
    city = City.query.filter_by(name=name).first()
    db.session.delete(city)
    db.session.commit()
    flash(f'{city.name} has been deleted', category='success')
    return redirect(url_for('views.index_get'))
