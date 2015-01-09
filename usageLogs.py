#!/usr/bin/python
import re
# import modules used here -- sys is a very standard one
import os, sys

path = r"C:\Users\you\Documents\Logs\2014_11\\"
outfile = r"C:\Users\you\Documents\Logs\Nov2014.csv"
e = open("usagecatalog.txt", "rU")
projList = e.readlines()
e.close()

def Cat(filename):
  f = open(filename, 'rU')
  for line in f:
    print line
  f.close()
  
def Csv(datlist):
  # Open a file
  print "in Csv"
  fo = open(outfile, "a")
  for dat in datlist:
    fo.write( dat + "\n")
  # Close opend file
  fo.close()

def Counter(filename):
  chops = []
  f = open(filename, 'rU')
  for line in f:
    chop = line.split()
    tmpline = ""
    proj = ""
    sub = ""
    if "index.htm" in line:
      rdate = chop[0] 
      rtime = chop[1]
      ruri = chop[4].lstrip()
      rname = chop[7]
      end = ruri.find("index.htm") - 1
      ruri = ruri[1:end]
      n_search = re.search(r'\\(\w+)', rname)
      if n_search:
        #print "in n search"
        for row in projList:
          row = row[1:-1]
          #ruri is:  _cpb_epss_
          #print "ruri is _" + ruri + "_"
          if  ruri == row:
            #print "It equals! row is: _" + row + "_ ruri is: _" + ruri + "_"
            #ruri = /pe_epss/shaft_alignment
            # or pe_epss/index.htm
            rname = n_search.group(1)
            u_search = re.search(r'(\w+)/(\w+)', ruri)
            if u_search:
              proj = u_search.group(1)
              sub = u_search.group(2)
              newline =  rdate + "," + rtime + "," + ruri + ", " + proj + "," + sub + "," + rname
              chops.append(newline)
            else: 
              #print "only one sub path "  
              w_search = re.search(r'(\w+)', ruri)
              if w_search:
                firstword = w_search.group(1)
                newline = rdate + "," + rtime + "," + ruri + ", " + firstword + "," + sub + "," + rname
                chops.append(newline)
    else:
      # "looking for downloads"
      if ( ".zip" or ".pdf" ) in line:
        print "found attachment "
        rdate = chop[0] 
        rtime = chop[1]
        ruri = chop[4]
        rname = chop[7]
        n_search = re.search(r'\\(\w+)', rname)
        if n_search:
          rname = n_search.group(1)
          u_search = re.search(r'(\w+)/(\w+.\w+)', ruri)  
          if u_search:
            proj = u_search.group(1)
            sub = u_search.group(2)
          newline =  rdate + "," + rtime + "," + ruri + ", " + proj + "," + sub + "," + rname
          chops.append(newline)
  Csv(chops)

def StartDir():
  # Open a file
  fo = open(outfile, "a")
  fo.write( "Date,Time,Uri, proj Title, proj Chapter,Viewer\n")
  fo.close()
  dirs = os.listdir( path )
  # This would print all the files and directories  print "proj list is: " + projList
  for file in dirs:
    Counter( path + file )
	
def main():
  #Cat(sys.argv[1])
  StartDir()

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
    
