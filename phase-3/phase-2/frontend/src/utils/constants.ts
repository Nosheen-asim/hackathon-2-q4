// Application constants

export const APP_NAME = 'TodoApp';
export const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000';
export const AUTH_TOKEN_KEY = 'todo_app_auth_token';

// Routes
export const ROUTES = {
  HOME: '/',
  LOGIN: '/login',
  SIGNUP: '/signup',
  DASHBOARD: '/dashboard',
  PROFILE: '/profile',
};

// Messages
export const MESSAGES = {
  WELCOME: 'Welcome to TodoApp!',
  LOGGED_IN: 'Successfully logged in',
  LOGGED_OUT: 'Successfully logged out',
  TODO_CREATED: 'Todo created successfully',
  TODO_UPDATED: 'Todo updated successfully',
  TODO_DELETED: 'Todo deleted successfully',
};

// Validation
export const VALIDATION = {
  EMAIL_PATTERN: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
  PASSWORD_MIN_LENGTH: 6,
  TITLE_MAX_LENGTH: 100,
  DESCRIPTION_MAX_LENGTH: 500,
};

// Colors
export const COLORS = {
  PRIMARY: '#3B82F6',
  SECONDARY: '#F3F4F6',
  SUCCESS: '#10B981',
  WARNING: '#F59E0B',
  DANGER: '#EF4444',
  BACKGROUND: '#FFFFFF',
  TEXT: '#1F2937',
};