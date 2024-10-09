#!/usr/bin/env python
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.tag import Tag
from app.forms.tag_form import TagForm
from app.extensions import db

tag_bp = Blueprint('tag', __name__)

@tag_bp.route('/tags')
def list_tags():
   tags = Tag.query.all()
   return render_template('tags.html', tags=tags)

@tag_bp.route('/tags/new', methods=['GET', 'POST'])
def new_tag():
   form = TagForm()
   if form.validate_on_submit():
       new_tag = Tag(title=form.title.data)
       db.session.add(new_tag)
       db.session.commit()
       flash('Tag created successfully!')
       return redirect(url_for('tag.list_tags'))
   return render_template('new_tag.html', form=form)

@tag_bp.route('/tags/edit/<int:tag_id>', methods=['GET', 'POST'])
def edit_tag(tag_id):
   tag = Tag.query.get_or_404(tag_id)
   form = TagForm(obj=tag)
   if form.validate_on_submit():
       tag.title = form.title.data
       db.session.commit()
       flash('Tag updated successfully!')
       return redirect(url_for('tag.list_tags'))
   return render_template('edit_tag.html', form=form)