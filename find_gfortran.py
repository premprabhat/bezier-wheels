import imp
import os


PATHS = (
    r'C:\MinGW\bin',
    r'C:\mingw-w64\i686-5.3.0-posix-dwarf-rt_v4-rev0',
    r'C:\mingw-w64\i686-6.3.0-posix-dwarf-rt_v5-rev1',
    r'C:\mingw-w64\x86_64-6.3.0-posix-seh-rt_v5-rev1',
)
ENV_VARS = (
    'PATH',
    'PATHEXT',
)


def find_gfortran(root):
    for subdir, _, filenames in os.walk(root):
        for filename in filenames:
            if 'gfortran' in filename.lower():
                yield os.path.join(subdir, filename)


def which_gfortran():
    path_extension = os.environ.get('PATHEXT', '')
    valid_extensions = [
        extension
        for extension in path_extension.split(os.pathsep)
        if extension
    ]

    path = os.environ.get('PATH', '')
    path_directories = path.split(os.pathsep)
    for directory_on_path in path_directories:
        basename = os.path.join(directory_on_path, 'gfortran')
        for extension in valid_extensions:
            potential_match = basename + extension
            if os.access(potential_match, os.X_OK):
                print(potential_match)


def setup_info():
    # Print some information about the Fortran compiler
    setup_filename = os.path.join(
        os.path.dirname(__file__),
        'bezier',
        'setup.py',
    )
    setup_mod = imp.load_source('setup', setup_filename)
    f90_compiler = setup_mod.get_f90_compiler()
    if f90_compiler is None:
        print('f90_compiler = None')
        print('f90_exe      = None')
        print('c_compiler   = None')
    else:
        print('f90_compiler = {}'.format(f90_compiler))
        f90_exe = f90_compiler.compiler_f90[0]
        print('f90_exe      = {}'.format(f90_exe))
        c_compiler = f90_compiler.c_compiler
        print('c_compiler   = {}'.format(c_compiler))


def main():
    for path in PATHS:
        for match in find_gfortran(path):
            print(match)

    for env_var in ENV_VARS:
        value = os.environ.get(env_var)
        if value is None:
            print('{} is unset'.format(env_var))
        else:
            print('{}={}'.format(env_var, value))

    which_gfortran()
    setup_info()


if __name__ == '__main__':
    main()
