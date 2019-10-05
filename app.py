#! flask/bin/python
from flask import Flask, jsonify, abort

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


@app.route('/todo/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

if __name__ == '__main__':
    app.run(debug=True)
