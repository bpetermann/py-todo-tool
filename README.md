# py-todo-tool

py-todo-tool is a straightforward command-line todo application that allows you to manage your tasks efficiently. 
You can easily add and organize your todos. All tasks are stored into a .txt file, that get's automatically generated when you first run the programm. Tasks that are one day or more old are automatically deleted

## Getting Started

Follow these steps to get started:

```shell
git clone https://github.com/bpetermann/py-todo-tool.git
cd py-todo-tool
pip install -r requirements.txt
```

## Usage

To start using py-todo-tool, open your terminal and navigate to the project directory. Then, run the following commmand to start the application:

```shell
python main.py
```
### Commands

Explore Available Commands: 

After launching the application, type "h" to view a list of available commands and their descriptions.


- The **"h"** command will help you get familiar with how to interact with the tool.
-  You can add new tasks to your todo list using the **"add"** command. Simply follow the prompts to provide a description and due date for your task.
- Use the **"delete"** command to remove tasks from your todo list. You will be prompted to select the task you want to delete.
- The **"show"** command allows you to view tasks for a specific day. You will be prompted to enter a date, and the tool will display all tasks due on that day.

Automatic Cleanup: py-todo-tool automatically removes old tasks upon program startup, so you don't have to worry about clutter in your todo list.
