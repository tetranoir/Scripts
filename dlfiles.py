"""
Follows and downloads all links from a website that end with a certain filetype.
Download path must exist. 
Currently, not a great way to log

arno gau
3/21/2016
"""

import urllib.request
import os.path
import shutil
import re

def crawl(src, dest = '', filetypes = [".pdf"], log = True):
  """
  Crawls a website for files of specified filetypes that are hyperlinked to.
  src   - the source url
  dest  - the destination folder
  filetypes - a list of filetypes to look for and download
  log  - log of all the files downloaded, tab separated
  """
  flog_str = ''
  found = False
  
  response  = urllib.request.urlopen(src)
  print('Crawling..')
  reg = '<a href="(.+{})">(.+)</a>' # formatter string for regex string
  #reg = '<a href="(.+{})"><.+title="(.+)"'
  
  for line in response:
    line = line.decode("utf-8")
    for type in filetypes:
      type = re.escape(type)
      match = re.search(reg.format(type), line)
      if match:
        found = True
        break # file cant end in multiple types
    if not match:
      continue
      
    link_name = match.group(2) # name of the text link
    url = match.group(1) # the complete file url
    
    dlfile_name = url.rsplit('/', 1)[-1] # name taken from the url
    file_dest = os.path.join(dest, dlfile_name)
    
    link_log = 'link: ' + link_name
    url_log = 'url: ' + url
    file_log = 'file: ' + file_dest
    status_log = 'Successful'
    
    try:
      if len(url) >= 60:
        print('url: .../' + url[-60:].split('/', 1)[-1])
      else:
        print(url_log)
      url = url.replace(' ', '%20')
      resp = urllib.request.urlopen(url)
      if len(file_dest) >= 60:
        print('file: ...\\' + file_dest[-60:].split('\\', 1)[-1])
      else:
        print(file_log)
      out = open(file_dest, 'wb')
      shutil.copyfileobj(resp, out)
    except OSError as e:
      status_log = 'Failed -- ' + str(e)
      print('Failed, check that destination file exists')
      break
    except Exception as e:
      status_log = 'Failed -- ' + str(e)
      print('Failed')
    finally:
      print('')
      try:
        out.close()
        resp.close()
      except:
        pass
      
    
    flog_str = flog_str + '%s\n%s\n%s\n%s\n\n' % (link_log, url_log, file_log, status_log)
  
  if found == False:
    print('Nothing downloaded')
    flog_str = 'Nothing downloaded\n'
    
  response.close()
  
  if log:
    flog = open(__file__ + '.log', 'w')
    flog.write(flog_str)
    flog.close()
    
  
def main():
  # input('Start')
  # src = input('Website: ')
  src = "http://zeldauniverse.net/media/music/ocarina-of-time-rearranged/"
  # src = 'http://pages.cs.wisc.edu/~remzi/OSTEP/'
  # dest = input('Download folder: ')
  ### MAKE SURE TO CHANGE IT TO r FOR RAW STRING
  dest = r'C:\Users\Tetranoir\Desktop\mus\zelda\OOT'
  crawl(src, dest, ['.mp3'])

  
# Boilerplate #
if __name__ == '__main__':
  main()