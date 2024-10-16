#!/usr/bin/env python
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.prop import Prop
from app.forms.prop_form import PropForm
from app.extensions import db

prop_bp = Blueprint('prop', __name__)

@prop_bp.route('/')
def list_props():
   props = Prop.query.all()
   return render_template('props.html', props=props)

@prop_bp.route('/new', methods=['GET', 'POST'])
def new_prop():
   form = PropForm()
   if form.validate_on_submit():
       new_prop = Prop(name=form.name.data, model_url=form.model_url.data)
       db.session.add(new_prop)
       db.session.commit()
       flash('Prop created successfully!')
       return redirect(url_for('prop.list_props'))
   return render_template('new_prop.html', form=form)

@prop_bp.route('/edit/<int:prop_id>', methods=['GET', 'POST'])
def edit_prop(prop_id):
   prop = Prop.query.get_or_404(prop_id)
   form = PropForm(obj=prop)
   if form.validate_on_submit():
       prop.name = form.name.data
       prop.model_url = form.model_url.data
       db.session.commit()
       flash('Prop updated successfully!')
       return redirect(url_for('prop.list_props'))
   return render_template('edit_prop.html', form=form)