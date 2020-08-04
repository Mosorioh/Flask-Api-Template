 
from flask import Flask, request
from flask import render_template
from flask import jsonify

import requests

import json
import os

# GUID
import uuid 

# Cors
from flask_cors import CORS

app=Flask(__name__,template_folder='templates')
cors = CORS(app)

@app.route('/')
def home():
    
    with open('./appSettings.json') as json_file:
        data = json.load(json_file)
    ServerPubsher = data['ServerPubsher']
    ServerSubcriber = data['ServerSubcriber']
    Endpoint = data['Endpoint']
    IpServer = data['IpServer']


    return render_template("index.html",IpServer=IpServer, ServerPubsher=ServerPubsher, ServerSubcriber=ServerSubcriber, Endpoint=Endpoint)

@app.route('/Settings')
def GetInfo():
    #print (EndpointId)
    with open('./appSettings.json') as json_file:
        data = json.load(json_file)
    print (data)
    return jsonify(data)

@app.route('/Settings', methods=["POST"])
def UpdateInfo():
    #print (EndpointId)
    ServerPubsher = request.form['ServerPubsher']
    ServerSubcriber = request.form['ServerSubcriber']
    Endpoint = request.form['Endpoint']
    IpServer = request.form['IpServer']

    data = {}
    data['ServerPubsher'] = ServerPubsher
    data['ServerSubcriber'] = ServerSubcriber
    data['Endpoint'] = Endpoint
    data['IpServer'] = IpServer
    

    with open('./appSettings.json', 'w') as file:
        json.dump(data, file)
    return jsonify(data)

if __name__ == '__main__':
    #app.run(host='192.168.100.233', port=5080, debug=True)
    app.run(host='192.168.100.6', port=5080, debug=True)

