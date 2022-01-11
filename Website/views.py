from flask import Blueprint, render_template, request, flash
from flask.helpers import flash
from flask.json import jsonify
from flask_login import login_required, current_user
from werkzeug.urls import url_encode_stream
from .models import Note
from . import db
import json



views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is to short!', category='error')
        else:
            new_Note = Note(data=Note, user_id = current_user.id)
            db.session.add(new_Note)
            db.session.commit()
            flash('Note added!', category='succes')
    return render_template("home.html", user =  current_user)

@views.route('/delete-note', methods = ['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit
            
        return jsonify({})
