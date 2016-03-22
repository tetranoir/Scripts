"""
Updates ted's grades using vocareum data.

HOW TO USE: Make sure the data is in CSV. For Ted, make sure the column you want to modify is the LAST column. To get the Ted scores, go to "full grade center". Click work offline, choose delimiter type: comma, and download everything. To get the Vocareum scores, from the assignment's grades list click Export and then Grades. Select "show email" and "show name" but NOT "rubric elements".

arno gau
3/21/2016
"""

import sys
import operator

ted_col = -1

def main():
    if len(sys.argv) == 3:
        voc_fname = sys.argv[1]
        ted_fname = sys.argv[2]
    else:
        voc_fname = input('vocareum file:')
        ted_fname = input('ted file:')
    voc_file = open(voc_fname)
    ted_file = open(ted_fname)

    # VOC
    voc = {}
    voc_file.readline() # header
    for line in voc_file:
        delim = line.split(',')
        userid = delim[0].lower()
        if userid[0] != 'a' and userid[0] != 'u': # if not ('a1234...' or 'u1234...') then its a name
            userid = userid.strip('"').split(' ') # take out middle name
            userid = userid[0] + userid[-1]
        score = delim[-1].strip() # score on last element
        if not score.isdigit(): # scores are  '-----' if nothing was entered
            score = '0'
        voc[userid] = score
    
    # TED
    ted_header = ted_file.readline().strip()
    ted = [ line.strip().split(',') for line in ted_file ]
    ted_updated = [ted_header]
    not_found = [] # people in ted that were not found in voc are stored here
    for line in ted: # all entries from ted are between ""
        userid = line[3].strip('"') # id number
        if userid not in voc: # if id number isnt there, try name
            userid = line[1].strip('"') + line[0].strip('"')
            userid = userid.lower()
        score = voc.get(userid)
        if score == None: # some people from ted arent in vocareum
            score = '0'
            not_found.append(userid)
        else:
            voc[userid] = 'U' # mark scores that were used
        line[ted_col] = '"' + score + '"' # col to change
        line = ','.join(line)
        ted_updated.append(line)

    ted_updated = '\n'.join(ted_updated)

    output = open('ted_updated.csv', 'w')
    output.write(ted_updated)
    
    not_used = [] # list of unused voc scores
    for item in voc.items():
        if item[1] != 'U':
            not_used.append(item)
            
    print("\tUnused scores from Vocareum:")
    print(sorted(not_used, key=operator.itemgetter(1), reverse=True)) # sort by score
    print("\tNames from Ted not found in Vocareum:")
    print(not_found)

if __name__ == "__main__":
    main()