"""
MCP Tool Registry

Registers and manages all available MCP tools such as add_task, list_tasks,
complete_task, delete_task, and update_task.
"""

class ToolRegistry:
    def __init__(self):
        """Initialize the tool registry with empty tools dictionary"""
        self.tools = {}

    def register_tool(self, name, tool_function):
        """Register a new tool with the registry"""
        self.tools[name] = tool_function

    def get_tool(self, name):
        """Retrieve a registered tool by name"""
        return self.tools.get(name)

    def list_available_tools(self):
        """Return a list of available tool names"""
        return list(self.tools.keys())