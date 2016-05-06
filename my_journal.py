"""
ThoughtBook

Usage:
    journal entry <entry>
    journal search <args>
    journal open <id>
    journal open_all
    journal delete <text>
    journal quit
    journal (-i | --interactive)
    journal (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from functions import JournalEntry


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class Journal (cmd.Cmd):

    def intro():
        print '\t '
        print '\t __ __       __        __       __ __    __   __   __'
        print "\t   |   |__| |  | |  | | __ |__|   |     |__| |  | |  | |_/"
        print "\t   |   |  | |__| |__| |__| |  |   |     |__| |__| |__| | |"
        print '-------------------------------------------------------------------------'
        print '\t\t Hello, Welcome to ThoughtBook'
        print '\t Simple console app to collect your thoughts and events'
        print '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . '
        print '\t\t For any help please print help then enter'
        print '-------------------------------------------------------------------------'

    intro = intro()
    prompt = 'ThoughtBook>> '
    file = None

    @docopt_cmd
    def do_entry(self, arg):
        """
        Usage: entry <entry>...
        """

        return JournalEntry().create_entry(arg)

    @docopt_cmd
    def do_search(self, args):
        """
        Usage: search <arg>...
        """
        search_criteria = args['<arg>']

        if search_criteria[0] == '>' or search_criteria[0] == '<':
            if len(search_criteria) == 3:
                return JournalEntry().search_date(search_criteria)
            elif len(search_criteria) > 3 and search_criteria[3] == 'and':
                return JournalEntry().search_both(search_criteria)
            else:
                print 'Wrong input'

        else:
            print JournalEntry().search_text(search_criteria[0])
            
    def do_open(self, args):
        """
        Usage: open <id>
        """
        args = int(args)

        return JournalEntry().open(args)

    def do_open_all(self, args):
        """
        Usage: open_all
        """
        return JournalEntry().open_all(args)


    def do_delete(self, args):
        """
        Usage: delete <text>
        """

        return JournalEntry().delete(args)

   
    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Till next time, Good Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    Journal().cmdloop()

print(opt)