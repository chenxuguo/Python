import argparse
import pprint
from typing import Optional
from typing import Sequence


def positive_int(s: str) -> int:
    try:
        v = int(s)
    except ValueError:
        raise argparse.ArgumentTypeError(f'expected positive integer, got {s!r}')

    if v <= 0:
        raise argparse.ArgumentTypeError(f'expected positive integer, got {v}')
        
    return v
    

def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    
    # parser.add_argument('filename', help='configuration filename %(prog)s')
    
    # parser.add_argument('-c', '--config', '--jsonfile',
                        # default='config.json',
                        # required=True,
                        # help='specify the config file (default: %(default)s)',
                        # )
    # types
    # parser.add_argument(
        # '--days',
        # type=positive_int,
    # )
    # count
    # parser.add_argument('-v', '--verbose', action='count', default=0)
    
    # booleab options
    # parser.add_argument('--force', action='store_true')
    
    # append
    # parser.add_argument('--log', action='append', default=[])
    
    # choice
    # parser.add_argument('--color', choices = ['auto', 'always', 'never'])
    
    # sub-commands
    subparsers = parser.add_subparsers(dest='command')
    subparsers.required  = True
    
    status_parser = subparsers.add_parser('status', help='show status')
    status_parser.add_argument('--force', action='store_true')
    
    checkout_parser = subparsers.add_parser('checkout', help = 'lots of stuff')
    checkout_parser.add_argument('--verbose', action='count')
    
    
    args = parser.parse_args(argv)

    
    pprint.pprint(vars(args))
    return 0
    
if __name__ == '__main__':
    exit(main())