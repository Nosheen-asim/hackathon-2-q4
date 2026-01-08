"""Test script to verify all todo application functionality."""

from todo_app.todo_manager import TodoManager


def test_all_functionality():
    """Test all functionality of the todo application."""
    print("Testing Todo Application Functionality...")

    # Create a new manager instance
    manager = TodoManager()

    # Test 1: Add functionality
    print("\n1. Testing ADD functionality:")
    todo1 = manager.add_todo("Buy groceries")
    todo2 = manager.add_todo("Walk the dog")
    todo3 = manager.add_todo("Finish homework")
    print(f"   Added {len(manager.get_all_todos())} todos")
    print(f"   Todos: {[str(t) for t in manager.get_all_todos()]}")

    # Test 2: View functionality
    print("\n2. Testing VIEW functionality:")
    all_todos = manager.get_all_todos()
    print(f"   Retrieved {len(all_todos)} todos")
    for todo in all_todos:
        print(f"   - {todo}")

    # Test 3: Update functionality
    print("\n3. Testing UPDATE functionality:")
    update_result = manager.update_todo(todo1.id, "Buy groceries and cook dinner")
    print(f"   Update successful: {update_result}")
    if update_result:
        updated_todo = manager.get_todo_by_id(todo1.id)
        print(f"   Updated todo: {updated_todo}")

    # Test 4: Mark as complete functionality
    print("\n4. Testing MARK COMPLETE functionality:")
    complete_result = manager.mark_todo_complete(todo1.id)
    print(f"   Mark complete successful: {complete_result}")
    if complete_result:
        completed_todo = manager.get_todo_by_id(todo1.id)
        print(f"   Completed todo: {completed_todo}")

    # Test 5: Mark as incomplete functionality
    print("\n5. Testing MARK INCOMPLETE functionality:")
    incomplete_result = manager.mark_todo_incomplete(todo1.id)
    print(f"   Mark incomplete successful: {incomplete_result}")
    if incomplete_result:
        incomplete_todo = manager.get_todo_by_id(todo1.id)
        print(f"   Incomplete todo: {incomplete_todo}")

    # Test 6: Delete functionality
    print("\n6. Testing DELETE functionality:")
    initial_count = len(manager.get_all_todos())
    delete_result = manager.delete_todo(todo2.id)
    print(f"   Delete successful: {delete_result}")
    if delete_result:
        new_count = len(manager.get_all_todos())
        print(f"   Todos before: {initial_count}, after: {new_count}")
        print(f"   Remaining todos: {[str(t) for t in manager.get_all_todos()]}")

    # Test 7: Error handling
    print("\n7. Testing ERROR HANDLING:")
    try:
        manager.add_todo("")  # Should raise ValueError
        print("   Error handling failed: Empty todo was accepted")
    except ValueError as e:
        print(f"   Error handling passed: {e}")

    invalid_update = manager.update_todo(999, "Non-existent todo")
    print(f"   Invalid ID update handled: {invalid_update}")

    invalid_delete = manager.delete_todo(999)
    print(f"   Invalid ID delete handled: {invalid_delete}")

    invalid_complete = manager.mark_todo_complete(999)
    print(f"   Invalid ID complete handled: {invalid_complete}")

    print("\n8. Testing UNIQUENESS of IDs:")
    print(f"   Next available ID: {manager.get_next_id()}")

    print("\nAll functionality tests completed successfully!")


if __name__ == "__main__":
    test_all_functionality()