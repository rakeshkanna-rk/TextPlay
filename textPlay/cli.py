import webbrowser
import sys
import pyfiglet
import time
from textPlay.colors import *
from textPlay.options import options
from textPlay.Gsearch import g_search
from textPlay.password_generator import create_password
from textPlay.encrypt_animation import encrypted
from textPlay.morse import Morse
from textPlay.files import *

VERSION = '0.1.4'
TITLE = f"{YELLOW}\n{pyfiglet.figlet_format("textPlay")}"
breaker = '\n----------------'
contact = f'''
Github : {CYAN}https://github.com/rakeshkanna-rk{RESET}
Mail : {CYAN}rakeshkanna0108@gmail.com{RESET}
'''
fle_opr = '''
1. Create Folder
2. Create File
3. Delete Folder
4. Delete File
5. Rename Folder
6. Move Folder
7. List Folder
8. Write File
9. Read File
'''
help_cli = '''Usage: MonoCipher <option>

Options:
 -h, --help          show this help message and exit
 -v, --version       show the version number and exit
 -m, --menu          Open main menu
 -c, --contact       Get author contact
'''

# COLORS
red = RED
green = GREEN
blue = BLUE
yellow = YELLOW
magenta = MAGENTA
cyan = CYAN
reset = RESET
lit_red = LIGHT_RED

def textPlay_cli():
    print(TITLE)
    try:
        if len(sys.argv) > 2:
            print(f"{RED}Invalid Input Provided{RESET}")
            print(help_cli)


        elif sys.argv[1] == '--help' or sys.argv[1] == '-h':
            print(help_cli)

        elif sys.argv[1] == '--menu' or sys.argv[1] == '-m':
            print(f"{GREEN} Openig Menu...{RESET}")
            time.sleep(2)
            menu()

        elif sys.argv[1] == '--version' or sys.argv[1] == '-v':
            print(f"{YELLOW}TextPlay {MAGENTA}{VERSION}{RESET}")

        elif sys.argv[1] == '--contact' or sys.argv[1] == '-c':
            print(contact)

        else:
            print(f"{RED}Invalid Input Provided{RESET}")
            print(help_cli)
            

    except IndexError :
        menu()


# MENU
def menu():
    options([(f'Web Search {RESET}', lambda: search()),
             (f'Morse Code/Decode {RESET}', lambda: morse()),
             (f'File Operations {RESET}', lambda: files()),
             (f'Password Generator {RESET}', lambda: pws_gen()),
             (f'Colors {RESET}{breaker}', lambda: colors_set()),
             (f'Text Play Tools {RESET}', lambda: tp_tools()),
             (f'Source Code {RESET}\n\n', lambda: source_code())],
             index=f"{magenta}>",
             head = "\n\tTextPlay CLI\n")


def colors_set():
    print(ALL_COLORS)

# PASSWORD GENERATOR
def pws_gen():
    psw = create_password()
    encrypted(psw, end_color=GREEN)


# FILES
def files():
    print(fle_opr)
    crt_loc = os.getcwd()
    print(f"Current Location: {YELLOW}{crt_loc}{RESET}")
    try:
        loop = True
        while loop:
            opr = int(input(f"{BLUE}What type of opration you need to do: {RESET}"))
            if opr == 1:
                file = ask()
                crt_dir(file)
                print(f"{GREEN}Folder created successfully!{RESET}")
            elif opr == 2:
                file = ask()
                write_file(file, tell_me=False)
                print(f"{GREEN}File created successfully!{RESET}")
            elif opr == 3:
                file = ask()
                del_folder(file)
                print(f"{GREEN}Folder deleted successfully!{RESET}")
            elif opr == 4:
                file = ask()
                del_file(file)
                print(f"{GREEN}File deleted successfully!{RESET}")
            elif opr == 5:
                old = ask(f"{BLUE}Enter folder name to rename: {RESET}")
                new = ask(f"{BLUE}Enter new folder name: {RESET}")
                rename_folder(old, new)
                print(f"{GREEN}Folder renamed successfully!{RESET}")
            elif opr == 6:
                old = ask(f"{BLUE}Enter folder name to move: {RESET}")
                new = ask(f"{BLUE}Enter location where you want to move: {RESET}")
                move_folder(old, new)
                print(f"{GREEN}Folder moved successfully!{RESET}")
            elif opr == 7:
                file = ask()
                lst_dir = list_dir(file)
                print(lst_dir)
            elif opr == 8:
                file = ask()
                content = input(f"Enter content: ")
                write_file(file, content, tell_me=False)
                print(f"{GREEN}File written successfully!{RESET}")
            elif opr == 9:
                file = ask()
                re_file = read_file(file)
                print(re_file)
            else:
                loop = False
            loop = False

    except Exception:
        print(f"{RED}Invalid Input Provided{RESET}")
        files()
        

def ask(text=f"{BLUE}Enter a folder name or location: {RESET}"):
    loop = True
    while loop:
        file = input(text)
        if file == "":
            print(f"{RED}Folder name can't be empty!{RESET}")
        else:
            loop = False
    return file

# SEARCH
def search():
    srch = input(f"Search: ")
    if srch == "":
        print(f"Search can't be empty!{RESET}")
        search()
    else:
        pass
    
    result = input(f"Number of results[1]: ")
    if result == "":
        result = 1
    else:
        pass
    
    print(f"Searching for: {srch}")
    print(f"Search results ↓\n{g_search(srch, int(result))}")

# MORSE
def morse():
    input_text = input("Enter text/Morse code: ")
    if input_text == "":
        print(f"{RED}Text can't be empty!{RESET}")
        morse()
    else:
        pass

    print("Received input:", input_text)  # Debug statement to verify input
    
    morse_instance = Morse()
    
    if "/" in input_text:
        decoded_text = morse_instance.decoder(input_text)
        print(f"Decoded Text: {decoded_text}")
    else:
        encoded_text = morse_instance.coder(input_text)
        print(f"Encoded Morse Code: {encoded_text + ' /'}")
        
def tp_tools():
    tools = f"""
\t{LIGHT_YELLOW}Text Play Tools{RESET}

{BOLD}• Web Search {RESET}
    This tool will search Google for a query and display the results.
    you can specify the number of results to display.

{BOLD}• Morse Code/Decode {RESET}
    This tool will convert text to morse code and vice versa.
    It will automatically detect if the input is morse code or text.

{BOLD}• Box {RESET}
    This tool will print a box with a message and a title with specified length.

{BOLD}• Colors {RESET}
    This tool will print text with different colors and styles.

{BOLD}• Options {RESET}
    This tool will display a menu with options and handle user input for navigation and selection.

{BOLD}• Password Generator {RESET}
    This tool will generate a random password with the specified length.

{BOLD}• Progress Bar {RESET}
    This tool will display a progress bar with a specified terminal length.

{BOLD}• Encryption Animation {RESET}
    This tool will display an encryption animation in the terminal with a specified word.

{BOLD}• Files {RESET}
    This tool will handle file creation, deletion, read, write and more.
    
{BOLD}• Source Code {RESET}
    View our source code at github. {BRIGHT_BLUE}https://github.com/rakeshkanna-rk/textPlay{RESET}
    Author: {MAGENTA}Rakesh Kanna S{reset}
"""

    print(tools)


def source_code():
    print(f"Source code at: {BRIGHT_BLUE}https://github.com/rakeshkanna-rk/textPlay{RESET}")
    webbrowser.open('https://github.com/rakeshkanna-rk/textPlay')
    print(f"Auto opening browser...{GREEN} ✔{RESET}")
