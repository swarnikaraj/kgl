from kgl.models import  Diajewel

diajewel = Diajewel.query.filter_by(reportnumber="454567").first()

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
    print(name)









