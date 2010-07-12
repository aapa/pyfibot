# -*- coding: utf-8 -*-


has_pywapi = False
try:
    import pywapi
    has_pywapi = True
except:
    print('Error loading library pywapi. Probably you havent installed it yet.')

def celcius_to_fahrenheit(f): return (int(f)-32)/1.8

def command_forecast(bot, user, channel, args):
    '''this module tells weather forecast for location'''
    if not has_pywapi: return

    result_dict = pywapi.get_weather_from_google(args)
    if not all(result_dict.values()):
        bot.say(channel, 'unknown location')
        return

    answerstr = u'%s: ' % (result_dict['forecast_information']['city'])
    for day in result_dict['forecasts']:
        answerstr = answerstr + (u'%s: %s (%.0f°C/%.0f°C), ' % (day['day_of_week'], \
                          day['condition'], \
                          celcius_to_fahrenheit(day['low']), \
                          celcius_to_fahrenheit(day['high'])))

    bot.say(channel, answerstr.encode('utf-8'))