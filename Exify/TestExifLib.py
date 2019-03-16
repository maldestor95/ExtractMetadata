import ExifLib 
import unittest
import os

class TestExif(unittest.TestCase):
    def setUp(self)  :
        self.PicPath=os.path.abspath('./test')
        self.x=ExifLib.EXIFEXTRACTOR(self.PicPath)

    def test_Generator(self):
        self.assertEqual(self.x.dirname,self.PicPath, "Folder shall exist")
        W=ExifLib.EXIFEXTRACTOR("WrongPath")
        self.assertEqual(W.dirname,None, "Folder shall not exist")

    def test_read1file(self):
        pic=os.path.join(self.PicPath,'P7890789.JPG')
        Res=self.x.readexif1file(pic)
        self.assertEqual(list(Res.keys())[0], 'C:\\dev\\exifextract\\Exify\\test\\P7890789.JPG', "expect to find picture")
      
        pic1=os.path.join(self.PicPath,'P7890789.TES')
        Res1=self.x.readexif1file(pic1)
        self.assertEqual(Res1, False, "Expected False as file not found")

        pic=self.PicPath
        Res=self.x.readexif1file(pic)
        self.assertEqual(Res, False, "Expected False as a directory is passed")    
    
    def test_readfolder(self):
        # print(self.x.dirname)
        self.x.load_dir()
        self.assertEqual(self.x.GetPictureList()[0],"C:\\dev\\exifextract\\Exify\\test\\P7890789.JPG")

    def test_ExportListToCsv(self):
        f=os.path.abspath('./test/Exif.csv')
        if os.path.isfile(f):
            os.remove(f)
        self.x.load_dir()
        self.x.ExportListToCsv(os.path.abspath('./test/Exif.csv'))
        self.assertEqual(True,True)


if __name__ == '__main__':
    unittest.main()
    
  # os.chdir('../test')
  # print(os.getcwd())
  # print(os.listdir())
  # x=EXIFEXTRACTOR()
  # x.load_dir()
  # x.ExportListToCsv('Exif.csv')