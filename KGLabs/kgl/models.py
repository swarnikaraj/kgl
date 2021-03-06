from datetime import datetime

from kgl import db


class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    company = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(120), nullable=False)
    msg = db.Column(db.String(120), nullable=False)


class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(80), nullable=False)
    subtitle = db.Column(db.String(21), nullable=False)
    img_file = db.Column(db.String(150), nullable=True)
    para1 = db.Column(db.String(12), nullable=True)
    para2 = db.Column(db.String(12), nullable=True)
    para3 = db.Column(db.String(12), nullable=True)


class Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=80), nullable=False, unique=True)
    password = db.Column(db.String(length=80), nullable=False)


class Admin(db.Model):
    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(60), nullable=False)


class Dossier(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    name = db.Column(db.String(150), nullable=True)
    receiptno = db.Column(db.String(150), nullable=True, unique=True)
    contactno = db.Column(db.String(150), nullable=True)
    particulars = db.Column(db.String(150), nullable=True)
    quantity = db.Column(db.String(150), nullable=True)
    rate = db.Column(db.String(150), nullable=True)
    total = db.Column(db.String(150), nullable=True)
    paid = db.Column(db.String(150), nullable=True)
    balance = db.Column(db.String(150), nullable=True)
    heading = db.Column(db.String(150), nullable=True)
    logo = db.Column(db.String(150), nullable=True)
    title = db.Column(db.String(150), nullable=True)
    subtitle = db.Column(db.String(150), nullable=True)
    reportnumber = db.Column(db.String(150), nullable=True, unique=True)
    shape = db.Column(db.String(150), nullable=True)
    measurement = db.Column(db.String(150), nullable=True)
    carat = db.Column(db.String(150), nullable=True)
    colourgrade = db.Column(db.String(150), nullable=True)
    claritygrade = db.Column(db.String(150), nullable=True)
    cutgrade = db.Column(db.String(150), nullable=True)
    polish = db.Column(db.String(150), nullable=True)
    symmetry = db.Column(db.String(150), nullable=True)
    fluorescence = db.Column(db.String(150), nullable=True)
    comment = db.Column(db.String(1024), nullable=True)
    img_file = db.Column(db.String(150), nullable=True)
    author = db.Column(db.Integer(), db.ForeignKey('employees.id'))


class Diajewel(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.now().date(), nullable=False)
    name = db.Column(db.String(150), nullable=True)
    receiptno = db.Column(db.String(150), nullable=True, unique=True)
    contactno = db.Column(db.String(150), nullable=True)
    particulars = db.Column(db.String(150), nullable=True)
    quantity = db.Column(db.String(150), nullable=True)
    rate = db.Column(db.String(150), nullable=True)
    total = db.Column(db.String(150), nullable=True)
    paid = db.Column(db.String(150), nullable=True)
    balance = db.Column(db.String(150), nullable=True)
    heading = db.Column(db.String(150), nullable=True)
    logo = db.Column(db.String(150), nullable=True)
    title = db.Column(db.String(150), nullable=True)
    subtitle = db.Column(db.String(150), nullable=True)
    reportnumber = db.Column(db.String(150), nullable=True, unique=True)
    description = db.Column(db.String(150), nullable=True)
    weight = db.Column(db.String(150), nullable=True)
    shape = db.Column(db.String(150), nullable=True)
    colourgrade = db.Column(db.String(150), nullable=True)
    claritygrade = db.Column(db.String(150), nullable=True)
    finish = db.Column(db.String(150), nullable=True)
    comment = db.Column(db.String(1024), nullable=True)
    img_file = db.Column(db.String(150), nullable=True)
    author = db.Column(db.Integer(), db.ForeignKey('employees.id'))


class Gemidentification(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    name=db.Column(db.String(150), nullable=True)
    receiptno = db.Column(db.String(150), nullable=True, unique=True)
    contactno = db.Column(db.String(150), nullable=True)
    particulars = db.Column(db.String(150), nullable=True)
    quantity = db.Column(db.String(150), nullable=True)
    rate = db.Column(db.String(150), nullable=True)
    total = db.Column(db.String(150), nullable=True)
    paid = db.Column(db.String(150), nullable=True)
    balance = db.Column(db.String(150), nullable=True)
    heading = db.Column(db.String(150), nullable=True)
    logo = db.Column(db.String(150), nullable=True)
    title = db.Column(db.String(150), nullable=True)
    subtitle = db.Column(db.String(150), nullable=True)
    reportnumber = db.Column(db.String(150), nullable=True, unique=True)
    shape = db.Column(db.String(150), nullable=True)
    measurement = db.Column(db.String(150), nullable=True)
    weight = db.Column(db.String(150), nullable=True)
    colour = db.Column(db.String(150), nullable=True)
    specificgravity = db.Column(db.String(150), nullable=True)
    refractiveindex = db.Column(db.String(150), nullable=True)
    hardness = db.Column(db.String(150), nullable=True)
    magnification = db.Column(db.String(150), nullable=True)
    result = db.Column(db.String(150), nullable=True)
    comment = db.Column(db.String(1024), nullable=True)
    img_file = db.Column(db.String(150), nullable=True)
    author = db.Column(db.Integer(), db.ForeignKey('employees.id'))


class Labgrown(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    name=db.Column(db.String(150), nullable=True)
    receiptno = db.Column(db.String(150), nullable=True, unique=True)
    contactno = db.Column(db.String(150), nullable=True)
    particulars = db.Column(db.String(150), nullable=True)
    quantity = db.Column(db.String(150), nullable=True)
    rate = db.Column(db.String(150), nullable=True)
    total = db.Column(db.String(150), nullable=True)
    paid = db.Column(db.String(150), nullable=True)
    balance = db.Column(db.String(150), nullable=True)
    heading = db.Column(db.String(150), nullable=True)
    logo = db.Column(db.String(150), nullable=True)
    title = db.Column(db.String(150), nullable=True)
    subtitle = db.Column(db.String(150), nullable=True)
    reportnumber = db.Column(db.String(150), nullable=True, unique=True)
    shape = db.Column(db.String(150), nullable=True)
    measurement = db.Column(db.String(150), nullable=True)
    weight = db.Column(db.String(150), nullable=True)
    colourgrade = db.Column(db.String(150), nullable=True)
    claritygrade = db.Column(db.String(150), nullable=True)
    cutgrade = db.Column(db.String(150), nullable=True)
    polish = db.Column(db.String(150), nullable=True)
    symmetry = db.Column(db.String(150), nullable=True)
    fluorescence = db.Column(db.String(150), nullable=True)
    comment = db.Column(db.String(1024), nullable=True)
    img_file = db.Column(db.String(150), nullable=True)
    author = db.Column(db.Integer(), db.ForeignKey('employees.id'))


class Gemjewel(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    name = db.Column(db.String(150), nullable=True)
    receiptno = db.Column(db.String(150), nullable=True, unique=True)
    contactno = db.Column(db.String(150), nullable=True)
    particulars = db.Column(db.String(150), nullable=True)
    quantity = db.Column(db.String(150), nullable=True)
    rate = db.Column(db.String(150), nullable=True)
    total = db.Column(db.String(150), nullable=True)
    paid = db.Column(db.String(150), nullable=True)
    balance = db.Column(db.String(150), nullable=True)
    heading = db.Column(db.String(150), nullable=True)
    logo = db.Column(db.String(150), nullable=True)
    title = db.Column(db.String(150), nullable=True)
    subtitle = db.Column(db.String(150), nullable=True)
    reportnumber = db.Column(db.String(150), nullable=True, unique=True)
    shape = db.Column(db.String(150), nullable=True)
    measurement = db.Column(db.String(150), nullable=True)
    weight = db.Column(db.String(150), nullable=True)
    colour = db.Column(db.String(150), nullable=True)
    specificgravity = db.Column(db.String(150), nullable=True)
    refractiveindex = db.Column(db.String(150), nullable=True)
    hardness = db.Column(db.String(150), nullable=True)
    magnification = db.Column(db.String(150), nullable=True)
    result = db.Column(db.String(150), nullable=True)
    comment = db.Column(db.String(1024), nullable=True)
    img_file = db.Column(db.String(150), nullable=True)
    author = db.Column(db.Integer(), db.ForeignKey('employees.id'))
