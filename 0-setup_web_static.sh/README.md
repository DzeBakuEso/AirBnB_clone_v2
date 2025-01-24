# 0x03. AirBnB Clone - Deploy Static

## DevOps | Python | SysAdmin | Scripting | CI/CD  
**Weight:** 1  
**Start Date:** Jan 21, 2025, 6:00 PM  
**End Date:** Jan 24, 2025, 6:00 PM  
**Checker Release:** Jan 22, 2025, 12:00 PM  
**Auto Review:** At project deadline  

---

## Background Context
This project focuses on deploying your **web_static** work from the AirBnB Clone. You'll use **Fabric**, a Python library and CLI tool for streamlining SSH-based tasks like transferring files, executing commands locally/remotely, and managing deployments. This marks your first deployment project, ensuring your web servers (from **0x0F. Load Balancer**) are fully utilized for real-world scenarios.

---

## Learning Objectives
By completing this project, you will be able to:
- Understand what **Fabric** is and how it simplifies deployments.
- Deploy code to servers efficiently.
- Create and work with `.tgz` archives.
- Execute Fabric commands locally and remotely.
- Transfer files using Fabric.
- Manage **Nginx** configurations, including using `alias`.
- Differentiate between `root` and `alias` in Nginx.

---

## Requirements

### Python Scripts
- **Allowed Editors:** `vi`, `vim`, `emacs`
- **Environment:** Ubuntu 20.04 LTS, Python3 (v3.4.0)
- All scripts must:
  - Start with `#!/usr/bin/python3`.
  - End with a new line.
  - Follow **PEP 8** (v1.7.*).
  - Be executable and their length tested using `wc`.
- **Documentation:** 
  - All functions (inside/outside classes) must have docstrings.
  - Documentation must describe the purpose clearly (e.g., `python3 -c 'print(__import__("module").function.__doc__)'`).

### Bash Scripts
- **Allowed Editors:** `vi`, `vim`, `emacs`
- **Environment:** Ubuntu 20.04 LTS
- All scripts must:
  - Start with `#!/usr/bin/env bash`.
  - End with a new line.
  - Include a second line comment explaining the script’s purpose.
  - Be executable and pass Shellcheck (v0.3.3-1~ubuntu20.04.1) without errors.

---

## Installation: Fabric for Python 3
1. Uninstall existing Fabric:
   ```bash
   pip3 uninstall Fabric
Author:Dzeble kwame
