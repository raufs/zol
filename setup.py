from setuptools import setup
import os

setup(name='zol',
      version='1.4.12',
      description='',
      url='http://github.com/Kalan-Lab/zol/',
      author='Rauf Salamzade',
      author_email='salamzader@gmail.com',
      license='BSD-3',
      packages=['zol'],
      scripts=['docker/ZOL',
               'bin/zol',
               'bin/fai',
               'bin/prepTG',
               'bin/abon',
               'bin/apos',
               'bin/atpoc',
               'bin/cgc',
               'bin/salt',
               'scripts/genbankToFasta.py',
               'scripts/annotateProtSeqs.py',
               'scripts/selectSpecificGeneClusters.py',
               'scripts/runProdigalAndMakeProperGenbank.py',
               'scripts/listAllGenomesInDirectory.py',
               'scripts/setup_annotation_dbs.py',
               'scripts/processNCBIGenBank.py',
               'scripts/extractBiG-SCAPEclusters.py',
               'zol/orthologs/findOrthologs.py',
               'scripts/convertMiniprotGffToGbkAndProt.py',
               'scripts/cagecatProcess.py',
               'scripts/fastgenomicsNeighborhoodToGenBanks.py'],
      zip_safe=False)

# compile RBH/InParanoid-esque programs written in C++
try:
    os.system("g++ -std=c++11 -o zol/orthologs/runRBH zol/orthologs/runRBH.cpp")
    os.system("g++ -std=c++11 -o zol/orthologs/splitDiamondResults zol/orthologs/splitDiamondResults.cpp")
    os.system("g++ -std=c++11 -o zol/splitDiamondResultsForFai zol/splitDiamondResultsForFai.cpp")
except:
    pass
