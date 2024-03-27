document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const questions = document.querySelectorAll('.question');

    form.addEventListener('submit', (event) => {
        let allAnswered = true;
        
        questions.forEach((question) => {
            if (!question.querySelector('input[type="radio"]:checked')) {
                allAnswered = false;
                question.style.borderLeftColor = 'red'; // Highlight unanswered questions
            } else {
                question.style.borderLeftColor = '#b76e79'; // Reset if answered
            }
        });

        if (!allAnswered) {
            event.preventDefault(); // Prevent form submission if any question is unanswered
            alert('Please answer all questions before proceeding.');
        }
    });
});
