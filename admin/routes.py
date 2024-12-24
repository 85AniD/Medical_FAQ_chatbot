from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from .models import Admin, UserProfile

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        admin = Admin.query.filter_by(username=username).first()
        if admin and admin.password == password:
            login_user(admin)
            return redirect(url_for('admin.dashboard'))
        user = UserProfile.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('admin.dashboard'))
    return render_template('admin_login.html')

@admin_blueprint.route('/admin/logout')
def admin_logout():
    logout_user()
    return redirect(url_for('admin.login'))

@admin_blueprint.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')
