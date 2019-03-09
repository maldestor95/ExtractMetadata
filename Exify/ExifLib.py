# coding: utf-8

import subprocess 
import os.path
import os
import json
import re
import csv
import unittest

def test():
  print ('lllll')

class EXIFEXTRACTOR:
  def __init__(self):
    self.my_path = os.path.abspath(os.path.dirname(__file__))
    self.dirname=os.getcwd()
    print(self.dirname)
    self.data=[]
    # exiv2path = os.path.abspath(os.path.dirname(__file__))
    self.exiv2path="C:\\dev\\exifextract\\bin\\exiv2\\exiv2.exe"
    print(self.exiv2path)

  def load_dir(self):
    # print(self.dirname)
    # self.dirname=DIR
    for f in os.listdir(self.dirname):
      if re.match('.+.JPG',f):
        print(os.path.join(self.dirname,f))
        res=self.readexif1file(os.path.join(self.dirname,f))
        self.data.append(res)
    # print(os.listdir(p))


  def readexif1file(self,Absolute_src_path):
  #Read the exifdata of srcpath
  #Return a dict: {srcpath:result}
  ## result.get(k).keys() #liste des tags
  ## result.get(k).get('Xmp.drone-parrot.PhotoMode').get('Value')) #get Value of a specific tag
    # my_path = os.path.abspath(os.path.dirname(__file__))
    # pathexiv2 = os.path.join(my_path, "bin\\exiv2\\exiv2.exe")
    proc=subprocess.Popen ([self.exiv2path, '-pa'],shell=True, stdout=subprocess.PIPE) #sortie en console

    res=proc.stdout.read().decode('utf-8')
    result={}
    for ligne in res.splitlines():
      L=re.sub('( )+',",",ligne).split(',')
      result.update({L[0]:{"Type":L[1],"Size":L[2],"Value":L[3]}})
    return {Absolute_src_path:result}


  def GetPictureList(self):
    # return an array of strings as fullpathname
    flist=[]
    for PICs in self.data:
      flist.append(next(iter(PICs.keys() ) ))
    return flist

  def ExportListToCsv(self,CSVname):
    # filename  ,tag1  ,tag2
    # f1        ,value ,value
    # f2        ,value ,value

    flist=self.GetPictureList()
    tags= self.data[0].get(flist[0]).keys()

    with open(self.dirname+'\\'+CSVname, 'w', newline='') as csvfile:  
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


def readexif1file(self,Absolute_src_path):
  #Read the exifdata of srcpath
  #Return a dict: {srcpath:result}
  ## result.get(k).keys() #liste des tags
  ## result.get(k).get('Xmp.drone-parrot.PhotoMode').get('Value')) #get Value of a specific tag
    # my_path = os.path.abspath(os.path.dirname(__file__))
    # pathexiv2 = os.path.join(my_path, "bin\\exiv2\\exiv2.exe")
    print(__file__)
    # proc=subprocess.Popen ([self.exiv2path, '-pa'],shell=True, stdout=subprocess.PIPE) #sortie en console

    # res=proc.stdout.read().decode('utf-8')
    # result={}
    # for ligne in res.splitlines():
    #   L=re.sub('( )+',",",ligne).split(',')
    #   result.update({L[0]:{"Type":L[1],"Size":L[2],"Value":L[3]}})
    # return {Absolute_src_path:result}
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
  # # print(os.getcwd())
  # os.chdir('../test')
  # print(os.getcwd())
  # print(os.listdir())
  # x=EXIFEXTRACTOR()
  # x.load_dir()
  # x.ExportListToCsv('Exif.csv')