// Pequeno script para chamar a API REST com fetch e JWT.
async function apiPost(url, data) {
  const res = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  const payload = await res.json().catch(()=>({}));
  if (!res.ok) throw payload;
  return payload;
}

async function apiGet(url) {
  const token = localStorage.getItem('access');
  const res = await fetch(url, {
    headers: token ? { 'Authorization': 'Bearer ' + token } : {},
  });
  const payload = await res.json().catch(()=>({}));
  if (!res.ok) throw payload;
  return payload;
}

// Login form
const loginForm = document.getElementById('login-form');
if (loginForm) {
  loginForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const data = Object.fromEntries(new FormData(loginForm).entries());
    const msg = document.getElementById('login-msg');
    msg.textContent = '...';
    try {
      const tokens = await apiPost('/api/auth/login', data);
      localStorage.setItem('access', tokens.access);
      localStorage.setItem('refresh', tokens.refresh);
      const me = await apiGet('/api/auth/me');
      msg.textContent = 'Bem-vindo, ' + (me.first_name || me.username) + '!';
    } catch (err) {
      msg.textContent = (err && (err.detail || JSON.stringify(err))) || 'Erro no login';
    }
  });
}

// Register form
const registerForm = document.getElementById('register-form');
if (registerForm) {
  registerForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const data = Object.fromEntries(new FormData(registerForm).entries());
    const msg = document.getElementById('register-msg');
    msg.textContent = '...';
    try {
      await apiPost('/api/auth/register', data);
      msg.textContent = 'Conta criada! Agora faça login.';
    } catch (err) {
      msg.textContent = (err && (err.detail || JSON.stringify(err))) || 'Erro no cadastro';
    }
  });
}
