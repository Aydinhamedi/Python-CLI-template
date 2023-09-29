# Python CLI Template
<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/>

This is a Python-based Command Line Interface (CLI) template. It's designed to be interactive and user-friendly, providing a variety of commands for users to interact with the system. You can customize this template to suit your needs by modifying the global variables, helper functions, and command functions.

## Key Features

- **Customizable CLI Name and Version:** You can set the name and version of your CLI by modifying the `CLI_NAME` and `CLI_Ver` global variables.

- **Interactive Command Prompt:** The CLI provides an interactive command prompt where users can enter commands. The prompt is managed by the `CLI_IM` function.

- **Command Handling:** The CLI can handle a variety of commands, which are defined in the `command_tuple` variable. You can add or remove commands from this tuple as needed.

- **Help Menu:** The CLI includes a help menu that lists all available commands. The help menu is displayed by the `CI_help` function.

- **Error Handling:** The CLI includes robust error handling capabilities, managed by the `IEH` function. This function handles internal errors and can display detailed error messages for debugging.

## Customizing the CLI

You can customize this CLI template to suit your needs. Here are some ways you can modify the template:

- **Add New Commands:** To add a new command, add a new entry to the `command_tuple` variable and create a corresponding case in the `main` function.

- **Modify the Help Menu:** To modify the help menu, change the `CI_help` function. You can change the way the help menu is displayed, or the information it includes.

- **Change the CLI Name or Version:** To change the name or version of the CLI, modify the `CLI_NAME` and `CLI_Ver` global variables.

- **Modify Error Handling:** To change the way errors are handled, modify the `IEH` function. You can change the error messages that are displayed, or the way errors are logged.

This CLI template is designed to be flexible and easy to customize, making it a great starting point for any Python-based CLI.
