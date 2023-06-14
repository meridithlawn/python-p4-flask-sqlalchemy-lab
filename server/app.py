#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal
# from flask import (
#     Flask,
#     request,
#     g,
#     sessiion,
#     json,
#     jsonify,
#     render_template,
#     make_response,
#     url_for,
#     redirect
# )

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.get(Animal.id == id)
    # animal = Animal.query.filter(Animal.id == id).first_or_404
    # animal = Animal.query.filter(Animal.id == id).one_or_none
    # use filter_by if you want all
    # animal = Animal.query.filter_by(id == id).first_or_404()
    # if animal:= db.session.get(Animal, id): most up-to-date version
    if animal:
        response_body = f"""
            <ul> ID: {animal.id} </ul>
            <ul> Name: {animal.name} </ul>
            <ul> Species: {animal.species} </ul>
            <ul> Zookeeper: {animal.zookeeper.name} </ul>
            <ul> Enclosure: {animal.enclosure.environment} </ul>
        """
        return make_response(response_body, 200)
    else:
        response_body = f"""
            <ul> No animal with ID {id}</ul>
        """
        return make_response(response_body, 404)


@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    if zk:= db.session.get(Zookeeper, id):
        response_body = f"""
            <ul> ID: {zk.id}</ul>
            <ul> Name: {zk.name}</ul>
            <ul> Birthday: {zk.birthday}</ul>
        """
        animal_names = [animal.name for animal in zk.animals]
        for name in animal_names:
            response_body += f"<ul>Animal: {name}</ul>"
        return make_response(response_body, 200)
    else:
        response_body = f"""
            <ul> 404 Not Found any zookeepers with id {id}</ul>
        """
        return make_response(response_body, 404)
    
@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    if enclosure:= db.session.get(Enclosure, id):
        response_body = f"""
        <ul> ID: {enclosure.id},/ul>
        <ul> Environment: {enclosure.environment}</ul>
        """
        enclosure_list = [enclosure.environment for enclosure in enclosure_list]
        for enclosure in enclosure_list:
            response_body += f"<ul>Environment: {enclosure}</ul>"
        return make_response(response_body, 200)
    else:
        response_body - f"""
            <ul> 404 Not Found any environments with id {id},/ul>
        """
        return make_response(response_body, 404)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
