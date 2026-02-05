import React from 'react';
import { Todo } from '@/types';

interface TodoItemProps {
  todo: Todo;
  onToggle: (id: string) => void;
  onEdit: (todo: Todo) => void;
  onDelete: (id: string) => void;
}

const TodoItem: React.FC<TodoItemProps> = ({ todo, onToggle, onEdit, onDelete }) => {
  const formatDate = (dateString: string) => {
    const options: Intl.DateTimeFormatOptions = { year: 'numeric', month: 'short', day: 'numeric' };
    return new Date(dateString).toLocaleDateString(undefined, options);
  };

  return (
    <div className={`flex items-center justify-between p-4 border border-gray-200 dark:border-gray-700 rounded-lg mb-2 ${todo.completed ? 'bg-green-50 dark:bg-gray-700' : 'bg-white dark:bg-gray-800'}`}>
      <div className="flex items-center">
        <input
          type="checkbox"
          checked={todo.completed}
          onChange={() => onToggle(todo.id)}
          className="h-5 w-5 text-blue-600 rounded focus:ring-blue-500"
        />
        <div className="ml-4">
          <h3 className={`text-lg font-medium ${todo.completed ? 'line-through text-gray-500' : 'text-gray-900 dark:text-white'}`}>
            {todo.title}
          </h3>
          {todo.description && (
            <p className="text-gray-600 dark:text-gray-400 mt-1">{todo.description}</p>
          )}
          {todo.dueDate && (
            <p className="text-sm text-gray-500 dark:text-gray-400 mt-1">
              Due: {formatDate(todo.dueDate)}
            </p>
          )}
          <div className="flex items-center text-xs text-gray-500 dark:text-gray-400 mt-1">
            <span>Created: {formatDate(todo.createdAt)}</span>
            <span className="mx-2">•</span>
            <span>Updated: {formatDate(todo.updatedAt)}</span>
          </div>
        </div>
      </div>
      <div className="flex space-x-2">
        <button
          onClick={() => onEdit(todo)}
          className="text-blue-600 hover:text-blue-900 dark:text-blue-400 dark:hover:text-blue-300"
        >
          <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
            <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
          </svg>
        </button>
        <button
          onClick={() => onDelete(todo.id)}
          className="text-red-600 hover:text-red-900 dark:text-red-400 dark:hover:text-red-300"
        >
          <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
            <path fillRule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clipRule="evenodd" />
          </svg>
        </button>
      </div>
    </div>
  );
};

export default TodoItem;