// Real authentication utilities that interact with your backend API
import { API_BASE_URL } from './constants';

export const isAuthenticated = (): boolean => {
  // Check if user has a valid token
  const token = localStorage.getItem('access_token');
  return !!token;
};

export const login = async (email: string, password: string): Promise<{ user: any; token: string } | null> => {
  try {
    const response = await fetch(`${API_BASE_URL}/auth/signin`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email, password }),
    });

    if (response.ok) {
      const data = await response.json();
      localStorage.setItem('access_token', data.access_token);
      return { user: data.user, token: data.access_token };
    } else {
      console.error('Login failed:', response.status);
      return null;
    }
  } catch (error) {
    console.error('Login error:', error);
    return null;
  }
};

export const signup = async (name: string, email: string, password: string): Promise<{ user: any; token: string } | null> => {
  try {
    const response = await fetch(`${API_BASE_URL}/auth/signup`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email, password }), // Backend only expects email and password
    });

    if (response.ok) {
      const data = await response.json();
      localStorage.setItem('access_token', data.access_token);
      return { user: data.user, token: data.access_token };
    } else {
      console.error('Signup failed:', response.status);
      return null;
    }
  } catch (error) {
    console.error('Signup error:', error);
    return null;
  }
};

export const logout = (): void => {
  localStorage.removeItem('access_token');
};

export const getCurrentUser = (): { id: string; name: string; email: string } | null => {
  // In a real app, you would decode the JWT token or retrieve user info from your backend
  const token = localStorage.getItem('access_token');
  if (token) {
    // Decode JWT token to get user info
    try {
      const base64Url = token.split('.')[1];
      const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
      const jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
      }).join(''));

      const decodedToken = JSON.parse(jsonPayload);
      return {
        id: decodedToken.user_id || '1',
        name: decodedToken.name || 'User',
        email: decodedToken.sub || 'user@example.com'
      };
    } catch (error) {
      console.error('Error decoding token:', error);
      return null;
    }
  }
  return null;
};

// Helper function to include auth token in API requests
export const authHeaders = (): Record<string, string> => {
  const token = localStorage.getItem('access_token');
  return token ? {
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json'
  } : { 'Content-Type': 'application/json' };
};