import React from 'react';
import Link from 'next/link';
import Button from '../ui/Button';

interface HeaderProps {
  user?: { name: string };
  onLogout?: () => void;
}

const Header: React.FC<HeaderProps> = ({ user, onLogout }) => {
  return (
    <header className="bg-white dark:bg-gray-800 shadow-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <Link href="/" className="flex-shrink-0 flex items-center">
              <span className="text-xl font-bold text-blue-600">TodoApp</span>
            </Link>
          </div>
          <div className="flex items-center">
            {user ? (
              <div className="flex items-center space-x-4">
                <span className="text-gray-700 dark:text-gray-300">Welcome, {user.name}</span>
                <Button variant="secondary" onClick={onLogout}>Logout</Button>
              </div>
            ) : (
              <div className="flex space-x-4">
                <Link href="/login">
                  <Button variant="secondary">Login</Button>
                </Link>
                <Link href="/signup">
                  <Button variant="primary">Sign Up</Button>
                </Link>
              </div>
            )}
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;