import pprint

import setup


def setup_info():
    # Print some information about the Fortran compiler
    f90_compiler = setup.get_f90_compiler()
    if f90_compiler is None:
        print('f90_compiler = None')
        print('f90_exe      = None')
        print('c_compiler   = None')
    else:
        print('f90_compiler = {}'.format(f90_compiler))
        f90_exe = f90_compiler.compiler_f90[0]
        pprint.pprint(f90_compiler.__dict__)
        print('f90_exe      = {}'.format(f90_exe))
        c_compiler = f90_compiler.c_compiler
        print('c_compiler   = {}'.format(c_compiler))
        pprint.pprint(c_compiler.__dict__)


if __name__ == '__main__':
    setup_info()
