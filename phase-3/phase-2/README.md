# Todo Application Frontend

A professional, modern, and clean Next.js frontend for a Todo application with authentication, dashboard, and CRUD operations.

## Features

- Modern UI with Tailwind CSS
- Responsive design for all device sizes
- Authentication system (login/signup)
- Full CRUD operations for todos
- Task filtering and sorting
- Loading states and error handling
- Clean, accessible codebase

## Tech Stack

- Next.js (App Router)
- TypeScript
- Tailwind CSS
- React Hooks

## Folder Structure

```
src/
├── app/
│   ├── (auth)/
│   │   ├── login/
│   │   │   └── page.tsx
│   │   └── signup/
│   │       └── page.tsx
│   ├── dashboard/
│   │   └── page.tsx
│   ├── layout.tsx
│   ├── page.tsx
│   └── globals.css
├── components/
│   ├── ui/
│   │   ├── Button.tsx
│   │   ├── Input.tsx
│   │   ├── Card.tsx
│   │   └── Modal.tsx
│   ├── auth/
│   │   ├── LoginForm.tsx
│   │   └── SignupForm.tsx
│   ├── todo/
│   │   ├── TodoList.tsx
│   │   ├── TodoItem.tsx
│   │   ├── CreateTodoModal.tsx
│   │   └── EditTodoModal.tsx
│   └── layout/
│       ├── Header.tsx
│       └── Sidebar.tsx
├── styles/
│   └── globals.css
├── utils/
│   ├── auth.ts
│   ├── constants.ts
│   └── helpers.ts
└── types/
    └── index.ts
```

## Getting Started

First, install the dependencies:

```bash
npm install
```

Then, run the development server:

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## Environment Variables

If needed, create a `.env.local` file in the root directory with the following variables:

```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:3001/api
```

## Color Palette

- Primary: Soft blue (#3B82F6)
- Secondary: Light gray (#F3F4F6)
- Success: Green (#10B981)
- Warning: Amber (#F59E0B)
- Danger: Red (#EF4444)
- Background: White/Off-white (#FFFFFF/#FAFAFA)
- Text: Dark gray (#1F2937) and medium gray (#6B7280)

## Type Definitions

- User: { id, name, email }
- Todo: { id, title, description, completed, createdAt, updatedAt, dueDate }
- AuthState: { user, isAuthenticated, loading }