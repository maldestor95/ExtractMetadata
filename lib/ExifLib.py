import subprocess 
import os.path
import os
import json
import re
import csv

class EXIFEXTRACTOR:
  def __init__(self,Absolute_src_path):
    self.my_path = os.path.abspath(os.path.dirname(__file__))
    self.dirname=Absolute_src_path
    self.data=[]

  def load_dir(self,DIR):
    print(self.dirname)
    self.dirname=DIR
    for f in os.listdir(DIR):
      if re.match('.+.JPG',f):
        # print(os.path.join(self.dirname,f))
        res=self.readexif1file(os.path.join(self.dirname,f))
        self.data.append(res)
    # print(os.listdir(p))


  def readexif1file(self,Absolute_src_path):
  #Read the exifdata of srcpath
  #Return a dict: {srcpath:result}
  ## result.get(k).keys() #liste des tags
  ## result.get(k).get('Xmp.drone-parrot.PhotoMode').get('Value')) #get Value of a specific tag
    my_path = os.path.abspath(os.path.dirname(__file__))
    pathexiv2 = os.path.join(my_path, "bin\\exiv2\\exiv2.exe")
    # print(pathexiv2, Absolute_src_path)
    proc=subprocess.Popen ([pathexiv2,Absolute_src_path, '-pa'],shell=True, stdout=subprocess.PIPE) #sortie en console

    res=proc.stdout.read().decode('utf-8')
    # print("res")
    result={}
    for ligne in res.splitlines():
      # print("R: " ,ligne)
      L=re.sub('( )+',",",ligne).split(',')
      # print(L[0])
      result.update({L[0]:{"Type":L[1],"Size":L[2],"Value":L[3]}})
      # print(o)
      # result.update(o)
    # print(result)
    return {Absolute_src_path:result}


  def GetPictureList(self):
    # return an array of strings as fullpathname

    # print("DATA:" ,type(self.data), "size ", len(self.data)) #array
    # print(len(self.data)) 
    flist=[]
    for PICs in self.data:
      # print("PICs in self.data",next(iter(PICs.keys() ) ) )
      flist.append(next(iter(PICs.keys() ) ))
      # print(fname)
      # f.append(i)
      # if 'C:\\dev\\exifextract\\test\\P7890789.JPG' in PICs:
      #   # d=self.data.get('C:\\dev\\exifextract\\test\\P7890789.JPG'):
      #   # print(d.get('Exif.Image.XResolution').get('Value'))
      #   PIC=PICs.get('C:\\dev\\exifextract\\test\\P7890789.JPG')
      #   print(PIC)
      #   print("\n", PIC.get('Exif.Image.XResolution').get('Value'))
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

	
if __name__=="__main__":
  
  # res=load_directory() #init
  # for i in res:
  # 	print(i.keys()) #file path
  # 	for k in i.keys():
  # 		print (i.get(k).keys()) #liste des tags
  # 		print (i.get(k).get('Xmp.drone-parrot.PhotoMode').get('Value'))
  

  	# print(i.keys(),type(i.keys()))#.values['Exif.GPSInfo.GPSLatitude'])
  	# print(res[0].values())
  # t={src:[1,2,3], 'v':['a',2,3]}
  # print(type(t))
  # print (t['v'])
  # load_d("./test")
  DIR=os.getcwd()
  # print(DIR)
# 'C:\\dev\\exifextract\\test'  
  x=EXIFEXTRACTOR(DIR)
  x.load_dir(DIR)
  # print(x.GetPictureList())
  x.ExportListToCsv('Exif.csv')