import os


def main():
    cwd = os.getcwd()
    print('os.getcwd(): {}'.format(cwd))
    print('Exists? {}'.format(os.path.exists(cwd)))
    bezier_dir = os.path.join(cwd, 'bezier')
    print('./bezier: {}'.format(bezier_dir))
    print('Exists? {}'.format(os.path.exists(bezier_dir)))


if __name__ == '__main__':
    main()
