from flask import Flask, request, jsonify, render_template
from requests_html import HTMLSession

app = Flask(__name__)

def get_weather(city):
    session = HTMLSession()
    url = f'https://www.google.com/search?q=weather+{city}'
    response = session.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'})
    
    if response.status_code != 200:
        return {'error': 'Weather information could not be retrieved.'}
    
    temp = response.html.find('span#wob_tm', first=True)
    unit = response.html.find('div.vk_bk.wob-unit span.wob_t', first=True)
    desc = response.html.find('div.VQF4g span#wob_dc', first=True)
    
    if temp and unit and desc:
        return {'city': city, 'temperature': temp.text, 'unit': unit.text, 'description': desc.text}
    else:
        return {'error': 'Weather information could not be retrieved.'}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather')
def weather():
    city = request.args.get('city')
    return jsonify(get_weather(city))

if __name__ == '__main__':
    app.run(debug=True)
