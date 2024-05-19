document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('loginForm');

  loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      
      const username = document.getElementById('username').value;
      const password = document.getElementById('password').value;

      const response = await fetch('/check_login', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({ username, password }),
      });

      const result = await response.json();

      if (result.success) {
          window.location.href = '/profile';
      } else {
          alert('Invalid username or password');
      }
  });
});
