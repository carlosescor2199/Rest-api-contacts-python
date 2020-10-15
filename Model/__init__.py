from Database import db, ma


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(40))
    lastname = db.Column(db.String(40))
    phoneNumber = db.Column(db.String(15))
    email = db.Column(db.String(50))

    def __init__(self, firstname, lastname, phoneNumber, email):
        self.firstname = firstname
        self.lastname = lastname
        self.phoneNumber = phoneNumber
        self.email = email


db.create_all()


class ContactSchema(ma.Schema):
    class Meta:
        fields = ('id', 'firstname', 'lastname', 'phoneNumber', 'email')


contact_schema = ContactSchema()
contacts_schema = ContactSchema(many=True)