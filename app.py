#! flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Faire les courses',
        'description': u'Acheter Lait, Fromage, Pizza, Fruit'
    },
    {
        'id': 2,
        'title': u'Apprendre Python',
        'description': u'Pour creer une API REST avec Flask'
    }
]

@app.route('/todo/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)
