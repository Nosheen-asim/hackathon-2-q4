<!--
Sync Impact Report:
Version change: 1.0.0 → 1.1.0
Modified principles: None (new constitution)
Added sections: All principles and governance rules
Removed sections: None
Templates requiring updates: N/A
Follow-up TODOs: None
-->
# Claude Code Agents Constitution

## Core Principles

### I. Spec-Driven Development (SDD)
All development follows the Spec-Driven Development methodology where every feature begins with a clear specification. Specifications must include user stories, acceptance criteria, and test scenarios before any implementation work begins. This ensures alignment between business requirements and technical implementation.

### II. Agent-First Architecture
Every capability should be designed as an autonomous agent that can operate independently. Agents must have well-defined inputs, outputs, and responsibilities. Each agent should be capable of performing its designated function without tight coupling to other components.

### III. Prompt History Records (PHRs) (NON-NEGOTIABLE)
Every user interaction and development decision must be recorded as a Prompt History Record. PHRs must capture the complete user input, system response, and outcomes. This creates an auditable trail of all development activities and enables learning from past decisions.

### IV. Template-Based Standardization
All artifacts must follow established templates to ensure consistency across the codebase. Templates for specs, plans, tasks, and ADRs must be used to maintain uniformity and enable automated processing of development artifacts.

### V. Minimal Viable Changes
All implementations must follow the smallest viable change principle. Only the minimal set of changes required to satisfy the immediate requirement should be implemented. Unrelated refactoring or improvements should be deferred to separate work items.

### VI. Architecture Decision Records (ADRs)
All architecturally significant decisions must be documented as Architecture Decision Records. An ADR is required when the decision has long-term consequences, multiple viable alternatives were considered, or the decision affects cross-cutting system design concerns.

## Additional Constraints

Technology Stack: Python-based agents with Claude Code integration. All agents should follow the patterns established in the .cloud/agents directory structure. Dependencies should be minimal and well-justified.

Security Requirements: All agent implementations must consider security implications. Sensitive data must be handled appropriately, and proper authentication/authorization patterns must be followed when integrating with external services.

## Development Workflow

Code Review Process: All changes must undergo peer review with specific focus on adherence to constitutional principles. Reviewers must verify that PHRs exist for all significant changes and that ADRs were created for architecturally significant decisions.

Quality Gates: Automated checks must verify that all files follow the established patterns and that required documentation artifacts exist. Code coverage and integration tests must pass before merging.

## Governance

This constitution supersedes all other development practices and procedures. All development activities must comply with these principles. Deviations require explicit constitutional amendments with proper justification and approval.

All pull requests and reviews must verify constitutional compliance. Complexity must be justified with clear benefits that outweigh the maintenance overhead. Use this constitution as the definitive guide for development decisions.

**Version**: 1.1.0 | **Ratified**: 2026-02-01 | **Last Amended**: 2026-02-01
