import { create } from 'zustand';

interface AuthState {
    isAuthenticated: boolean;
    token: string | null;
    refreshToken: string | null;
    login: (email: string, password: string) => Promise<void>;
    signup: (name: string, email: string, password: string) => Promise<void>;
    logout: () => void;
    restoreSession: () => void;
    authFetch: (url: string, options?: RequestInit) => Promise<Response>;
}

// ✅ Usa a variável de ambiente corretamente
const API_URL = import.meta.env.VITE_API_URL;

export const useAuth = create<AuthState>((set, get) => ({
    isAuthenticated: false,
    token: localStorage.getItem('authToken'),
    refreshToken: localStorage.getItem('refreshToken'),

    login: async (email, password) => {
        try {
            const resp = await fetch(`${API_URL}/api/token/`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, password }),
            });

            if (!resp.ok) throw new Error('Falha no login');

            const data = await resp.json();

            localStorage.setItem('authToken', data.access);
            localStorage.setItem('refreshToken', data.refresh);

            set({
                isAuthenticated: true,
                token: data.access,
                refreshToken: data.refresh,
            });
        } catch (error) {
            console.error('Erro ao fazer login:', error);
            set({ isAuthenticated: false, token: null, refreshToken: null });
        }
    },

    signup: async (name, email, password) => {
        try {
            const resp = await fetch(`${API_URL}/api/users/`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    name,
                    email,
                    password,
                    password_confirmation: password,
                    bio: "",
                    avatar: null,
                }),
            });

            if (!resp.ok) throw new Error('Falha no cadastro');

            await resp.json();
            await get().login(email, password); // Login automático
        } catch (error) {
            console.error('Erro ao fazer cadastro:', error);
        }
    },

    logout: () => {
        localStorage.removeItem('authToken');
        localStorage.removeItem('refreshToken');
        set({ isAuthenticated: false, token: null, refreshToken: null });
        window.location.href = '/login';
    },

    restoreSession: () => {
        const token = localStorage.getItem('authToken');
        const refreshToken = localStorage.getItem('refreshToken');
        if (token && refreshToken) {
            set({ isAuthenticated: true, token, refreshToken });
        } else {
            set({ isAuthenticated: false, token: null, refreshToken: null });
        }
    },

    authFetch: async (url, options: RequestInit = {}) => {
        const { token } = get();

        const headers = {
            ...options.headers,
            Authorization: token ? `Bearer ${token}` : '',
            'Content-Type': 'application/json',
        };

        return fetch(`${API_URL}${url}`, {
            ...options,
            headers,
        });
    },
}));
