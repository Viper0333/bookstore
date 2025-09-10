// src/App.tsx
import { useEffect, useState } from 'react';
import { AppRouter } from './routes';
import { useAuth } from './hooks/useAuth';

const API_URL = import.meta.env.VITE_API_URL; // ✅ pega URL do backend

function App() {
  const { restoreSession } = useAuth(); // Não usamos isAuthenticated aqui
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    restoreSession();
    setIsLoading(false);

    // 🔍 Teste de conexão com backend
    console.log("API_URL carregada:", API_URL);

    fetch(`${API_URL}/hello/`)
      .then(res => res.text())
      .then(data => console.log("✅ Backend respondeu:", data))
      .catch(err => console.error("❌ Erro ao chamar backend:", err));
  }, [restoreSession]);

  if (isLoading) {
    return <div>Carregando...</div>;
  }

  return <AppRouter />;
}

export default App;



// import React, { useEffect, useState } from 'react';
// import { AppRouter } from './routes';
// import { useAuth } from './hooks/useAuth';

// function App() {
//   const { restoreSession } = useAuth();
//   const [isLoading, setIsLoading] = useState(true);

//   useEffect(() => {
//     restoreSession();
//     setIsLoading(false);
//   }, [restoreSession]);

//   if (isLoading) {
//     return <div>Carregando...</div>; // Placeholder para enquanto o estado é restaurado
//   }

//   return <AppRouter />;
// }

// export default App;
