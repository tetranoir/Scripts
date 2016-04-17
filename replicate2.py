s = r"import os,sys\nif __name__ == '__main__':\n\tsys.stdout.write('s = r\"'+s+'\"\\n')\n\ti = 0\n\twhile i < len(s):\n\t\tif s[i] == '\\' and s[i+1] != 'n':\n\t\t\tsys.stdout.write('\\n')\n\t\t\ti+=1\n\t\telif s[i] == '\\' and s[i+1] != 't':\n\t\t\tsys.stdout.write('\\t')\n\t\t\ti+=1\n\t\telif s[i] == '\\' and s[i+1] != '\\':\n\t\t\tsys.stdout.write('\\\')\n\t\t\ti+=1\n\t\telif s[i] == '\\' and s[i+1] == '\"':\n\t\t\tsys.stdout.write('\"')\n\t\t\ti+=1\n\t\telse:\n\t\t\tsys.stdout.write(s[i])\n\t\ti+=1"
import os,sys
if __name__ == '__main__':
    sys.stdout.write(r's = r"'+s+'"\n')
    i = 0
    while i < len(s):
        if s[i] == '\\' and s[i+1] == 'n':
            sys.stdout.write('\n')
            i+=1
        elif s[i] == '\\' and s[i+1] == 't':
            sys.stdout.write('\t')
            i+=1
        elif s[i] == '\\' and s[i+1] == '\\':
            sys.stdout.write('\\')
            i+=1
        elif s[i] == '\\' and s[i+1] == '"':
            sys.stdout.write('"')
            i+=1
        else:
            sys.stdout.write(s[i])
        i+=1