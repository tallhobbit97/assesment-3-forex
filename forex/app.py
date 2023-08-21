from flask import Flask, request, render_template, flash, redirect
from currencies import check_currency, make_exchange

app = Flask('__name__')
app.config['SECRET_KEY'] = 'dshjKLSDAsdkhH'

@app.route('/')
def homepage():
    """Shows user the homepage"""
    return render_template('index.html')

@app.route('/exchange', methods=['POST'])
def exchange():
    """Checks for valid currency and handles exchange"""
    frm = request.form['from']
    to = request.form['to']
    amt = request.form['amount']
    if not check_currency(frm):
        flash(f'Not a valid code: {frm}')
        return redirect('/')
    
    if not check_currency(to):
        flash(f'Not a valid code: {to}')
        return redirect('/')
    
    try:
        int(request.form['amount'])
    except:
        flash('Not a valid number')
        return redirect('/')

    return render_template('result.html', result=make_exchange(frm, to, int(amt)))