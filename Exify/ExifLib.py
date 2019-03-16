# coding: utf-8

import subprocess 
import os.path
import os
import json
import re
import csv
import unittest


class EXIFEXTRACTOR:
  def __init__(self,PATH):
    # self.my_path = os.path.abspath(os.path.dirname(__file__))
    if os.path.isdir(PATH):
      self.dirname=PATH
      self.data=[]
      self.exiv2path=os.path.join(os.path.abspath('.'),"bin\\exiv2\\exiv2.exe")
    else:
      self.dirname=None

  def load_dir(self):
    """
      Read all JPG files and store results in self.data
      if dirname wasn't initiated properly, self.data remains and empty array []
    """
    if self.dirname!=None:
      for f in os.listdir(self.dirname):
        if re.match('.+.JPG',f):
          print(os.path.join(self.dirname,f))
          res=self.readexif1file(os.path.join(self.dirname,f))
          self.data.append(res)


  def readexif1file(self,Absolute_src_path):
    """  
    Read the exifdata of srcpath
    Return a dict: {srcpath:result}
     result.get(k).keys() #liste des tags
     result.get(k).get('Xmp.drone-parrot.PhotoMode').get('Value')) #get Value of a specific tag
    """
    if os.path.isfile(Absolute_src_path) and os.path.splitext(Absolute_src_path)[1]==".JPG":
      print("Processing ", Absolute_src_path)
      proc=subprocess.Popen ([self.exiv2path, '-pa',Absolute_src_path],shell=True, stdout=subprocess.PIPE) #sortie en console
      # proc.wait(timeout=
      res=proc.stdout.read().decode('utf-8')
      result={}
      for ligne in res.splitlines():
        L=re.sub('( )+',",",ligne).split(',')
        result.update({L[0]:{"Type":L[1],"Size":L[2],"Value":L[3]}})
      return {Absolute_src_path:result}
    else:
      return False


  def GetPictureList(self):
    """ return an array of strings as fullpathname
      the array is empty if no directory has been previously read with method load_dir
    """
    flist=[]
    for PICs in self.data:
      flist.append(next(iter(PICs.keys() ) ))
    return flist

  def ExportListToCsv(self,CSVname):
    # filename  ,tag1  ,tag2
    # f1        ,value ,value
    # f2        ,value ,value

    flist=self.GetPictureList()
    print(flist)
    tags= self.data[0].get(flist[0]).keys()

    with open(CSVname, 'w', newline='') as csvfile:  
      spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

      #1st Row
      spamwriter.writerow(["File"]+list(tags))

      #parse all files & fill-in csv
      for D in self.data:
        fname=next(iter(D.keys()))
        fvalue=next(iter(D.values()))
        row=[fname]
        for tag in tags:
          row.append(fvalue.get(tag).get('Value'))
        spamwriter.writerow(row)
    return True
def exportToKML(self,):
  print("exportToKML")
  
if __name__ == '__main__':
    # unittest.main()
  print(os.getcwd())
  # os.chdir('../test')
  # print(os.getcwd())
  # print(os.listdir())
  # x=EXIFEXTRACTOR()
  # x.load_dir()
  # x.ExportListToCsv('Exif.csv')