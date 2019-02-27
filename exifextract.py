import subprocess 
import os.path
import os
import json
import re


class EXIFEXTRACTOR:
  def __init__(self):
    self.my_path = os.path.abspath(os.path.dirname(__file__))
  def p(self):
    print(self.my_path)    

def readexif1file(Absolute_src_path):
#Read the exifdata of srcpath
#Return a dict: {srcpath:result}
## result.get(k).keys() #liste des tags
## result.get(k).get('Xmp.drone-parrot.PhotoMode').get('Value')) #get Value of a specific tag
	my_path = os.path.abspath(os.path.dirname(__file__))
	pathexiv2 = os.path.join(my_path, "bin\\exiv2\\exiv2.exe")
	proc=subprocess.Popen ([pathexiv2,Absolute_src_path, '-pa'],shell=True, stdout=subprocess.PIPE) #sortie en console
	res=proc.stdout.read().decode('utf-8')
	result={}
	for ligne in res.splitlines():
		# print("R: " ,ligne)
		L=re.sub('( )+',",",ligne).split(',')
		result.update({L[0]:{"Type":L[1],"Size":L[2],"Value":L[3]}})
		# print(o)
		# result.update(o)
	return {Absolute_src_path:result}

def load_directory():
  my_path=os.path.abspath(os.path.dirname(__file__))

  res=[]

  src="P7890789.JPG"
  srcpath=os.path.join(my_path, "test\\",src)
  res.append(readexif1file(srcpath))

  src="P7900790.JPG"
  srcpath=os.path.join(my_path, "test\\",src)
  res.append(readexif1file(srcpath))
  return res

def load_d(p):
  for f in os.listdir(p):
    if re.match('.+.JPG',f):
      print(f)
  print(os.listdir(p))


def getTag(name):
	print('tt')
	
if __name__=="__main__":
  res=load_directory() #init
  for i in res:
  	print(i.keys()) #file path
  	for k in i.keys():
  		print (i.get(k).keys()) #liste des tags
  		print (i.get(k).get('Xmp.drone-parrot.PhotoMode').get('Value'))
  	# print(i.keys(),type(i.keys()))#.values['Exif.GPSInfo.GPSLatitude'])
  	# print(res[0].values())
  # t={src:[1,2,3], 'v':['a',2,3]}
  # print(type(t))
  # print (t['v'])
  load_d("./test")
  x=EXIFEXTRACTOR()
  x.p()