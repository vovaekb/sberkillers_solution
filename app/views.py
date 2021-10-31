from flask import Flask, request, jsonify, Response
from . import app

@app.route('/', methods=['GET'])
def index():
    return Response('Hello', status=200)

'''
@app.route('/action_tickets', methods=['GET'])
def action_tickets():
    action_tickets = app.session.query(ActionTicket).all()
    print(len(action_tickets))
    return jsonify({'action_tickets ': [ticket.serialized for ticket in action_tickets]}), 200 


@app.route('/create_information_tickets', methods=['GET', 'POST'])
def create_information_tickets():
    pass
'''
