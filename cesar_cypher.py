"""
part cipherdecryption
"""
#!/usr/bin/env python2.6
__author__ = ["Alexis Schreiber"]
__credits__ = ["Alexis Schreiber"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = ["Alexis Schreiber"]
__status__ = "Prodcution"



import string
from argparse import ArgumentParser
import sys

TAB_ASCII = list(string.ascii_lowercase)


def swap_letters(sentence, key):
    """
         used to swap letters
    """
    letter = None
    new_test = []
    for letter in sentence.lower():
        if str.isalpha(letter):
            if TAB_ASCII.index(letter)+key > 25:
                letter = TAB_ASCII[TAB_ASCII.index(letter)+key-26]
            else:
                letter = TAB_ASCII[TAB_ASCII.index(letter)+key]
        new_test.append(letter)
    return ''.join(new_test)



def all_keys(cryp_file):
    """
        Trying all the possibility in the lantin alphabet
    """
    try:
        cryp_file = open(cryp_file, "r")
    except (IOError, OSError) as exception:
        print
        print "File access Error :\n%s"  % exception
        raise SystemExit

    for key in range(1, 26):
        print "%%%%%%%%%%%%%%%%%"
        print "try with key : %d" % key
        print "%%%%%%%%%%%%%%%%%"

        cryp_file.seek(0, 0)
        for line in cryp_file:
            print swap_letters(line.lower(), key)
        print
    cryp_file.close()

def one_key(cryp_file, key):
    """
    Try only one possibility to get the clear text
    """
    try:
        cryp_file = open(cryp_file, "r")
    except (IOError, OSError) as exception:
        print
        print "File access Error :\n%s"  % exception
        raise SystemExit
    key = key % 26
    print "%%%%%%%%%%%%%%%%%"
    print "try with key : %d" % key
    print "%%%%%%%%%%%%%%%%%"
    cryp_file.seek(0, 0)
    for line in cryp_file:
        print swap_letters(line.lower(), key)
    cryp_file.close()




def parse_args(args):
    """
    Defined all the arguments to be passed to this program
    """

    usage = "%(prog)s --file/-f file.txt "

    parser = ArgumentParser(usage=usage,
                            epilog="gonna output a clear text of your substition by cesar")

    # Common arguments
    parser.add_argument("--file",
                        "-f",
                        help="[REQUIRED] you should provide a file name",
                        action='store',
                        required=True,
                        type=str)
    parser.add_argument("--all",
                        "-a",
                        help=" try all the possibility ",
                        action="store_true",
                        required=False)
    parser.add_argument("--key",
                        "-k",
                        help="key of the cipher",
                        action='store',
                        required=False,
                        type=str)
    args = parser.parse_args(args)
    return args



def main():
    """
    Main function
    """

    args = parse_args(sys.argv[1:])
    if args.all == True:
        all_keys(args.file)
    elif args.key:
        try:
            key = int(args.key)
            one_key(args.file, int(key))
        except ValueError:
            print 'Please enter an integer'

    else:
        print
        print "[Error] : missing arguments (please choose --all or --key)"
        print "use  --help for more details"



if __name__ == "__main__":
    main()
