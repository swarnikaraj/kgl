import datetime
import os
from datetime import datetime
from werkzeug.utils import redirect, secure_filename
from kgl import app, db

from flask import render_template, request, session, make_response
from kgl.models import Posts, Contact, Dossier, Admin, Employees, Diajewel, Gemidentification, Gemjewel, Labgrown

import pdfkit

path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

li = Admin.query.all()
adminuser = li[0].username
adminpass = li[0].password


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


# Diamond dossier start
@app.route("/dossierverifyinput", methods=['GET', 'POST'])
def dossierverifyinput_route():
    return render_template('dossierverifyinput.html')


@app.route("/dossierverifyresult", methods=['GET', 'POST'])
def dossierverifyresult_route():
    if request.method == 'POST':

        reportno = request.form.get('reportno')

        dossier = Dossier.query.filter_by(reportnumber=reportno).first()
        if dossier:
            name = dossier.name
            receiptno = dossier.receiptno
            contactno = dossier.contactno
            particulars = dossier.particulars
            quantity = dossier.quantity
            rate = dossier.rate
            total = dossier.total
            paid = dossier.paid
            balance = dossier.balance
            heading = dossier.heading
            logo = dossier.logo
            title = dossier.title
            subtitle = dossier.subtitle
            reportnumber = dossier.reportnumber
            shape = dossier.shape
            measurement = dossier.measurement
            carat = dossier.carat
            colourgrade = dossier.colourgrade
            claritygrade = dossier.claritygrade
            cutgrade = dossier.cutgrade
            polish = dossier.polish
            symmetry = dossier.symmetry
            fluorescence = dossier.fluorescence
            comment = dossier.comment
            img_file = dossier.img_file
            author = dossier.author
            dossier = Dossier(date=datetime.now().date(), name=name, receiptno=receiptno, contactno=contactno,
                              particulars=particulars,
                              quantity=quantity,
                              rate=rate, total=total, paid=paid, balance=balance, heading=heading, logo=logo,
                              title=title, subtitle=subtitle, reportnumber=reportnumber,
                              shape=shape, measurement=measurement, carat=carat, colourgrade=colourgrade,
                              claritygrade=claritygrade, cutgrade=cutgrade, polish=polish, symmetry=symmetry,
                              fluorescence=fluorescence, comment=comment, img_file=img_file, author=author
                              )

            return render_template('dossierverifyresult.html', heading=heading, logo=logo, title=title,
                                   subtitle=subtitle, reportnumber=reportnumber,
                                   shape=shape, measurement=measurement, carat=carat, colourgrade=colourgrade,
                                   claritygrade=claritygrade, cutgrade=cutgrade,
                                   polish=polish, symmetry=symmetry, fluorescence=fluorescence, comment=comment,
                                   img_file=img_file, author=author)
        return '<h1>Result Not Found</h1'





@app.route(
    '/<reportnumber>/<shape>/<measurement>/<carat>/<colourgrade>/<claritygrade>/<cutgrade>/<polish>/<symmetry'
    '>/<fluorescence>/<comment>')
def generate_dossier_pdf(reportnumber, shape, measurement, carat, colourgrade, claritygrade, cutgrade, polish, symmetry,
                         fluorescence, comment):
    rendered = render_template('dossierverifyresult.html', reportnumber=reportnumber, shape=shape,
                               measurement=measurement, carat=carat,
                               colourgrade=colourgrade, claritygrade=claritygrade, cutgrade=cutgrade, polish=polish,
                               symmetry=symmetry,
                               fluorescence=fluorescence, comment=comment
                               )
    pdf = pdfkit.from_string(rendered, False, configuration=config)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline:filename=certificate.pdf'
    return response

# diamond dossier end


# diamond jewellery start

@app.route("/verify_diamond_jwellery", methods=['GET', 'POST'])
def diamond_jwellery_verifyresult_route():
    if request.method == 'POST':
        reportnumber = request.form.get('reportno')

        diajewel = Diajewel.query.filter_by(reportnumber=reportnumber).first()
        if diajewel:
            name = diajewel.name
            receiptno = diajewel.receiptno
            contactno = diajewel.contactno
            particulars = diajewel.particulars
            quantity = diajewel.quantity
            rate = diajewel.rate
            total = diajewel.total
            paid = diajewel.paid
            balance = diajewel.balance
            heading = diajewel.heading
            logo = diajewel.logo
            title = diajewel.title
            subtitle = diajewel.subtitle
            reportnumber = diajewel.reportnumber
            description = diajewel.description
            weight = diajewel.weight
            shape = diajewel.shape
            colourgrade = diajewel.colourgrade
            claritygrade = diajewel.claritygrade
            finish = diajewel.finish
            comment = diajewel.comment
            img_file = diajewel.img_file
            author = diajewel.author
            diajewel = Diajewel(date=datetime.now().date(), name=name, receiptno=receiptno, contactno=contactno,
                                particulars=particulars,
                                quantity=quantity, rate=rate, total=total, paid=paid, balance=balance, heading=heading,
                                logo=logo,
                                title=title, subtitle=subtitle, reportnumber=reportnumber, description=description,
                                weight=weight,
                                shape=shape, colourgrade=colourgrade, claritygrade=claritygrade, finish=finish,
                                comment=comment,
                                img_file=img_file, author=author
                                )

            return render_template('diajewelleryverifyresult.html', heading=heading, logo=logo, title=title,
                                   subtitle=subtitle, reportnumber=reportnumber, description=description, weight=weight,
                                   shape=shape, colourgrade=colourgrade,
                                   claritygrade=claritygrade, finish=finish, comment=comment, img_file=img_file,
                                   author=author
                                   )
        return '<h1> Report Not Found</h1>'


@app.route("/diamond_jewellery_verify", methods=['GET', 'POST'])
def diajewellleryverifyinput_route():
    return render_template('diajewelleryverifyinput.html')


# End diamond jwellery


# start gem identification

@app.route("/gem_identification_verify", methods=['GET', 'POST'])
def gemidentificationverifyinput_route():
    return render_template('gemidentificationverifyinput.html')


@app.route("/identify_gem_report", methods=['GET', 'POST'])
def gemidentificationverifyresult_route():
    if request.method == 'POST':
        reportnumber = request.form.get('reportno')

        gemidentification = Gemidentification.query.filter_by(reportnumber=reportnumber).first()
        if gemidentification:
            name = gemidentification.name
            receiptno = gemidentification.receiptno
            contactno = gemidentification.contactno
            particulars = gemidentification.particulars
            quantity = gemidentification.quantity
            rate = gemidentification.rate
            total = gemidentification.total
            paid = gemidentification.paid
            balance = gemidentification.balance
            heading = gemidentification.heading
            logo = gemidentification.logo
            title = gemidentification.title
            subtitle = gemidentification.subtitle

            reportnumber = gemidentification.reportnumber
            shape = gemidentification.shape
            measurement = gemidentification.measurement
            weight = gemidentification.weight
            colour = gemidentification.colour
            specificgravity = gemidentification.specificgravity
            refractiveindex = gemidentification.refractiveindex
            hardness = gemidentification.hardness
            magnification = gemidentification.magnification
            result = gemidentification.result
            comment = gemidentification.comment
            img_file = gemidentification.img_file
            author = gemidentification.author
            gemidentification = Gemidentification(date=datetime.now().date(), name=name, receiptno=receiptno,
                                                  contactno=contactno,
                                                  particulars=particulars, quantity=quantity, rate=rate, total=total,
                                                  paid=paid, balance=balance, heading=heading, logo=logo,
                                                  title=title, subtitle=subtitle, reportnumber=reportnumber,
                                                  shape=shape, measurement=measurement, weight=weight, colour=colour,
                                                  specificgravity=specificgravity, refractiveindex=refractiveindex,
                                                  hardness=hardness, magnification=magnification, result=result,
                                                  comment=comment, img_file=img_file, author=author
                                                  )

            return render_template('gemidentificationverifyresult.html', heading=heading, logo=logo,
                                   title=title, subtitle=subtitle, reportnumber=reportnumber, shape=shape,
                                   measurement=measurement, weight=weight, colour=colour,
                                   specificgravity=specificgravity, refractiveindex=refractiveindex, hardness=hardness,
                                   magnification=magnification, result=result,
                                   comment=comment, img_file=img_file, author=author
                                   )
        return '<h1> Report Not Found</h1>'


# end gem identification


# gem jwellery start

@app.route("/verify_gem_jewellery", methods=['GET', 'POST'])
def gemjewelverifyresult_route():
    if request.method == 'POST':
        reportnumber = request.form.get('reportno')

        gemjewel = Gemjewel.query.filter_by(reportnumber=reportnumber).first()
        if gemjewel:
            name = gemjewel.name
            receiptno = gemjewel.receiptno
            contactno = gemjewel.contactno
            particulars = gemjewel.particulars
            quantity = gemjewel.quantity
            rate = gemjewel.rate
            total = gemjewel.total
            paid = gemjewel.paid
            balance = gemjewel.balance
            heading = gemjewel.heading
            logo = gemjewel.logo
            title = gemjewel.title
            subtitle = gemjewel.subtitle
            reportnumber = gemjewel.reportnumber
            shape = gemjewel.shape
            measurement = gemjewel.measurement
            weight = gemjewel.weight
            colour = gemjewel.colour
            specificgravity = gemjewel.specificgravity
            refractiveindex = gemjewel.refractiveindex
            hardness = gemjewel.hardness
            magnification = gemjewel.magnification
            result = gemjewel.result
            comment = gemjewel.comment
            img_file = gemjewel.img_file
            author = gemjewel.author
            gemjewel = Gemjewel(date=datetime.now().date(), name=name, receiptno=receiptno, contactno=contactno,
                                particulars=particulars, quantity=quantity, rate=rate, total=total, paid=paid,
                                balance=balance, heading=heading, logo=logo,
                                title=title, subtitle=subtitle, reportnumber=reportnumber, shape=shape,
                                measurement=measurement, weight=weight, colour=colour,
                                specificgravity=specificgravity, refractiveindex=refractiveindex, hardness=hardness,
                                magnification=magnification, result=result,
                                comment=comment, img_file=img_file, author=author
                                )

            return render_template('gemjewelverifyresult.html', heading=heading, logo=logo,
                                   title=title, subtitle=subtitle, reportnumber=reportnumber, shape=shape,
                                   measurement=measurement, weight=weight, colour=colour,
                                   specificgravity=specificgravity, refractiveindex=refractiveindex, hardness=hardness,
                                   magnification=magnification, result=result,
                                   comment=comment, img_file=img_file, author=author
                                   )
        return '<h1> Report Not Found</h1>'


@app.route("/gem_jewellery_verify", methods=['GET', 'POST'])
def gemjewelverifyinput_route():
    return render_template('gemjewelverifyinput.html')


# gem jwellery end


# lab grown start

@app.route("/verify_lab_grown", methods=['GET', 'POST'])
def labgrownverifyresult_route():
    if request.method == 'POST':
        reportnumber = request.form.get('reportno')

        labgrown = Labgrown.query.filter_by(reportnumber=reportnumber).first()
        if labgrown:
            name = labgrown.name
            receiptno = labgrown.receiptno
            contactno = labgrown.contactno
            particulars = labgrown.particulars
            quantity = labgrown.quantity
            rate = labgrown.rate
            total = labgrown.total
            paid = labgrown.paid
            balance = labgrown.balance
            heading = labgrown.heading
            logo = labgrown.logo
            title = labgrown.title
            subtitle = labgrown.subtitle
            reportnumber = labgrown.reportnumber
            shape = labgrown.shape
            measurement = labgrown.measurement
            weight = labgrown.weight
            colourgrade = labgrown.colourgrade
            claritygrade = labgrown.claritygrade
            cutgrade = labgrown.cutgrade
            polish = labgrown.polish
            symmetry = labgrown.symmetry
            fluorescence = labgrown.fluorescence
            comment = labgrown.comment
            img_file = labgrown.img_file
            author = labgrown.author
            labgrown = Labgrown(date=datetime.now().date(), name=name, receiptno=receiptno, contactno=contactno,
                                particulars=particulars, quantity=quantity, rate=rate, total=total, paid=paid,
                                balance=balance, heading=heading, logo=logo,
                                title=title, subtitle=subtitle, reportnumber=reportnumber, shape=shape,
                                measurement=measurement, weight=weight,
                                colourgrade=colourgrade, claritygrade=claritygrade, cutgrade=cutgrade, polish=polish,
                                symmetry=symmetry, fluorescence=fluorescence, comment=comment, img_file=img_file,
                                author=author
                                )

            return render_template('labgrownverifyresult.html', heading=heading, logo=logo,
                                   title=title, subtitle=subtitle, reportnumber=reportnumber, shape=shape,
                                   measurement=measurement, weight=weight,
                                   colourgrade=colourgrade, claritygrade=claritygrade, cutgrade=cutgrade, polish=polish,
                                   symmetry=symmetry, fluorescence=fluorescence, comment=comment, img_file=img_file,
                                   author=author
                                   )
        return '<h1> Report Not Found</h1>'


@app.route("/lab_grown_verify", methods=['GET', 'POST'])
def labgrownverifyinput_route():
    return render_template('labgrownverifyinput.html')


# lab grown end


@app.route('/login', methods=['GET', 'POST'])
def userlogin():
    if request.method == 'POST':
        uname = request.form.get('username')
        upass = request.form.get('password')
        user = Employees.query.filter_by(username=uname).first()
        if user:
            if user.password == upass:
                session['user'] = uname
                return render_template('userdashboard.html', username=uname)
        return "<h1>Username or the password is Incorrect</h1>"

    return render_template('employeelogin.html')


@app.route("/gemblog")
def blog_route():
    posts = Posts.query.filter_by().all()

    return render_template('gemblog.html', posts=posts)


@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()

    return render_template('blog-single.html', post=post)


@app.route("/blog-single")
def blog_single_route():
    return render_template('blog-single.html', )


@app.route("/createusers", methods=['GET', 'POST'])
def createusers_route():
    if "user" in session and session['user'] == adminuser:

        if request.method == 'POST':
            username = request.form.get("username")
            password = request.form.get("password")
            employee = Employees(username=username, password=password)
            db.session.add(employee)
            db.session.commit()
            return '<h1> User Created Successfully</h1>'

        return render_template("createuser.html")
    else:
        return render_template('login.html')



@app.route("/allreports")
def allreports():
    return render_template('reports.html')


@app.route('/diamondDossiersList')
def diamond_dossiers_list():
    dossier = Dossier.query.all()

    return render_template('diamond_dossiers_list.html', dossier=dossier)


@app.route('/allusers')
def user_list():
    employees = Employees.query.all()

    return render_template('allusers.html', employees=employees)


@app.route('/<name>/<contactno>/<date>/<receiptno>/<particulars>/<quantity>/<rate>/<total>/<paid>/<balance>')
def generate_pdf(name, contactno, date, receiptno, particulars, quantity, rate, total, paid, balance, ):
    rendered = render_template('receipt.html', name=name, contactno=contactno, date=date, receiptno=receiptno,
                               particulars=particulars, quantity=quantity, rate=rate, total=total, paid=paid,
                               balance=balance)
    pdf = pdfkit.from_string(rendered, False, configuration=config)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline:filename=receipt.pdf'
    return response




@app.route("/editdossier/<string:sno>", methods=['GET', 'POST'])
def editdossier(sno):
    if "user" in session and session['user'] == adminuser:
        if request.method == 'POST':

            name = request.form.get('name')
            receiptno = request.form.get('receiptno')
            contactno = request.form.get('contactno')
            particulars = request.form.get('particulars')
            quantity = request.form.get('quantity')
            rate = request.form.get('rate')
            total = request.form.get('total')
            paid = request.form.get('paid')
            balance = request.form.get('balance')
            heading = request.form.get('heading')
            logo = request.form.get('logo')
            title = request.form.get('title')
            subtitle = request.form.get('subtitle')
            reportnumber = request.form.get('reportnumber')
            shape = request.form.get('shape')
            measurement = request.form.get('measurement')
            carat = request.form.get('carat')
            colourgrade = request.form.get('colourgrade')
            claritygrade = request.form.get('claritygrade')
            cutgrade = request.form.get('cutgrade')
            polish = request.form.get('polish')
            symmetry = request.form.get('symmetry')
            fluorescence = request.form.get('fluorescence')
            comment = request.form.get('comment')
            img_file = request.form.get('img_file')
            author = request.form.get('author')

            if sno == '0':
                dossier = Dossier(date=datetime.now(), name=name, receiptno=receiptno, contactno=contactno,
                                  particulars=particulars,
                                  quantity=quantity,
                                  rate=rate, total=total, paid=paid, balance=balance, heading=heading, logo=logo,
                                  title=title, subtitle=subtitle, reportnumber=reportnumber,
                                  shape=shape, measurement=measurement, carat=carat, colourgrade=colourgrade,
                                  claritygrade=claritygrade, cutgrade=cutgrade, polish=polish, symmetry=symmetry,
                                  fluorescence=fluorescence, comment=comment, img_file=img_file, author=author
                                  )
                db.session.add(dossier)
                db.session.commit()

                return render_template('receipt.html', date=datetime.now(), name=name, receiptno=receiptno,
                                       contactno=contactno,
                                       particulars=particulars,
                                       quantity=quantity, rate=rate, total=total, paid=paid, balance=balance)
            else:
                dossier = Dossier.query.filter_by(sno=sno).first()

                dossier.name = name
                dossier.receiptno = receiptno
                dossier.contactno = contactno
                dossier.particulars = particulars
                dossier.quantity = quantity
                dossier.rate = rate
                dossier.total = total
                dossier.paid = paid
                dossier.balance = balance
                dossier.heading = heading
                dossier.logo = logo
                dossier.title = title
                dossier.subtitle = subtitle
                dossier.reportnumber = reportnumber
                dossier.shape = shape
                dossier.measurement = measurement
                dossier.carat = carat
                dossier.colourgrade = colourgrade
                dossier.claritygrade = claritygrade
                dossier.cutgrade = cutgrade
                dossier.polish = polish
                dossier.symmetry = symmetry
                dossier.fluorescence = fluorescence
                dossier.comment = comment
                dossier.img_file = img_file
                dossier.author = author

                db.session.commit()

                return redirect('/editdossier/' + sno)
        dossier = Dossier.query.filter_by(sno=sno).first()
        return render_template("editdossier.html", dossier=dossier, sno=sno)


@app.route("/Education")
def regulation_route():
    return render_template('Education.html')


@app.route("/termsConditions")
def termsconditions_route():
    return render_template('termsConditions.html')


@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard_route():
    if 'user' in session and session['user'] == adminuser:
        posts = Posts.query.all()
        return render_template('dashboard.html', posts=posts)

    if request.method == 'POST':
        username = request.form.get("uname")
        userpass = request.form.get("pass")
        if username == adminuser and userpass == adminpass:
            # set the session variable
            session['user'] = username
            posts = Posts.query.all()
            return render_template("dashboard.html", posts=posts)
        return '</h1> Invaid username or password </h1>'

    else:
        return render_template("login.html")


@app.route("/contactmsg", methods=['GET', 'POST'])
def contactmsg_route():
    if 'user' in session and session['user'] == "krystal":
        contact = Contact.query.all()
        return render_template('contactmsg.html', contact=contact)

    if request.method == 'POST':
        username = request.form.get("uname")
        userpass = request.form.get("pass")
        if username == "krystal" and userpass == "123456789":
            # set the session variable
            session['user'] = username
            contact = Contact.query.all()
            return render_template("contactmsg.html", contact=contact)

    else:
        return render_template('login.html')


@app.route("/editpost/<string:sno>", methods=['GET', 'POST'])
def edit_post(sno):
    if "user" in session and session['user'] == "krystal":
        if request.method == 'POST':
            title = request.form.get('title')
            slug = request.form.get('slug')
            subtitle = request.form.get('subtitle')
            img_file = request.form.get('img_file')
            para1 = request.form.get('para1')
            para2 = request.form.get('para2')
            para3 = request.form.get('para3')

            if sno == '0':
                post = Posts(title=title, slug=slug, subtitle=subtitle, img_file=img_file, para1=para1, para2=para2,
                             para3=para3)
                db.session.add(post)
                db.session.commit()
            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.title = title
                post.slug = slug
                post.subtitle = subtitle
                post.img_file = img_file
                post.para1 = para1
                post.para2 = para2
                post.para3 = para3
                db.session.commit()

                return redirect('/editpost/' + sno)
        post = Posts.query.filter_by(sno=sno).first()

        return render_template("editpost.html", post=post, sno=sno)


@app.route("/about")
def about_route():
    return render_template('about.html')


@app.route("/register")
def register_route():
    return render_template('register.html')


# sno,name,email,phone,company,subject,msg

@app.route("/contact", methods=['GET', 'POST'])
def contact_route():
    if request.method == 'POST':
        # add entry
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        company = request.form.get('company')
        subject = request.form.get('subject')
        msg = request.form.get('msg')

        entry = Contact(name=name, email=email, phone=phone, company=company, subject=subject, msg=msg)
        db.session.add(entry)
        db.session.commit()
        return '<h1> Querry Submitted Successfully</h1>'

    return render_template('contact.html')


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/dashboard')


@app.route('/userlogout')
def logout_user():
    session.pop('user')
    return redirect('/login')


@app.route("/deletepost/<string:sno>", methods=['GET', 'POST'])
def delete_post(sno):
    if "user" in session and session['user'] == "krystal":
        post = Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect("/dashboard")


@app.route("/deletedossier/<string:sno>", methods=['GET', 'POST'])
def delete_dossier(sno):
    if "user" in session and session['user'] == "krystal":
        dossier = Dossier.query.filter_by(sno=sno).first()
        db.session.delete(dossier)
        db.session.commit()
    return redirect("/diamondDossiersList")


@app.route("/deleteemployees/<string:id>", methods=['GET', 'POST'])
def delete_employees(id):
    if "user" in session and session['user'] == "krystal":
        employee = Employees.query.filter_by(id=id).first()
        db.session.delete(employee)
        db.session.commit()
    return redirect("/allusers")


@app.route("/uploader", methods=['GET', 'POST'])
def uploader():
    if "user" in session and session['user'] == 'krystal':
        if request.method == 'POST':
            f = request.files['file1']
            f.save(os.path.join('E:/KGLabs/KGLabs/KGL/static/assets/img', secure_filename(f.filename)))
            return "Uploaded successfully!"
