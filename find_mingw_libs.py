import os


PATHS = (
    r'C:\MinGW\bin',
    r'C:\mingw-w64\i686-5.3.0-posix-dwarf-rt_v4-rev0',
    r'C:\mingw-w64\i686-6.3.0-posix-dwarf-rt_v5-rev1',
    r'C:\mingw-w64\x86_64-6.3.0-posix-seh-rt_v5-rev1',
)

def mingw_lib_find(root):
    for subdir, _, filenames in os.walk(root):
        for filename in filenames:
            lower = filename.lower()
            if (lower.endswith('.lib') or
                    lower.endswith('.a') or lower.endswith('.dll')):
                yield os.path.join(subdir, filename)


def main():
    for path in PATHS:
        for match in mingw_lib_find(path):
            print(match)


if __name__ == '__main__':
    main()
