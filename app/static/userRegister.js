document.addEventListener('DOMContentLoaded', () => {
    const registrationForm = document.getElementById('registrationForm');


    registrationForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      const passwordInput = document.getElementById('password').value();
      const confirmPasswordInput = document.getElementById('confirmPassword').value();
      const username =  document.getElementById('username').value();
      const email =  document.getElementById('email').value();


      const response = await fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ passwordInput, confirmPasswordInput, username, email }),
    });

    const result = await response.json();

    if (result.success) {
        window.location.href = '/home';
    } else if (result.new_user) {
        alert('Invalid username or password');
        window.location.href = '/home';
    }
    else if(result.password_confirm) {
        alert('Passwords do not match');
        window.location.href = '/home';
      } 
    });
});