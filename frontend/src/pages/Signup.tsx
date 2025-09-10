import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Twitter } from 'lucide-react';
import { useAuth } from '../hooks/useAuth';

export function Signup() {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [passwordConfirmation, setPasswordConfirmation] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();
    const { signup } = useAuth();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();

        if (password !== passwordConfirmation) {
            setError('As senhas não coincidem.');
            return;
        }

        try {
            await signup(name, email, password); // 👈 usando o hook
            setError('');
            navigate('/'); // Redireciona para o feed depois de logar
        } catch (err) {
            console.error('Erro ao cadastrar:', err);
            setError('Não foi possível criar a conta.');
        }
    };

    return (
        <div className="min-h-screen bg-black flex items-center justify-center">
            <div className="w-full max-w-md space-y-8 p-6">
                <div className="flex justify-center">
                    <Twitter className="h-12 w-12 text-white" />
                </div>
                <h2 className="text-center text-3xl font-bold text-white">Crie sua Conta</h2>
                <form className="space-y-6" onSubmit={handleSubmit}>
                    <div>
                        <input
                            type="text"
                            placeholder="Nome"
                            className="w-full px-4 py-3 bg-black border border-gray-800 rounded-lg text-white focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
                            required
                            value={name}
                            onChange={(e) => setName(e.target.value)}
                        />
                    </div>
                    <div>
                        <input
                            type="email"
                            placeholder="Email"
                            className="w-full px-4 py-3 bg-black border border-gray-800 rounded-lg text-white focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
                            required
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                        />
                    </div>
                    <div>
                        <input
                            type="password"
                            placeholder="Senha"
                            className="w-full px-4 py-3 bg-black border border-gray-800 rounded-lg text-white focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
                            required
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                    </div>
                    <div>
                        <input
                            type="password"
                            placeholder="Repita a Senha"
                            className="w-full px-4 py-3 bg-black border border-gray-800 rounded-lg text-white focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
                            required
                            value={passwordConfirmation}
                            onChange={(e) => setPasswordConfirmation(e.target.value)}
                        />
                    </div>
                    {error && <p className="text-red-500">{error}</p>}
                    <button
                        type="submit"
                        className="w-full py-3 bg-blue-500 text-white rounded-full font-bold hover:bg-blue-600"
                    >
                        Cadastrar-se
                    </button>
                </form>
                <p className="text-center text-gray-500">
                    Já tem uma Conta?{' '}
                    <a href="/login" className="text-blue-500 hover:underline">
                        Entrar
                    </a>
                </p>
            </div>
        </div>
    );
}




// import React, { useState } from 'react';
// import { useNavigate } from 'react-router-dom'; // Import para redirecionamento
// import { Twitter } from 'lucide-react';

// export function Signup() {
//     const [email, setEmail] = useState('');
//     const [password, setPassword] = useState('');
//     const [passwordConfirmation, setPasswordConfirmation] = useState('');
//     const [error, setError] = useState('');
//     const navigate = useNavigate(); // Hook para navegação

//     const handleSubmit = async (e: React.FormEvent) => {
//         e.preventDefault();

//         // Verificar se as senhas coincidem
//         if (password !== passwordConfirmation) {
//             setError('Passwords do not match');
//             return;
//         }

//         try {
//             const response = await fetch('https://bookstore-v1-fa2u.onrender.com/api/users/', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json',
//                 },
//                 body: JSON.stringify({
//                     email: email,
//                     password: password,
//                     password_confirmation: passwordConfirmation, // Enviar para o back-end
//                 }),
//             });

//             if (response.ok) {
//                 console.log('User created successfully');
//                 setError('');
//                 navigate('/login'); // Redirecionar para a página de login
//             } else {
//                 const data = await response.json();
//                 setError(data.detail || 'Failed to create user');
//             }
//         } catch (err) {
//             console.error('Error:', err);
//             setError('An unexpected error occurred.');
//         }
//     };

//     return (
//         <div className="min-h-screen bg-black flex items-center justify-center">
//             <div className="w-full max-w-md space-y-8 p-6">
//                 <div className="flex justify-center">
//                     <Twitter className="h-12 w-12 text-white" />
//                 </div>
//                 <h2 className="text-center text-3xl font-bold text-white">Crie sua Conta</h2>
//                 <form className="space-y-6" onSubmit={handleSubmit}>
//                     <div>
//                         <input
//                             type="email"
//                             placeholder="Email"
//                             className="w-full px-4 py-3 bg-black border border-gray-800 rounded-lg text-white focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
//                             required
//                             value={email}
//                             onChange={(e) => setEmail(e.target.value)}
//                         />
//                     </div>
//                     <div>
//                         <input
//                             type="password"
//                             placeholder="Senha"
//                             className="w-full px-4 py-3 bg-black border border-gray-800 rounded-lg text-white focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
//                             required
//                             value={password}
//                             onChange={(e) => setPassword(e.target.value)}
//                         />
//                     </div>
//                     <div>
//                         <input
//                             type="password"
//                             placeholder="Repita a Senha"
//                             className="w-full px-4 py-3 bg-black border border-gray-800 rounded-lg text-white focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
//                             required
//                             value={passwordConfirmation}
//                             onChange={(e) => setPasswordConfirmation(e.target.value)}
//                         />
//                     </div>
//                     {error && <p className="text-red-500">{error}</p>}
//                     <button
//                         type="submit"
//                         className="w-full py-3 bg-blue-500 text-white rounded-full font-bold hover:bg-blue-600"
//                     >
//                         Cadastra-se
//                     </button>
//                 </form>
//                 <p className="text-center text-gray-500">
//                     Já tem uma Conta?{' '}
//                     <a href="/" className="text-blue-500 hover:underline">
//                         Entrar
//                     </a>
//                 </p>
//             </div>
//         </div>
//     );
// }
