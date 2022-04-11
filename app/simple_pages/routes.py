from flask import Blueprint, render_template, redirect, url_for, send_file

simple_pages = Blueprint('simple_pages', __name__)

@simple_pages.route('/test')
def indexx():
  return 'I like cookies'

@simple_pages.route('/about')
def about():
  return 'I like cookies'

@simple_pages.route('/test2')
def about_me():
  return redirect(url_for('simple_pages.about'))

@simple_pages.route('/test3')
def legal():
    return 'I like cookies'