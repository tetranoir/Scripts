import sys

def entries(m, n):
    ms = len(m) + 1
    ns = len(n) + 1
    e = [ ns * [0] for i in range(ms) ]
    for i in range(ms):
        e[i][0] = i
    for j in range(ns):
        e[0][j] = j
    for i in range(1, ms):
        for j in range(1, ns):
            e[i][j] = min(e[i-1][j] + 1, e[i][j-1] + 1, e[i-1][j-1] + (0 if n[j-1] == m[i-1] else 1))
    return e
    
def edit_letters(m, n, e, i, j, dm = '', dn = ''):
    p = 3*[100]
    if i > 0:
        p[1] = e[i-1][j]
    if j > 0:
        p[2] = e[i][j-1]
    if sum(p) < 200:
        p[0] = e[i-1][j-1]
    if sum(p) == 300:
        return (dm, dn)
    ind = p.index(min(p))
    if ind == 0:
        return edit_letters(m, n, e, i-1, j-1, m[i-1] + dm, n[j-1] + dn)
    if ind == 1:
        return edit_letters(m, n, e, i-1, j, m[i-1] + dm , '_'+dn)
    if ind == 2:
        return edit_letters(m, n, e, i, j-1, '_'+dm, n[j-1] + dn )
    
def edit_dist(e):
    return e[-1][-1]

def main():
    if len(sys.argv) != 3:
        print('nop')
        return
    m = sys.argv[1]
    n = sys.argv[2]
    e = entries(m, n)
    dm, dn = edit_letters(m,n,e, len(m), len(n))
    print("edit distance: %d" % (edit_dist(e)))
    print("edit letters: %s\n              %s" % (dm, dn))
    

# boilerplate #
if __name__ == '__main__':
    main()