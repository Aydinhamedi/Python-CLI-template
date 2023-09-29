# Usage doc

>  **Warning**\
>  Please note that this code uses my print_color\
>  for more info go to https://github.com/Aydinhamedi/Python-color-print.

## 1. Configuring `CLI.cmd`

Start by setting up the configuration to suit your needs. You can do this by modifying the following lines:

```bat
REM CONF
set CLI_NAME="CHANGE THE NAME" 
set python_min_VER=9
```

For example, if you want the minimum Python version to be 3.6.x and the CLI name to be "Test", you would change the lines to:

```bat
REM CONF
set CLI_NAME=Test
set python_min_VER=6 
```

## 2. Setting up the Requirements File

Next, specify the Python packages your project requires in `Data\requirements.txt`. For example:

```requirements
numpy
keras
Pillow
```

## 3. Customizing `CLI_main.py`

Open `Data\CLI_main.py` to customize the CLI.

### Importing Python Packages

Add any additional Python packages you need at the beginning of the file:

```python
#pylib
import os
import sys
import difflib
import traceback
from datetime import datetime
from PrintColor.Print_color import print_Color
```

> **Warning**\
> Do not remove any of the existing imports.

### Defining Global Variables

Define any global variables you need:

```python
#global vars>>>
#CONST SYS
CLI_NAME = '`CHANGE THE NAME`' # your CLI name
CLI_Ver = '0.00' # your CLI ver
# ...
#normal global
# ...
#other
# ...
```

### Adding Helper Functions

Add any helper functions your CLI requires:

```python
#HF>>>
# ... (helper funcs)
```

### Adding Command Functions

Add functions for any commands your CLI supports:

```python
#CF>>>
# ...
```

> **Note**\
> A help function is included by default.

### Defining Commands

Define the commands your CLI supports:

```python
#CMT>>>
command_tuple = (
    'help', # help
    'exit', # Quit the CLI
    'clear' # Clear the CLI
)
```

And provide descriptions for each command:

```python
cmd_descriptions = {
    'help': 'Show the help menu with the list of all available commands'
}
cmd_descriptions_other = {
    'exit': 'Quit the CLI',
    'clear': 'Clear the CLI'
}
```

### Adding Command Functionality

Finally, add functionality for each command in the main function:

```python
#main
def main():
    #CLI loop
    while True: #WT
        #input manager
        input_array = CLI_IM()
        match input_array[0]: #MI
            case 'help':
                CI_help() 
            case 'IIE':
                pass
            case 'clear':
                os.system('cls' if os.name == 'nt' else 'clear')
                print(CLI_Info)
            case 'exit':
                raise KeyboardInterrupt
            case _:
                IEH(id = 'F[main],L1[WT],L2[MI],Error[nothing matched]', stop = False, DEV = False)
```

This is where you define what happens when each command is entered.
