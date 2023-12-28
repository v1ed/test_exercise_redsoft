from app import app, db
from app.forms import LoginForm, RegistrationForm, Sort
from app.models import User

from flask import render_template, redirect, request, url_for
from flask_login import current_user, login_user, logout_user, login_required

import asyncio
import json


async def get_user(username):
    return User.query.filter_by(username=username).first()


def get_parents(data, l):
    for d in data:
        if 'children' in d.keys():
            l += [{"key": d["key"], "name": d["name"]}]
            get_parents(d["children"], l)
    return l


def parent_searcher(data, key):
    for d in data:
        if d["key"] == key:
            if 'children' in d.keys():
                return d["children"]
            return None
        elif 'children' in d.keys():
            p = parent_searcher(d["children"], key)
            if p is not None:
                return p


async def get_data(key=""):
    with open("server_data.json", "r") as f:
        data = json.load(f)
    parents = get_parents(data, [])
    childrens = parent_searcher(data, key)
    asyncio.sleep(1)
    return parents, childrens


@app.route('/')
def index():
    return render_template("index.html", title="Index")


@app.route('/browse', methods=["GET", "POST"])
@login_required
async def browse():
    parent_key = request.args.get('parent', type=str)
    parents, childrens = await get_data(parent_key)
    print(request.data)
    # form = Sort()
    # if form.validate_on_submit():
    #     childrens = {k: v for k, v in sorted(childrens.items(), key=lambda item: item[1])}
    return render_template("browse.html", 
                           title="Browse", 
                           parents=parents, 
                           childrens=childrens, 
                           cur_parent=parent_key)


@app.route('/login', methods=["GET", "POST"])
async def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = await get_user(form.username.data)
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for('login'))
        login_user(user, remember=True)
        return redirect(url_for('index'))
    return render_template('login.html', title="Log in", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)