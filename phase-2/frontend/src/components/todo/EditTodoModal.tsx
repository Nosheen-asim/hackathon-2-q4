import React, { useState, useEffect } from 'react';
import Modal from '../ui/Modal';
import Input from '../ui/Input';
import Button from '../ui/Button';
import { Todo } from '@/types';

interface FormData {
  title: string;
  description: string;
  dueDate?: string;
}

interface EditTodoModalProps {
  isOpen: boolean;
  onClose: () => void;
  todo: Todo | null;
  onUpdate: (id: string, data: FormData) => void;
  loading?: boolean;
}

const EditTodoModal: React.FC<EditTodoModalProps> = ({ isOpen, onClose, todo, onUpdate, loading = false }) => {
  const [formData, setFormData] = useState<FormData>({
    title: '',
    description: '',
    dueDate: '',
  });
  const [errors, setErrors] = useState<Partial<FormData>>({});

  useEffect(() => {
    if (todo) {
      setFormData({
        title: todo.title,
        description: todo.description,
        dueDate: todo.dueDate || '',
      });
    }
  }, [todo]);

  const validate = (): boolean => {
    const newErrors: Partial<FormData> = {};
    if (!formData.title.trim()) {
      newErrors.title = 'Title is required';
    } else if (formData.title.length > 100) {
      newErrors.title = 'Title must be less than 100 characters';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
    // Clear error when user starts typing
    if (errors[name as keyof FormData]) {
      setErrors({
        ...errors,
        [name]: undefined,
      });
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (todo && validate()) {
      onUpdate(todo.id, formData);
    }
  };

  if (!todo) return null;

  return (
    <Modal isOpen={isOpen} onClose={onClose} title="Edit Task">
      <form onSubmit={handleSubmit} className="space-y-4">
        <Input
          label="Title"
          type="text"
          id="title"
          name="title"
          value={formData.title}
          onChange={handleChange}
          error={errors.title}
          placeholder="What needs to be done?"
        />

        <div>
          <label htmlFor="description" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
            Description
          </label>
          <textarea
            id="description"
            name="description"
            value={formData.description}
            onChange={handleChange}
            rows={3}
            className="input-field"
            placeholder="Add details..."
          />
        </div>

        <Input
          label="Due Date"
          type="date"
          id="dueDate"
          name="dueDate"
          value={formData.dueDate}
          onChange={handleChange}
        />

        <div className="flex justify-end space-x-3 pt-4">
          <Button type="button" variant="secondary" onClick={onClose}>
            Cancel
          </Button>
          <Button type="submit" variant="primary" isLoading={loading}>
            Update Task
          </Button>
        </div>
      </form>
    </Modal>
  );
};

export default EditTodoModal;