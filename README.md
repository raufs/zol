# *zol (& fai)*

[![Preprint](https://img.shields.io/badge/Preprint-bioRxiv-darkblue?style=flat-square&maxAge=2678400)](https://www.biorxiv.org/content/10.1101/2023.06.07.544063v2)
[![Documentation](https://img.shields.io/badge/Documentation-Wiki-darkgreen?style=flat-square&maxAge=2678400)](https://github.com/Kalan-Lab/zol/wiki)
[![Docker](https://img.shields.io/badge/Docker-DockerHub-darkred?style=flat-square&maxAge=2678400)](https://hub.docker.com/r/raufs/zol)
[![install with bioconda](https://img.shields.io/badge/install%20with-bioconda-brightgreen.svg?style=flat)](http://bioconda.github.io/recipes/zol/README.html) [![Conda](https://img.shields.io/conda/dn/bioconda/zol.svg)](https://anaconda.org/bioconda/zol/files)
[![Anaconda-Server Badge](https://anaconda.org/bioconda/zol/badges/latest_release_date.svg)](https://anaconda.org/bioconda/zol)
[![Anaconda-Server Badge](https://anaconda.org/bioconda/zol/badges/platforms.svg)](https://anaconda.org/bioconda/zol)
[![Anaconda-Server Badge](https://anaconda.org/bioconda/zol/badges/license.svg)](https://anaconda.org/bioconda/zol)

*zol (& fai)* are tools to search for gene clusters (sets of co-located genes - e.g. viruses/phages or biosynthetic gene clusters) in a target set of (meta-)genomes and to subsequently simplify the identification of interesting functional, evolutionary, and conservation patterns through creating detailed and color-formatted XLSX spreadsheets that can summarize information across 100s to 1000s of homologous gene cluster instances where visualization-based approaches might be overwhelming or computationally intensive to render.

1. [Program Descriptions](#program-description)
2. [Installation](#installation)
3. [Overview of Major Results](https://github.com/Kalan-Lab/zol/wiki/0.-overview-of-major-result-files)
4. [Short note on resource requirements](#short-note-on-resource-requirements)
5. [Test Case](#test-case)
6. [Documetation](https://github.com/Kalan-Lab/zol/wiki)
7. [Example Usages](https://github.com/Kalan-Lab/zol/wiki/4.-basic-usage-examples)
8. [Tutorial with Tips and Tricks](https://github.com/Kalan-Lab/zol/wiki/5.-tutorial-%E2%80%90-a-detailed-walkthrough)
9. [Premade Target Genome Databases](https://github.com/Kalan-Lab/zol/wiki/7.-premade-prepTG-dbs)
10. [Dependencies](https://github.com/Kalan-Lab/zol/wiki/6.-dependencies)
11. [Assessing the conservation of a focal sample's BGC-ome, phage-ome, and plasmid-ome using abon, atpoc, and apos](https://github.com/Kalan-Lab/zol/wiki/0.-overview-of-major-result-files#abon-atpoc-and-apos-results)
12. [(***New***) Summary visualization of 1000s of gene clusters using cgc](https://github.com/Kalan-Lab/zol/wiki/5.3-visualization-of-1000s-of-gene-clusters-using-cgc)
13. [(***New***) Assessing support for lateral gene transfer using salt](https://github.com/Kalan-Lab/zol/wiki/5.4-horizontal-or-lateral-transfer-assessment-of-gene-clusters-using-salt)

![image](https://github.com/Kalan-Lab/zol/assets/4260723/23c8eae2-ed2f-4c58-bf69-89506c258d9a)


**Citation:**
```
zol & fai: large-scale targeted detection and evolutionary investigation of gene clusters

R Salamzade, PQ Tran, C Martin, AL Manson, 
MS Gilmore, AM Earl, K Anantharaman, LR Kalan
bioRxiv 2023.06.07.544063; doi: https://doi.org/10.1101/2023.06.07.544063
```

In addition, please cite important [dependency software or databases](https://github.com/Kalan-Lab/zol/wiki/6.-dependencies) for your specific analysis accordingly.

## Program Descriptions:

### Prepare Target Genomes (prepTG)

**`prepTG`** processes and performs gene-calling or gene-mapping on an input set of genomes to ease and optimize downstream searches using fai.

### Find Additional Instances (fai)

**`fai`** is a program to search for additional instances of a gene-cluster or genomic locus in some set of target genomes. Inspired by cblaster, CORASON, ClusterFinder, MultiGeneBlast, etc. It leverages DIAMOND alignment similar to [cblaster](https://github.com/gamcil/cblaster) and runs fairly rapidly (allowing it to scale to thousands of genomes and even work on metagenomic assemblies). fai features some key differentiating options relative to other software: (i) can assess syntenic similarity of candidate homologous gene clusters to the query gene cluster, (ii) can allow for looser criteria thresholds for gene cluster detection in target genomes if multiple neighborhoods are identified as homologous and on scaffold edges (thus improving fragmented gene cluster identification due to assembly issues) - similar to lsaBGC-Expansion, (iii) filter secondary neighborhoods - e.g. homologous gene neighborhoods to the query which meet the criteria but are not the best match.

### Zoom on Locus (zol)

**`zol`** is a program to create table reports showing ortholog group conservation, annotation, and evolutionary stats for any gene-cluster or locus of interest. At it's core it performs ortholog group inference de novo across gene-cluster instances similar to [CORASON](https://github.com/nselem/corason), but uses an InParanoid-like algorithm. Tables are similar but currently more in-depth and feature some different statistics than lsaBGC-PopGene reports. zol produces a basic heatmap, but for visualizations of gene-clusters we recommend other tools such as [clinker](https://github.com/gamcil/clinker), [pyGenomeViz](https://github.com/moshi4/pyGenomeViz), [CORASON](https://github.com/nselem/corason), and [gggenomes](https://github.com/thackl/gggenomes), which we think the in-depth spreadsheet complements nicely. We also provide examples of how zol and skani can be used to select representative gene clusters for such visual investigations. 

Critically, ***with the development of some key options, together, fai and zol enable high-throughput detection of orthologs across multi-species datasets comprising of thousands of genomes.***

## Installation:

#### Bioconda (Recommended):

Note, (for some setups at least) ***it is critical to specify the conda-forge channel before the bioconda channel to properly configure priority and lead to a successful installation.***
 
**Recommended**: For a significantly faster installation process, use `mamba` in place of `conda` in the below commands, by installing `mamba` in your base conda environment.

```bash
# 1. install and activate zol
conda create -n zol_env -c conda-forge -c bioconda zol
conda activate zol_env

# 2. depending on internet speed, this can take 20-30 minutes
# end product will be ~36 GB! You can also run in minimal mode
# (which will only download PGAP HMM models < 5 GB) using -m. 
setup_annotation_dbs.py
```

>Note, when you create a conda environment using `-n`, the environment will typically be stored in your home directory. However, because the databases can be large, you might prefer to instead setup the conda environment somewhere else with more space on your system using `-p`. For instance, `conda create -p /path/to/drive_with_more_space/zol_conda_env/ -c conda-forge -c bioconda zol`. Then, next time around you would simply activate this environment by providing the path to it: `conda activate /path/to/drive_with_more_space/zol_conda_env/`

#### Docker:

___Requires docker to be installed on your system!___

To keep the Docker image size relatively low (currently ~8GB), only the PGAP database is included.

```bash
# get wrapper script from GitHub
wget https://raw.githubusercontent.com/Kalan-Lab/zol/main/docker/run_ZOL.sh

# change permissions to allow execution
chmod a+x ./run_ZOL.sh

# run script
./run_ZOL.sh
```

#### Conda Manual:

```bash
# 1. clone Git repo and change directories into it!
git clone https://github.com/Kalan-Lab/zol
cd zol/

# 2. create conda environment using yaml file and activate it!
conda env create -f zol_env.yml -n zol_env
conda activate zol_env

# 3. complete python installation with the following commands:
python setup.py install
pip install -e .

# 4. depending on internet speed, this can take 20-30 minutes
# end product will be 28 GB! You can also run in minimal mode
# (which will only download PGAP HMM models < 5 GB) using -m.
# within zol Git repo with conda environment activated, run:
setup_annotation_dbs.py
```

## Short Note on Resource Requirements:

Different programs in the zol suite have different resource requirements. Moving forward, the default settings in the `zol` program itself should usually allow for low memory usage and faster runtime. For thousands of gene cluster instances, we recommend to either use the dereplication/reinflation approach (see manuscript for comparison on evolutionary statistics between this approach and a full processing) or using CD-HIT clustering (a greedy incremental clustering approach - which is nicely illustrated/explained on the [MMSeqs2 wiki](https://github.com/soedinglab/MMseqs2/wiki#clustering-modes)) to determine protein clusters/families (not true ortholog groups). Disk space is generally not a huge concern for zol analysis, but if working with thousands of gene clusters things can temporarily get large. 

Available disk space is the primary concern however for `fai` and `prepTG`. This is mostly the case for users interested in the construction and searching of large databases (containing over a thousand genomes). Generally, `prepTG` and `fai` are designed to work on metagenomic as well as genomic datasets and do not have a high memory usage, but genomic files stack up in space and DIAMOND alignment files can quite get large as well.

## Test case:

Following installation, you can run a provided test case focused on a subset of Enterococcal polysaccharide antigen instances in *E. faecalis* and *E. faecium* as such:

#### Bioconda:

```bash
# download test data tar.gz and bash script for running tests
wget https://github.com/Kalan-Lab/zol/raw/main/test_case.tar.gz
wget https://raw.githubusercontent.com/Kalan-Lab/zol/main/run_tests.sh

# run bash-based testing script
bash run_tests.sh
```

#### Docker:

```bash
# download test scripts from (bash script which you can reference for learning how to run zol).
wget https://raw.githubusercontent.com/Kalan-Lab/zol/main/docker/test_docker.sh

# change permissions to allow execution
chmod a+x ./test_docker.sh

# run tests
./test_docker.sh
```

Note, the script `test_docker.sh` must be run in the same folder as run_ZOL.sh!

#### Conda Manual:

Within the zol GitHub repo, run the following:

```bash
bash run_tests.sh
```

## License:

```
BSD 3-Clause License

Copyright (c) 2023, Kalan-Lab
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```
