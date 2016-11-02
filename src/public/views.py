"""
Logic for dashboard related routes
"""
from flask import Blueprint, render_template,url_for,request,redirect
from .forms import LogUserForm, PapirForm
from ..data.database import db
from ..data.models import LogUser, PapirDB
blueprint = Blueprint('public', __name__)

@blueprint.route('/', methods=['GET'])
def index():
    return render_template('public/index.tmpl')

@blueprint.route('/loguserinput',methods=['GET', 'POST'])
def InsertLogUser():
    form = LogUserForm()
    if form.validate_on_submit():
        LogUser.create(**form.data)
    return render_template("public/LogUser.tmpl", form=form)

@blueprint.route('/loguserlist',methods=['GET'])
def ListuserLog():
    pole = db.session.query(LogUser).all()
    return render_template("public/listuser.tmpl",data = pole)

@blueprint.route('/papir', methods=['GET', 'POST'])
def papiry():
    form = PapirForm()
    if form.validate_on_submit():
        PapirDB.create(**form.data)
    return render_template("public/papir.tmpl", form=form)

@blueprint.route('/vypis_papir', methods=['GET'])
def vypis_papiry():
    pole = db.session.query(PapirDB).all()
    return render_template("public/vypispapir.tmpl", data=pole)

@blueprint.route('/smazat_papir/<int:id>', methods=['GET'])
def smazat_papiry(id):
    pole = db.session.query(PapirDB).filter_by(id = id).first()
    db.session.delete(pole)
    db.session.commit()
    return redirect(request.args.get("next")or url_for("public.vypis_papiry"))