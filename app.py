import os
from flask import Flask, render_template, request, redirect, url_for, session, make_response
from results.interpreter import HormoneResultInterpreter
from weasyprint import HTML


app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html')

hormones = ['adrenaline', 'dopamine', 'endorphins', 'estrogen', 'norepinephrine',
            'oxytocin', 'serotonin', 'testosterone', 'vasopressin']

@app.route('/<hormone>_exp')
def show_explanation(hormone):
    if hormone in hormones:
        return render_template(f'hormone_explanations/{hormone}_exp.html')
    return redirect(url_for('index'))

@app.route('/<hormone>_quiz', methods=['GET', 'POST'])
def show_quiz(hormone):
    if request.method == 'POST':
        score = 0

        for i in range(1, 6):
            score += float(request.form.get(f'question{i}', 0))

        session[f'{hormone}_score'] = score

        next_index = hormones.index(hormone) + 1
        if next_index < len(hormones):
            next_hormone = hormones[next_index]
            return redirect(url_for('show_explanation', hormone=next_hormone))
        return redirect(url_for('user_data_form'))

    if hormone in hormones:
        return render_template(f'hormone_quizzes/{hormone}_quiz.html')
    return redirect(url_for('index'))

@app.route('/user_data_form', methods=['GET', 'POST'])
def user_data_form():
    if request.method == 'POST':
        session['user_age'] = request.form['age']
        return redirect(url_for('results'))
    
    return render_template('user_data_form.html')

@app.route('/results')
def results():
    user_scores = {hormone: session.get(f'{hormone}_score', 0) for hormone in hormones}
    interpreter = HormoneResultInterpreter(user_scores)
    overall_score = interpreter.overall_score
    overall_interpretation = interpreter.overall_interpretation
    detailed_feedback = interpreter.get_detailed_feedback(overall_interpretation['level'])
    hormone_definitions = interpreter.get_hormone_definitions()
    hormone_interpretations = interpreter.hormone_interpretations

    level = overall_interpretation['level']
    result_images = {
        'Very Low': 'very-low.png',
        'Low': 'low.png',
        'Medium': 'medium.png',
        'High': 'high.png',
        'Very High': 'very-high.png'
    }
    result_image = result_images[level]
    
    return render_template('results.html', overall_score=overall_score, 
                           overall_interpretation=overall_interpretation, 
                           detailed_feedback=detailed_feedback,
                           hormone_definitions=hormone_definitions,
                           results_data=hormone_interpretations,
                           result_image=result_image)

@app.route('/results/pdf')
def results_pdf():
    # Re-fetch user's results and data for the PDF
    user_scores = {hormone: session.get(f'{hormone}_score', 0) for hormone in hormones}
    interpreter = HormoneResultInterpreter(user_scores)
    overall_score = interpreter.overall_score
    overall_interpretation = interpreter.overall_interpretation
    detailed_feedback = interpreter.get_detailed_feedback(overall_interpretation['level'])
    hormone_definitions = interpreter.get_hormone_definitions()
    hormone_interpretations = interpreter.hormone_interpretations

    # Last added:
    level = overall_interpretation['level']
    result_images = {
        'Very Low': 'very-low.png',
        'Low': 'low.png',
        'Medium': 'medium.png',
        'High': 'high.png',
        'Very High': 'very-high.png'
    }
    result_image = result_images[level]
    
    # Make sure to pass the same data you pass to the results page
    html = render_template('results_pdf.html', overall_score=overall_score, 
                           overall_interpretation=overall_interpretation, 
                           detailed_feedback=detailed_feedback,
                           hormone_definitions=hormone_definitions,
                           results_data=hormone_interpretations,
                           result_image=result_image)

    pdf = HTML(string=html).write_pdf()
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=results.pdf'
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8000)))
