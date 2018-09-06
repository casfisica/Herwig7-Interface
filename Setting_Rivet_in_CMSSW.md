# Setting Rivet in CMSSW

## Installation instructions:

```bash
export SCRAM_ARCH=slc6_amd64_gcc630
cmsrel CMSSW_10_1_1
cd CMSSW_10_1_1/src
cmsenv

git-cms-init
git-cms-addpkg GeneratorInterface/RivetInterface
git-cms-addpkg Configuration/Generator

git clone ssh://git@gitlab.cern.ch:7999/cms-gen/Rivet.git

source Rivet/rivetSetup.sh
scram b -j8

```


```bash



```
## Test :


<par>directory:</par>

<!--li is listing-->

<li><i>Herw</i>: other cmsRun nal file</li>
