'use client';

import React, { useState } from 'react';
import LoginForm from '@/components/auth/LoginForm';
import { useRouter } from 'next/navigation';
import { login } from '@/utils/auth';

export default function LoginPage() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const router = useRouter();

  const handleLogin = async (data: { email: string; password: string }) => {
    setLoading(true);
    setError('');

    try {
      const result = await login(data.email, data.password);
      if (result) {
        router.push('/dashboard');
      } else {
        setError('Invalid email or password');
      }
    } catch (err) {
      console.error('Login error:', err);
      setError('An error occurred during login');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
      <div className="w-full max-w-md">
        <div className="text-center">
          <h2 className="text-3xl font-extrabold text-gray-900 dark:text-white">
            Sign in to your account
          </h2>
        </div>
        {error && (
          <div className="mb-4 p-3 bg-red-100 text-red-700 rounded-md">
            {error}
          </div>
        )}
        <LoginForm onLogin={handleLogin} loading={loading} />
      </div>
    </div>
  );
}