from flask import Flask, render_template, request
from backend_consumer import PrClient


app = Flask(__name__)
pr_client  = PrClient()


@app.route('/')
def start():

    return render_template('index.html')

@app.route('/get-similarity', methods=[ 'POST', 'GET'])
def get_similarity():

    route1 = request.values.get('route1')
    route2 = request.values.get('route2')

    similarity_score = pr_client.process_get(f'similarity?route1={route1}&route2={route2}')



    return render_template('index.html', similarity_score=similarity_score.json())


if __name__== "__main__":
    app.run(host='0.0.0.0', debug = True, port = 5004)

