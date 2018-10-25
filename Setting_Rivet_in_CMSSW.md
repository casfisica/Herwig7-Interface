# Setting Rivet in CMSSW

## Installation instructions:

```bash
export SCRAM_ARCH=slc6_amd64_gcc630
cmsrel CMSSW_10_1_1
cd CMSSW_10_1_1/src
cmsenv

git-cms-init
#################################################
#If is inside other CMSSW enviroment start here #
#################################################
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


<par>EWK-10-012, Jet rates in W and Z production (Author: Lovedeep Saini, Anil Singh</par>

```bash
rivet −h
rivet −−list−analyses // List precompiled analyses shipped with Rivet
rivet −−show−analysis CMS 2015 I1310737 // Detailed info for particular analysis
rivet −−show−analysis MC ZJETS MU
rivet −−show−analysis ATLAS 2015 CONF 2015 041

rivet −a ATLAS 2015 CONF 2015 041 −a MC ZJETS MU −H Output.yoda
INPUTFILE

rivet −a CMS 2015 I1310737 −H Output2.yoda −−ignore−beams INPUTFILE

rivet−mkhtml −h
rivet−mkhtml Output.yoda:’LegendLabel’ −−mc−errs

```


