# Herwig7-Interface

## Installation instructions:
```bash
export SCRAM_ARCH=slc6_amd64_gcc630
cmsrel CMSSW_10_1_1
cd CMSSW_10_1_1/src
cmsenv
git cms-addpkg GeneratorInterface/Herwig7Interface
scram b clean
scram b -j 10
```
## Test of the Herwig7 interface:
<par>Create a new crab task and submit the jobs:  </par>

<marquee>This is basic example of marquee</marquee>
