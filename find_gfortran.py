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


if __name__ == '__main__':
    main()
