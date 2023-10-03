#start L1
print('Loading the CLI...', end='\r')
#pylib
import os
import sys
import inspect
import difflib
import traceback
from datetime import datetime
from PrintColor.Print_color import print_Color
#global vars>>>
#CONST SYS
CLI_NAME = '`CHANGE THE NAME`' # your CLI name
CLI_Ver = '0.00' # your CLI ver
Debug_m = False
# ...
#normal global
# ...
#other
# ...
#HF>>>
#Debug
def Debug(ID, DEBUG_IF, SFL: bool = True):
    if Debug_m:
        frame_info = inspect.currentframe()
        location = f'{inspect.stack()[1].filename}:{frame_info.f_back.f_lineno}' if SFL else f'L:{frame_info.f_back.f_lineno}'
        print_Color(f'\n~*--> ~*DEBUG INFO id: ~*[{str(ID)}]~*, Location: ~*[{location}]~*, time: ~*[{datetime.now().strftime("%Y/%m/%d | %H:%M:%S")}]\n~*--> ~*Data: ~*{str(DEBUG_IF)}\n~*--> ~*Data Type: ~*{type(DEBUG_IF)}\n', ['red', 'magenta', 'yellow', 'magenta', 'yellow', 'magenta', 'yellow', 'red', 'magenta', 'yellow', 'red', 'magenta', 'yellow'], advanced_mode=True)
# ... (helper funcs)
#CF>>>
#CI_help
def CI_help(SSUH: bool = True, show_lines: bool = True): #change show_lines and SSUH to change the style
    #main
    if SSUH:
        print_Color(f'{("┌─ " if show_lines else "")}~*Main (you can run them in order for simple usage):', ['cyan'], advanced_mode=True)
        for i, (cmd, desc) in enumerate(cmd_descriptions.items(), start=1):
            if i == len(cmd_descriptions):
                print_Color(f'{("│  └─ " if show_lines else "")}~*{i}. {cmd}: ~*{desc}', ['yellow', 'normal'], advanced_mode=True)
            else:
                print_Color(f'{("│  ├─ " if show_lines else "")}~*{i}. {cmd}: ~*{desc}', ['yellow', 'normal'], advanced_mode=True)
        #other
        print_Color(f'{("└─ " if show_lines else "")}~*Other:', ['cyan'], advanced_mode=True)
        for i, (cmd_other, desc_other) in enumerate(cmd_descriptions_other.items(), start=1):
            if i == len(cmd_descriptions_other):
                print_Color(f'{("   └─ " if show_lines else "")}~*{cmd_other}: ~*{desc_other}', ['yellow', 'normal'], advanced_mode=True)
            else:
                print_Color(f'{("   ├─ " if show_lines else "")}~*{cmd_other}: ~*{desc_other}', ['yellow', 'normal'], advanced_mode=True)
    else:
        print_Color(f'~*commands:', ['cyan'], advanced_mode=True)
        #main
        for i, (cmd, desc) in enumerate(cmd_descriptions.items(), start=1):
            if i == len(cmd_descriptions):
                print_Color(f'{("└─ " if show_lines else "")}~*{cmd}: ~*{desc}', ['yellow', 'normal'], advanced_mode=True)
            else:
                print_Color(f'{("├─ " if show_lines else "")}~*{cmd}: ~*{desc}', ['yellow', 'normal'], advanced_mode=True)
        #others
        for i, (cmd_other, desc_other) in enumerate(cmd_descriptions_other.items(), start=1):
            if i == len(cmd_descriptions_other):
                print_Color(f'{("└─ " if show_lines else "")}~*{cmd_other}: ~*{desc_other}', ['yellow', 'normal'], advanced_mode=True)
            else:
                print_Color(f'{("├─ " if show_lines else "")}~*{cmd_other}: ~*{desc_other}', ['yellow', 'normal'], advanced_mode=True)
# ... (commands funcs)
#CMT>>>
command_tuple = (
    'help', # help
    'exit', # Quit the CLI
    'debug', # debug
    'clear' # Clear the CLI
)
# UTF-8 Box Drawings table:
# '│' (U+2502): Box Drawings Light Vertical
# '┌' (U+250C): Box Drawings Light Down and Right
# '┐' (U+2510): Box Drawings Light Down and Left
# '└' (U+2514): Box Drawings Light Up and Right
# '┘' (U+2518): Box Drawings Light Up and Left
# '├' (U+251C): Box Drawings Light Vertical and Right
# '┤' (U+2524): Box Drawings Light Vertical and Left
# '┬' (U+252C): Box Drawings Light Down and Horizontal
# '┴' (U+2534): Box Drawings Light Up and Horizontal
# '┼' (U+253C): Box Drawings Light Vertical and Horizontal
cmd_descriptions = {
    'help': 'Show the help menu with the list of all available commands'
}
cmd_descriptions_other = {
    'exit': 'Quit the CLI',
    'clear': 'Clear the CLI'
}
#funcs(INTERNAL)>>> (DO NOT CHANGE)
#CLI_IM
def CLI_IM(CLII: bool = True):
    if CLII: print_Color('>>> ', ['green'], print_END='')  
    U_input = input('').lower()
    try:
        str_array = U_input.split()
        if str_array[0] in command_tuple:
            return str_array
        else:
            closest_match = difflib.get_close_matches(str_array[0], command_tuple, n=1)
            if closest_match:
                print_Color(f'~*ERROR: ~*Invalid input. you can use \'~*help~*\', did you mean \'~*{closest_match[0]}~*\'.', ['red', 'yellow', 'green', 'yellow', 'green', 'yellow'], advanced_mode=True)
            else:
                print_Color(f'~*ERROR: ~*Invalid input. you can use \'~*help~*\'.', ['red', 'yellow', 'green', 'yellow'], advanced_mode=True)
            return ['IIE']
    except IndexError:
        return ['IIE']
#IEH
def IEH(id: str = 'Unknown', stop: bool = True, DEV: bool = True):
    print_Color(f'~*ERROR: ~*Internal error info/id:\n~*{id}~*.', ['red', 'yellow', 'bg_red', 'yellow'], advanced_mode=True)   
    if DEV: 
        print_Color('~*Do you want to see the detailed error message? ~*[~*Y~*/~*n~*]: ',
                    ['yellow', 'normal', 'green', 'normal', 'red', 'normal'],
                    advanced_mode = True,
                    print_END='')
        show_detailed_error = input('')
        if show_detailed_error.lower() == 'y':
            print_Color('detailed error message:', ['yellow'])
            traceback.print_exc()
    if stop: sys.exit('SYS EXIT|ERROR: Internal|by Internal Error Handler')
#main
def main():
    #global
    global Debug_m
    #CLI loop
    while True: #WT
        #input manager
        input_array = CLI_IM()
        Debug('Input command', input_array) # Debug example usage
        match input_array[0]: #MI
            case 'help':
                CI_help() 
            case 'IIE':
                pass
            case 'clear':
                os.system('cls' if os.name == 'nt' else 'clear')
                print(CLI_Info)
            case 'debug':
                print('Debug mode is ON...')
                Debug_m = True
            case 'exit':
                raise KeyboardInterrupt
            case _:
                IEH(id = 'F[main],L1[WT],L2[MI],Error[nothing matched]', stop = False, DEV = False)
#start>>>
#clear the 'start L1' prompt
print('                  ', end='\r')
#Start INFO
VER = f'V{CLI_Ver}' + datetime.now().strftime(" CDT(%Y/%m/%d | %H:%M:%S)")
#CLI_Info
CLI_Info = f'{CLI_NAME} Ver: {VER} \nPython Ver: {sys.version} \nType \'help\' for more information.'
print(CLI_Info)
#start main
try:
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        pass
except Exception as e:
    IEH(id=f'F[SYS],RF[main],Error[{e}]', DEV=True)
else:
    print_Color(f'\n~*[{CLI_NAME} CLI] ~*closed.', ['yellow', 'red'], advanced_mode=True)
#end(EOF) 