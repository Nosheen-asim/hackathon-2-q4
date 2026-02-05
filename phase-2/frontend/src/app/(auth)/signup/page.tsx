'use client';

import React, { useState } from 'react';
import SignupForm from '@/components/auth/SignupForm';
import { useRouter } from 'next/navigation';
import { signup } from '@/utils/auth';

export default function SignupPage() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const router = useRouter();

  const handleSignup = async (data: { name: string; email: string; password: string }) => {
    setLoading(true);
    setError('');

    try {
      // Note: Our backend signup endpoint only takes email and password
      const result = await signup(data.name, data.email, data.password);
      if (result) {
        router.push('/dashboard');
      } else {
        setError('Failed to create account. Please try again.');
      }
    } catch (err) {
      console.error('Signup error:', err);
      setError('An error occurred during signup');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
      <div className="w-full max-w-md">
        <div className="text-center">
          <h2 className="text-3xl font-extrabold text-gray-900 dark:text-white">
            Create a new account
          </h2>
        </div>
        {error && (
          <div className="mb-4 p-3 bg-red-100 text-red-700 rounded-md">
            {error}
          </div>
        )}
        <SignupForm onSignup={handleSignup} loading={loading} />
      </div>
    </div>
  );
}