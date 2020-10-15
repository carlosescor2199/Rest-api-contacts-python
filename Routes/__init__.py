from API import app
from flask import request

from Database import db
from Model import Contact, contact_schema, contacts_schema


@app.route('/contacts', methods=["POST"])
def create_contact():
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    phoneNumber = float(request.json['phoneNumber'])
    email = request.json['email']

    new_contact = Contact(firstname, lastname, phoneNumber, email)
    db.session.add(new_contact)
    db.session.commit()

    return  contact_schema.jsonify(new_contact)

@app.route('/contacts', methods=["GET"])
def get_contacts():
    all_products = Contact.query.all()
    result = contacts_schema.dump(all_products)

    return contacts_schema.jsonify(result)

@app.route('/contacts/<id>', methods=["GET"])
def get_product(id):
    contact = Contact.query.get(id)
    return contact_schema.jsonify(contact)

@app.route('/contacts/<id>', methods=["PUT"])
def update_product(id):
    contact = Contact.query.get(id)

    firstname = request.json['firstname']
    lastname = request.json['lastname']
    phoneNumber = float(request.json['phoneNumber'])
    email = request.json['email']

    contact.firstname = firstname
    contact.lastname = lastname
    contact.phoneNumber = phoneNumber
    contact.email = email

    db.session.commit()
    return contact_schema.jsonify(contact)

@app.route('/contacts/<id>', methods=["DELETE"])
def delete_product(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    return contact_schema.jsonify(contact)