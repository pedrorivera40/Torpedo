from app import app
from flask import Flask, redirect, url_for, session, jsonify, request

@app.route("/", methods=['GET'])
def TorpedoHello():
    return jsonify("Buenas"),200