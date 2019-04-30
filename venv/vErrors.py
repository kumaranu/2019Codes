from pathlib import Path
import os

#p = Path('.')
#print (p)
#print (p.absolute())
#print (p.exists())
#print (p.is_file())

#q = p/'aa'
#print(q.absolute())
#print (q.exists())
#os.mkdir(q)
#print (q.exists())

#print ([x for x in p.iterdir() if x.is_dir()])
#print ([x.absolute()  for x in p.iterdir() if x.is_dir()])
#print (list(p.glob('*.py')))
#print (list(p.rglob('*.py'))) #recursive glob

#print (q.exists())

#fp = q/'newfile.txt'
#print (fp.open('wt').write('Hello pyconza!'))

directory_in_str = "~/aa/waterwire/scans/waterwires/diffTempHistogram/logFiles/2/analysisInPython/autosubScanAnalysis/"
p = Path(directory_in_str)
print ("p is",p)

pathlist = list(p.glob('*.txt'))

print ("pathlist is ",list(p.glob("*.txt")))

#for path in pathlist:
#    path_in_str = str(path)
#    print(path_in_str)
