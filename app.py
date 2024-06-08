from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_price(code):
    데이터 = requests.get(f'https://finance.naver.com/item/sise.nhn?code={code}')
    soup = BeautifulSoup(데이터.content, 'html.parser')
    현재가 = soup.find('strong', id="_nowVal").text
    변동률 = soup.find_all('span', class_="tah")[5].text
    #주가명 = soup.find_all('a','window.location.reload()').text
    return 현재가, 변동률

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_price', methods=['POST'])
def get_price_route():
    code = request.form['code']
    현재가, 변동률 = get_price(code)
    return render_template('index.html', 현재가=현재가, 변동률=변동률)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
