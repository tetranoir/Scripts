import os
if __name__ == '__main__':
    f = os.path.realpath(__file__)
    r = open(f).read()
    open(f,'w').write(r)