from flask import Flask, request
from similarity import check_similarity

app = Flask(__name__)


@app.route('/ping')
def ping():

    result = {
        "ping"  : "pong"
    }
    return result



@app.route('/similarity', methods=['GET', 'POST'])
def similarity():

    print ("here")

    route1 = request.values.get('route1')
    route2 = request.values.get('route2')

    similarity_score = int(check_similarity(route1, route2)*100)
  

    similarity_score = {
        "similarity_score" : similarity_score
    }

    return similarity_score

    


if __name__== "__main__":
    app.run(host="0.0.0.0", debug = True, port = 5003)