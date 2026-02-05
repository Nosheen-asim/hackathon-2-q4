'use client';

import React, { useState, useEffect } from 'react';
import Header from '@/components/layout/Header';
import Sidebar from '@/components/layout/Sidebar';
import TodoList from '@/components/todo/TodoList';
import CreateTodoModal from '@/components/todo/CreateTodoModal';
import EditTodoModal from '@/components/todo/EditTodoModal';
import { Todo, User } from '@/types';
import { getCurrentUser } from '@/utils/auth';
import { API_BASE_URL } from '@/utils/constants';

export default function DashboardPage() {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [showEditModal, setShowEditModal] = useState(false);
  const [editingTodo, setEditingTodo] = useState<Todo | null>(null);
  const [loading, setLoading] = useState(true);
  const [filter, setFilter] = useState<'all' | 'active' | 'completed'>('all');
  const [currentUser, setCurrentUser] = useState<User | null>(null);

  // Fetch user data from auth system
  useEffect(() => {
    const user = getCurrentUser();
    if (user) {
      setCurrentUser(user);
    } else {
      // Redirect to login if not authenticated
      window.location.href = '/login';
    }
  }, []);

  // Fetch todos from backend API
  useEffect(() => {
    const fetchTodos = async () => {
      try {
        const token = localStorage.getItem('access_token');
        if (!token) {
          window.location.href = '/login';
          return;
        }

        const response = await fetch(`${API_BASE_URL}/todos`, {
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          }
        });

        if (response.ok) {
          const data = await response.json();
          setTodos(data.todos || []);
        } else if (response.status === 401) {
          // Unauthorized - redirect to login
          localStorage.removeItem('access_token');
          window.location.href = '/login';
        } else {
          console.error('Failed to fetch todos:', response.status);
        }
      } catch (error) {
        console.error('Error fetching todos:', error);
      } finally {
        setLoading(false);
      }
    };

    if (currentUser) {
      fetchTodos();
    }
  }, [currentUser]);

  const handleCreateTodo = async (data: { title: string; description: string; dueDate?: string }) => {
    try {
      const token = localStorage.getItem('access_token');
      if (!token) {
        window.location.href = '/login';
        return;
      }

      const response = await fetch(`${API_BASE_URL}/todos`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });

      if (response.ok) {
        const newTodo = await response.json();
        setTodos([newTodo, ...todos]);
        setShowCreateModal(false);
      } else if (response.status === 401) {
        // Unauthorized - redirect to login
        localStorage.removeItem('access_token');
        window.location.href = '/login';
      } else {
        console.error('Failed to create todo:', response.status);
      }
    } catch (error) {
      console.error('Error creating todo:', error);
    }
  };

  const handleUpdateTodo = async (id: string, data: { title: string; description: string; dueDate?: string }) => {
    try {
      const token = localStorage.getItem('access_token');
      if (!token) {
        window.location.href = '/login';
        return;
      }

      const response = await fetch(`${API_BASE_URL}/todos/${id}`, {
        method: 'PUT',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });

      if (response.ok) {
        const updatedTodo = await response.json();
        setTodos(todos.map(todo =>
          todo.id === id ? updatedTodo : todo
        ));
        setShowEditModal(false);
        setEditingTodo(null);
      } else if (response.status === 401) {
        // Unauthorized - redirect to login
        localStorage.removeItem('access_token');
        window.location.href = '/login';
      } else {
        console.error('Failed to update todo:', response.status);
      }
    } catch (error) {
      console.error('Error updating todo:', error);
    }
  };

  const handleToggleTodo = async (id: string) => {
    try {
      const token = localStorage.getItem('access_token');
      if (!token) {
        window.location.href = '/login';
        return;
      }

      const todo = todos.find(t => t.id === id);
      if (!todo) return;

      const response = await fetch(`${API_BASE_URL}/todos/${id}/complete`, {
        method: 'PATCH',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ completed: !todo.completed })
      });

      if (response.ok) {
        const updatedTodo = await response.json();
        setTodos(todos.map(todo =>
          todo.id === id ? updatedTodo : todo
        ));
      } else if (response.status === 401) {
        // Unauthorized - redirect to login
        localStorage.removeItem('access_token');
        window.location.href = '/login';
      } else {
        console.error('Failed to toggle todo:', response.status);
      }
    } catch (error) {
      console.error('Error toggling todo:', error);
    }
  };

  const handleDeleteTodo = async (id: string) => {
    try {
      const token = localStorage.getItem('access_token');
      if (!token) {
        window.location.href = '/login';
        return;
      }

      const response = await fetch(`${API_BASE_URL}/todos/${id}`, {
        method: 'DELETE',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        }
      });

      if (response.ok) {
        setTodos(todos.filter(todo => todo.id !== id));
      } else if (response.status === 401) {
        // Unauthorized - redirect to login
        localStorage.removeItem('access_token');
        window.location.href = '/login';
      } else {
        console.error('Failed to delete todo:', response.status);
      }
    } catch (error) {
      console.error('Error deleting todo:', error);
    }
  };

  const handleEditTodo = (todo: Todo) => {
    setEditingTodo(todo);
    setShowEditModal(true);
  };

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    window.location.href = '/login';
  };

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 flex">
      <Sidebar currentUser={currentUser || undefined} />

      <div className="flex-1 flex flex-col overflow-hidden">
        <Header user={currentUser || undefined} onLogout={handleLogout} />

        <main className="flex-1 overflow-y-auto p-6">
          <TodoList
            todos={todos}
            onToggle={handleToggleTodo}
            onEdit={handleEditTodo}
            onDelete={handleDeleteTodo}
            onCreate={() => setShowCreateModal(true)}
            loading={loading}
            filter={filter}
            setFilter={setFilter}
          />
        </main>
      </div>

      <CreateTodoModal
        isOpen={showCreateModal}
        onClose={() => setShowCreateModal(false)}
        onCreate={handleCreateTodo}
      />

      <EditTodoModal
        isOpen={showEditModal}
        onClose={() => setShowEditModal(false)}
        todo={editingTodo}
        onUpdate={handleUpdateTodo}
      />
    </div>
  );
}