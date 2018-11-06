# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: GeneratorInterface/Herwig7Interface/python/Herwig7_Dummy_Matchbox_90X_ppToee.py --fileout file:Matchbox_90X_ppToee.root --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions auto:run2_mc --beamspot Realistic25ns13TeVEarly2017Collision --step GEN,SIM --nThreads 1 --geometry DB:Extended --era Run2_2017 --python_filename Herwig7_Matchbox_90X_ppToee_GEN_SIM.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 5
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('SIM',eras.Run2_2017)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeVEarly2017Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(5000)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('GeneratorInterface/Herwig7Interface/python/Herwig7_Dummy_Matchbox_90X_ppToee.py nevts:5'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('file:Matchbox_90X_ppToZJets.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.XMLFromDBSource.label = cms.string("Extended")
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')

process.generator = cms.EDFilter("Herwig7GeneratorFilter",
    Matchbox = cms.vstring('read snippets/PPCollider.in',
        'cd /Herwig/Generators',
        'set EventGenerator:EventHandler:LuminosityFunction:Energy 7000.0',
        'cd /Herwig/MatrixElements/',
        '# Z+jet',
        'insert SubProcess:MatrixElements[0] MEZJet',
        'cd /Herwig/Generators',
        '# analysis of W/Z events',
        'insert EventGenerator:AnalysisHandlers 0 /Herwig/Analysis/DrellYan',
        'saverun LHC EventGenerator'),
    configFiles = cms.vstring(),
    crossSection = cms.untracked.double(-1),
    dataLocation = cms.string('${HERWIGPATH:-6}'),
    dumpConfig = cms.untracked.string('HerwigConfig.in'),
    eventHandlers = cms.string('/Herwig/EventHandlers'),
    filterEfficiency = cms.untracked.double(1.0),
    generatorModule = cms.string('/Herwig/Generators/EventGenerator'),
    hwpp_basicSetup = cms.vstring('#read Matchbox/GenericCollider.in', 
        '#create ThePEG::RandomEngineGlue /Herwig/RandomGlue', 
        '#set /Herwig/Generators/EventGenerator:RandomNumberGenerator /Herwig/RandomGlue', 
        'set /Herwig/Generators/EventGenerator:DebugLevel 2', 
        'set /Herwig/Generators/EventGenerator:PrintEvent 1', 
        'set /Herwig/Generators/EventGenerator:MaxErrors 10000'),
    hwpp_cmsDefaults = cms.vstring('+hwpp_basicSetup', 
        '+hwpp_setParticlesStableForDetector'),
    hwpp_setParticlesStableForDetector = cms.vstring('set /Herwig/Particles/mu-:Stable Stable', 
        'set /Herwig/Particles/mu+:Stable Stable', 
        'set /Herwig/Particles/Sigma-:Stable Stable', 
        'set /Herwig/Particles/Sigmabar+:Stable Stable', 
        'set /Herwig/Particles/Lambda0:Stable Stable', 
        'set /Herwig/Particles/Lambdabar0:Stable Stable', 
        'set /Herwig/Particles/Sigma+:Stable Stable', 
        'set /Herwig/Particles/Sigmabar-:Stable Stable', 
        'set /Herwig/Particles/Xi-:Stable Stable', 
        'set /Herwig/Particles/Xibar+:Stable Stable', 
        'set /Herwig/Particles/Xi0:Stable Stable', 
        'set /Herwig/Particles/Xibar0:Stable Stable', 
        'set /Herwig/Particles/Omega-:Stable Stable', 
        'set /Herwig/Particles/Omegabar+:Stable Stable', 
        'set /Herwig/Particles/pi+:Stable Stable', 
        'set /Herwig/Particles/pi-:Stable Stable', 
        'set /Herwig/Particles/K+:Stable Stable', 
        'set /Herwig/Particles/K-:Stable Stable', 
        'set /Herwig/Particles/K_S0:Stable Stable', 
        'set /Herwig/Particles/K_L0:Stable Stable'),
    parameterSets = cms.vstring('Matchbox', 
        'hwpp_cmsDefaults'),
    repository = cms.string('${HERWIGPATH}/HerwigDefaults.rpo'),
    run = cms.string('InterfaceMatchboxTest')
)


process.ProductionFilterSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# customisation of the process.                                                                                                                                                                            
process.load('GeneratorInterface.RivetInterface.rivetAnalyzer_cfi')

# Automatic addition of the customisation function from Configuration.GenProduction.rivet_customize                                                                                                        
#from Configuration.GenProduction.rivet_customize import customise                                                                                                                                         

def customise(process):
        process.load('GeneratorInterface.RivetInterface.rivetAnalyzer_cfi')
        process.rivetAnalyzer.AnalysisNames = cms.vstring('CMS_2015_I1310737','CMS_2013_I1209721','CMS_2012_I941555', 'CMS_2013_I1224539_ZJET','CMS_2013_I1256943','CMS_2013_I1258128') 
#	process.rivetAnalyzer.CrossSection = cms.double(9757000000)
        process.rivetAnalyzer.OutputFile = cms.string('Z+Jets.yoda')
        process.generation_step+=process.rivetAnalyzer
        process.schedule.remove(process.RAWSIMoutput_step)
        return(process)
#call to customisation function customise imported from Configuration.GenProduction.rivet_customize                                                                                                        
process = customise(process)


# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
