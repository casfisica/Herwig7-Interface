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
<par>For testing of the recently build interface you can run one of the following cmsRun files available in the GeneratorInterface/Herwig7Interface/test directory:</par>


<!--li is listing-->

<li><i>Herwig7Test_ConfigFile_GEN_SIM.py</i>: Uses Herwig7 interface to read in an external Herwig7 input file called TestConfig.in. Difference to other cmsRun files is that the Herwig7 config is not provided in the python code but as an external file</li>
  
  
<li>Herwigpp_Herwig7interfaceTestProcess_cff_py_GEN_SIM.py: Uses the .  </li>
  
```bash
  cmsRun Herwigpp_Herwig7interfaceTestProcess_cff_py_GEN_SIM.py
```

<li><b><i>Herwig7_Matchbox_90X_ppToee_GEN_SIM.py</i></b>: Uses the old .</li>

<li>LEP.in: Can be used to invoke Herwig7 standalone as a check via</li>

<li>TestConfig.in: Herwig7 inputfile used as a test config together with the Herwigpp_ConfigFile_cff_py_GEN_SIM.py cmsRun file</li>

