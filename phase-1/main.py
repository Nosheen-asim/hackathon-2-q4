#!/usr/bin/env python3
"""
Console-based Todo Application
A simple in-memory todo application for educational purposes.
"""

from cli_interface import TodoCLI


def main():
    """Main entry point for the todo application."""
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()