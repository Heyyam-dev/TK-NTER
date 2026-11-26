# Project Plan

This document outlines the comprehensive project roadmap, including: operational rules for skills and agents, terminal conventions, keyword management and focus discipline, backend development stages, AI model optimization tasks, and Claude Code integration strategy.

## Current Project State

- `readme_reader/`: A command-line tool written in Rust that reads files and displays them with line numbers. Currently has no external dependencies.
- `Qwen-VL-Series-Finetune/`: A Git submodule for Qwen-VL model fine-tuning research and development.

---

## 1. Skills Rules

- **Single purpose**: Each skill performs exactly one task (e.g., "read README", "Qwen fine-tune").
- **Clear naming**: The skill name should indicate when it will be triggered.
- **Recurring tasks**: Cover routine operations such as build, test, deploy, and data preparation.
- **Risky operations**: Deletion, force push, and database changes require explicit user permission.
- **Logging**: Every change (date and content) must be recorded in this file.

## 2. Agents Rules

- **Scope**: Each agent works only within its designated area of responsibility (e.g., backend agents handle server/API code; frontend agents handle UI code).
- **Planning**: Before making significant changes, an agent creates a plan and obtains user approval.
- **Permissions**: Agents do not delete, overwrite data, or commit/push without explicit permission.
- **Reporting**: Upon completion, agents provide a brief summary of changes, affected files, and test results.
- **Coordination**: Only one agent works on a given file at any time.
- **Clarity**: When uncertain, agents ask clarifying questions instead of making assumptions that could cause problems.

## 3. Backend tasks

### Stage 1: Core Setup
- [ ] Define backend project structure (select language and framework)
- [ ] Set up configuration files and environment variables (`.env` template, `.gitignore`)
- [ ] Implement main server startup logic and health-check endpoint

### Stage 2: Data and API
- [ ] Design the data model and database schema
- [ ] Implement CRUD endpoints
- [ ] Add input validation and comprehensive error handling
- [ ] Configure logging

### Stage 3: Security and Quality
- [ ] Implement authentication and authorization mechanisms
- [ ] Write unit and integration tests
- [ ] Create API documentation

### Stage 4: Deployment
- [ ] Configure Docker and build process
- [ ] Set up environment separation (development, staging, production)
- [ ] Implement monitoring and backup strategies

---

## 4. AI (Qwen): Kernel and Micro-Architecture

This section covers kernel-level and micro-architecture optimization work for the Qwen model. Detailed tasks will be refined in subsequent phases.

- [ ] Study the structure and dependencies of the Qwen-VL submodule (`Qwen-VL-Series-Finetune/`)
- [ ] Identify kernel-level components (computation kernels, attention mechanisms, data loading pipelines)
- [ ] Plan micro-architecture modifications (layers, modules, configuration parameters)
- [ ] Establish and document performance baselines

---

## 5. Terminal Rules

- **Working directory**: All terminal commands execute from the project root (`C:\Users\FUJITSU\OneDrive\Desktop\Tk`). Any directory changes must be explicitly noted.
- **Platform and shell**: The platform is Windows with PowerShell as the primary shell. POSIX commands (`grep`, `sed`, `/dev/null`) are used with Bash only when absolutely necessary.
- **File operations**: Use dedicated tools (Read, Grep, Glob, Edit) for file operations instead of terminal commands.
- **Background execution**: Long-running commands (build, test, server) run in the background; results are checked periodically. No indefinite waiting.
- **No interactive mode**: Interactive commands are forbidden (`git rebase -i`, `git add -i`, `Read-Host`, `pause`).
- **Destructive operations**: Commands that modify or delete data (`rm -rf`, `Remove-Item -Recurse`, `git reset --hard`, `git push --force`, `git clean`) require explicit user approval.
- **Error handling**: When commands fail, exit codes and error messages are recorded. Failed commands are not retried without understanding the root cause.
- **Output verbosity**: Terminal output is concise—only key results and errors are shown, not full logs.
- **Sensitive files**: Secret files (`.env`, `credentials.json`, `.claude/settings.local.json`) are never printed or committed.
- **Git workflow**: Commits and pushes require permission. Changes to `main` are made via a new branch first.

## 6. Keyword Rules

- **Assignment**: Every skill and agent has an associated keyword list (e.g., "README", "read", "Qwen", "fine-tune", "build", "test", "deploy").
- **Triggering**: When a user request contains a keyword, the matching skill or agent is automatically activated.
- **Uniqueness**: Each keyword belongs to exactly one skill or agent; no duplication across components.
- **Format**: Keywords are short and specific (1–3 words).
- **Tracking**: All keyword changes are recorded in this file with the date and details.
- **Language**: Description fields are written in English. Keywords may use the user's native language. Code names (`readme_reader`, `Qwen-VL-Series-Finetune`) remain unchanged.

## 7. Focus Rules

- **Single objective**: Each session focuses on one primary goal. Other tasks are recorded as separate items for later work.
- **File exclusivity**: Only one agent modifies a given file at any time.
- **Scope discipline**: Agents work only on files directly related to their current task and avoid unrelated changes.
- **Interruption handling**: When an unrelated request arrives, current work is paused or queued; the user is consulted for priority decisions.
- **Task closure**: Upon completion, the session documents what was done, which files changed, and identifies the next step.
- **Blocking items**: Obstacles and open questions are listed separately to maintain focus on the primary objective.

---

## 8. Claude Code Integration: CLI, IDE, MCP Servers, and Configuration

This section outlines Claude Code integration with the project, including MCP server setup, automation hooks, and system configuration.

### Stage 1: Foundation Setup
- [ ] Install Claude Code CLI and initialize `settings.json`
- [ ] Configure Git integration (commit/PR signatures and attributions)
- [ ] Create configuration files in the `.claude/` directory (settings.json, hooks, approval policies)
- [ ] Verify IDE integration (VS Code, JetBrains, or other supported IDEs)

### Stage 2: MCP Server Integration
- [ ] Identify and select required MCP servers (Calendly, Gmail, Google Drive, Google Docs, etc.)
- [ ] Configure MCP server settings in `settings.json` (authentication, resource paths, endpoints)
- [ ] Integrate MCP tools with project agents (data retrieval, file operations, workflows)
- [ ] Establish permission rules and access control for MCP commands

### Stage 3: Hooks and Automation
- [ ] Configure Git hooks (`pre-commit`, `pre-push`) for validation and formatting
- [ ] Automate terminal command execution (build, test, lint workflows)
- [ ] Set up submit hooks (user prompt triggers for automated workflows)
- [ ] Configure tool call hooks (pre/post-execution actions for specific tools)

### Stage 4: Approvals and Security Policies
- [ ] Create `.claude/approvals.yml` (pull request review policies and automation rules)
- [ ] Set up custom classifiers (risk assessment and code quality evaluation)
- [ ] Define protection rules for sensitive files (`.env`, credentials, private keys)
- [ ] Configure GitHub App permissions and Claude Approvals integration

### Stage 5: Skills and Agents Configuration
- [ ] Develop project-specific skills (backend build, test, Qwen fine-tune, etc.)
- [ ] Define agent types and their areas of responsibility
- [ ] Establish skill keywords and triggering rules
- [ ] Document skills and agents in `.claude/skills.md`

### Stage 6: Monitoring, Logging, and Performance
- [ ] Set up logging and monitoring for Claude Code activity
- [ ] Manage session context (memory management, artifact organization)
- [ ] Track and analyze problematic tool calls
- [ ] Monitor and record performance metrics

---

## Open Questions and Decisions

- **Backend stack**: Which language and framework will be selected for the backend?
- **Tool architecture**: Is `readme_reader` integrated into the backend system, or does it remain a standalone utility?
- **Model serving**: Does Qwen-VL fine-tuning require a dedicated backend service (model API or microservice)?
- **MCP priorities**: Which MCP servers are highest priority for Claude Code integration in this project?
- **Approval policies**: Which rules in the approval policy should be classified as critical or mandatory?
