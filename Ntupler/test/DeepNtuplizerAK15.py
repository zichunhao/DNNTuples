import FWCore.ParameterSet.Config as cms

# ---------------------------------------------------------
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing('analysis')

options.outputFile = 'output.root'
# options.inputFiles = '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/82A9346F-78D8-AE45-A0A9-F3BC0A33480B.root' ## QCD test
# options.inputFiles = '/store/mc/RunIISummer20UL17MiniAODv2/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/99B7EC88-541E-3143-8892-6DDD179CBC4B.root' ## QCD test 2
# options.inputFiles = '/store/group/cmst3/group/vhcc/sfTuples/BulkGravitonToHHTo4QTau_MX-600to6000_MH-15to250/20UL17MiniAODv2/part2/miniv2_14998562-1403.root' ## H->qq/tautau
# options.inputFiles = '/store/group/cmst3/group/vhcc/sfTuples/BulkGravitonToHHTo4Glu_MX-600to6000_MH-15to250/20UL17MiniAODv2/part3/miniv2_15687298-876.root' ## H->gg
# options.inputFiles = '/store/group/cmst3/group/vhcc/sfTuples/ChargedHiggs_HplusToBC_HminusToBC_HT-600to6000_MH-15to250/20UL17MiniAODv2/miniv2_15164446-2044.root' ## H->bc
# options.inputFiles = '/store/group/cmst3/group/vhcc/sfTuples/ChargedHiggs_HplusToCS_HminusToCS_HT-600to6000_MH-15to250/20UL17MiniAODv2/miniv2_15687299-2655.root' ## H->cs
# options.inputFiles = '/store/group/cmst3/group/vhcc/sfTuples/H1H1_2HDM_H1ToBS_HT-600to6000_MH-15to250/20UL17MiniAODv2/miniv2_15723624-285.root' ## H->bs
# options.inputFiles = '/store/group/cmst3/group/vhcc/sfTuples/BulkGravitonToHHTo4L_MX-600to6000_MH-15to250/20UL17MiniAODv2/part3/miniv2_15744104-989.root' ## H->ll
# options.inputFiles = '/store/group/cmst3/group/vhcc/sfTuples/Spin0ToTT_VariableMass_WhadWhad_MX-600to6000_MH-15to250/20UL17MiniAODv2/miniv2_15094466-3566.root' ## top hadronic
# options.inputFiles = '/store/group/cmst3/group/vhcc/sfTuples/Spin0ToTT_VariableMass_WlepWlep_MX-600to6000_MH-15to250_ext1/20UL17MiniAODv2/miniv2_15094468-7131.root' ## top leptonic
# options.inputFiles = '/store/group/cmst3/group/vhcc/sfTuples/20220523_HWW_JHUVariableWMass/2017/mc/BulkGravitonToHHTo4W_MX-600to6000_MH-15to250_JHUVariableWMass_part2/DNNTuples_PrivateMC/220523_095639/0002/miniv2_2419.root' ## HWW 1
# options.inputFiles = '/store/group/cmst3/group/vhcc/sfTuples/20220523_HWW_JHUVariableWMass/2017/mc/BulkGravitonToHHTo4W_MX-600to6000_MH-15to250_JHUVariableWMass_part2/DNNTuples_PrivateMC/220523_095639/0002/miniv2_2420.root' ## HWW 2
# options.inputFiles = '/store/cmst3/group/vhcc/sfTuples/BulkGravitonToHHTo4W_MX-600to6000_MH-15to250_JHUVariableWMass2DMesh/20UL17MiniAODv2/part2/miniv2_15683018-4322.root' ## HWW 2dmesh
# options.inputFiles = '/store/cmst3/group/vhcc/sfTuples/BulkGravitonToHHTo4Z_MX-600to6000_MH-15to250_JHUVariableZMass/20UL17MiniAODv2/part3/miniv2_15820048-548.root' ## HZZ 1
options.inputFiles = '/store/cmst3/group/vhcc/sfTuples/BulkGravitonToHHTo4Z_MX-600to6000_MH-15to250_JHUVariableZMass/20UL17MiniAODv2/part3/miniv2_15820048-549.root' ## HZZ 2
# options.inputFiles = '/store/cmst3/group/vhcc/sfTuples/BulkGravitonToHHTo4Z_MX-600to6000_MH-15to250_JHUVariableZMass2DMesh/20UL17MiniAODv2/part2/miniv2_15822201-2585.root' ## HZZ 2dmesh
# options.inputFiles = '/store/mc/RunIISummer20UL17MiniAODv2/BulkGravToZZToZhadZhad_narrow_M-1000_TuneCP5_13TeV-madgraph-pythia/MINIAODSIM/106X_mc2017_realistic_v9-v2/110000/DABA0ABE-8F97-9747-9A7A-4E31435442E1.root' ## Zqq inference
# options.inputFiles = '/store/mc/RunIISummer20UL17MiniAODv2/BulkGravToWWToWhadWhad_narrow_M-1000_TuneCP5_13TeV-madgraph-pythia/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/F1F668E3-CB4A-ED4E-9493-3485628D5059.root'  ## Wqq inference

options.maxEvents = -1

options.register('skipEvents', 0, VarParsing.multiplicity.singleton, VarParsing.varType.int, "skip N events")
options.register('inputDataset',
                 '',
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.string,
                 "Input dataset")
options.register('isTrainSample', True, VarParsing.multiplicity.singleton,
                 VarParsing.varType.bool, "if the sample is used for training")

options.parseArguments()

# test command: cmsRun DeepNtuplizerAK8.py maxEvents=100 isTrainSample=1

globalTagMap = {
    'auto': 'auto:phase1_2018_realistic',
    'UL18': '106X_upgrade2018_realistic_v16_L1v1',
    'UL17': '106X_mc2017_realistic_v9',
}

## current workflow: only run interactively
assert options.inputDataset == '' and len(options.inputFiles) == 1, 'Only run interactively with file len=1'
print("Running", options.inputFiles)
era = 'auto'
for k in globalTagMap:
    if k in options.inputDataset:
        era = k
if options.inputDataset == '':
    _inputfile = options.inputFiles[0]
    if '2017/' in _inputfile or 'UL17' in _inputfile:
        era = 'UL17'
    elif '2018/' in _inputfile or 'UL18' in _inputfile:
        era = 'UL18'
print('++era: ', era)
# ---------------------------------------------------------
process = cms.Process("DNNFiller")

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.options = cms.untracked.PSet(
    allowUnscheduled=cms.untracked.bool(True),
    wantSummary=cms.untracked.bool(False)
)

print('Using output file ' + options.outputFile)

process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string(options.outputFile))

process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(options.maxEvents))

process.source = cms.Source('PoolSource',
                            fileNames=cms.untracked.vstring(options.inputFiles),
                            skipEvents=cms.untracked.uint32(options.skipEvents)
                            )
# ---------------------------------------------------------
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.EventContent.EventContent_cff")
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, globalTagMap[era], '')
print('Using global tag', process.GlobalTag.globaltag)
# ---------------------------------------------------------
from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection
from RecoBTag.ONNXRuntime.pfParticleNet_cff import _pfMassDecorrelatedParticleNetJetTagsProbs, _pfMassDecorrelatedParticleNetJetTagsMetaDiscrs
pfMassDecorrelatedParticleNetJetTagsAll = _pfMassDecorrelatedParticleNetJetTagsProbs + _pfMassDecorrelatedParticleNetJetTagsMetaDiscrs

useReclusteredJets = True
jetR = 1.5

# only inference the new taggers when not producing the training sample
doCustomTaggerInference = True if not options.isTrainSample else False

bTagDiscriminators = [
    'pfCombinedInclusiveSecondaryVertexV2BJetTags',
    'pfBoostedDoubleSecondaryVertexAK8BJetTags'
]

btagDiscriminatorsCustom = []
if doCustomTaggerInference:
    from DeepNTuples.Ntupler.jetTools import updateJetCollection # use custom updataJetCollection
    from DeepNTuples.Ntupler.hwwTagger.pfMassDecorrelatedInclParticleTransformerV2_cff import _pfMassDecorrelatedInclParticleTransformerAK15V2JetTagsAllSelected
    btagDiscriminatorsCustom = [] # + _pfMassDecorrelatedInclParticleTransformerAK15V2JetTagsAllSelected


JETCorrLevels = ['L2Relative', 'L3Absolute']

from DeepNTuples.Ntupler.jetToolbox_cff import jetToolbox
jetToolbox(process, 'ak15', 'dummySeq', 'noOutput', PUMethod='Puppi', JETCorrPayload='AK8PFPuppi',
           JETCorrLevels=JETCorrLevels, Cut='pt > 120.0 && abs(rapidity()) < 2.4', runOnMC=True, addNsub=True, maxTau=3,
           addSoftDrop=True, addSoftDropSubjets=True, subJETCorrPayload='AK4PFPuppi', subJETCorrLevels=JETCorrLevels,
           bTagDiscriminators=['None'],
           subjetBTagDiscriminators=['None'])

updateJetCollection(
    process,
    jetSource=cms.InputTag('packedPatJetsAK15PFPuppiSoftDrop'),
    rParam=jetR,
    jetCorrections=('AK8PFPuppi', cms.vstring(['L2Relative', 'L3Absolute']), 'None'),
    btagDiscriminators=bTagDiscriminators + pfMassDecorrelatedParticleNetJetTagsAll + btagDiscriminatorsCustom,
    postfix='AK15WithPuppiDaughters',  # needed to tell the producers that the daughters are puppi-weighted
)
# modify the ParticleNet-MD AK15 model
process.pfParticleNetTagInfosAK15WithPuppiDaughters.jet_radius = 1.5
process.pfMassDecorrelatedParticleNetJetTagsAK15WithPuppiDaughters.preprocess_json = 'DeepNTuples/Ntupler/data/ParticleNet-MD/ak15/V02d/preprocess.json'
process.pfMassDecorrelatedParticleNetJetTagsAK15WithPuppiDaughters.model_path = 'DeepNTuples/Ntupler/data/ParticleNet-MD/ak15/V02d/particle-net.onnx'

srcJets = cms.InputTag('selectedUpdatedPatJetsAK15WithPuppiDaughters')
# ---------------------------------------------------------
from PhysicsTools.PatAlgos.tools.helpers import getPatAlgosToolsTask, addToProcessAndTask
patTask = getPatAlgosToolsTask(process)

from RecoJets.JetProducers.ak8GenJets_cfi import ak8GenJets
from RecoJets.Configuration.GenJetParticles_cff import genParticlesForJetsNoNu
process.ak15GenJetsWithNu = ak8GenJets.clone(
    src='packedGenParticles',
    rParam=cms.double(jetR),
    jetPtMin=100.0
)
process.ak15GenJetsWithNuSoftDrop = process.ak15GenJetsWithNu.clone(
    useSoftDrop=cms.bool(True),
    zcut=cms.double(0.1),
    beta=cms.double(0.0),
    R0=cms.double(jetR),
    useExplicitGhosts=cms.bool(True)
)
# ak15GenJetsNoNu and ak15GenJetsNoNuSoftDrop seems already run in ak15 jet clustering
# use a different name here
process.packedGenParticlesForJetsNoNu = genParticlesForJetsNoNu.clone(
    src='packedGenParticles'
)
process.ak15GenJetsNoNuRerun = process.ak15GenJetsWithNu.clone(
    src='packedGenParticlesForJetsNoNu' # using packedGenParticles with no neutrinos as input
)
process.ak15GenJetsNoNuRerunSoftDrop = process.ak15GenJetsWithNuSoftDrop.clone(
    src='packedGenParticlesForJetsNoNu'
)
process.ak15GenJetsWithNuMatch = cms.EDProducer("GenJetMatcher",  # cut on deltaR; pick best by deltaR
                                                src=srcJets,  # RECO jets (any View<Jet> is ok)
                                                # GEN jets  (must be GenJetCollection)
                                                matched=cms.InputTag("ak15GenJetsWithNu"),
                                                mcPdgId=cms.vint32(),  # n/a
                                                mcStatus=cms.vint32(),  # n/a
                                                checkCharge=cms.bool(False),  # n/a
                                                maxDeltaR=cms.double(jetR),  # Minimum deltaR for the match
                                                # maxDPtRel   = cms.double(3.0),                  # Minimum deltaPt/Pt for the match (not used in GenJetMatcher)
                                                # Forbid two RECO objects to match to the same GEN object
                                                resolveAmbiguities=cms.bool(True),
                                                # False = just match input in order; True = pick lowest deltaR pair first
                                                resolveByMatchQuality=cms.bool(False),
                                                )
process.ak15GenJetsWithNuSoftDropMatch = cms.EDProducer("GenJetMatcher",  # cut on deltaR; pick best by deltaR
                                                        src=srcJets,  # RECO jets (any View<Jet> is ok)
                                                        # GEN jets  (must be GenJetCollection)
                                                        matched=cms.InputTag("ak15GenJetsWithNuSoftDrop"),
                                                        mcPdgId=cms.vint32(),  # n/a
                                                        mcStatus=cms.vint32(),  # n/a
                                                        checkCharge=cms.bool(False),  # n/a
                                                        maxDeltaR=cms.double(jetR),  # Minimum deltaR for the match
                                                        # maxDPtRel   = cms.double(3.0),                  # Minimum deltaPt/Pt for the match (not used in GenJetMatcher)
                                                        # Forbid two RECO objects to match to the same GEN object
                                                        resolveAmbiguities=cms.bool(True),
                                                        # False = just match input in order; True = pick lowest deltaR pair first
                                                        resolveByMatchQuality=cms.bool(False),
                                                        )
process.ak15GenJetsNoNuMatch = process.ak15GenJetsWithNuMatch.clone(matched=cms.InputTag("ak15GenJetsNoNuRerun"))
process.ak15GenJetsNoNuSoftDropMatch = process.ak15GenJetsWithNuSoftDropMatch.clone(matched=cms.InputTag("ak15GenJetsNoNuRerunSoftDrop"))

process.genJetTask = cms.Task(
    process.ak15GenJetsWithNu,
    process.ak15GenJetsWithNuMatch,
    process.ak15GenJetsWithNuSoftDrop,
    process.ak15GenJetsWithNuSoftDropMatch,
    process.packedGenParticlesForJetsNoNu,
    process.ak15GenJetsNoNuRerun,
    process.ak15GenJetsNoNuMatch,
    process.ak15GenJetsNoNuRerunSoftDrop,
    process.ak15GenJetsNoNuSoftDropMatch,
)

# DeepNtuplizer
process.load("DeepNTuples.Ntupler.DeepNtuplizer_cfi")
process.deepntuplizer.jets = srcJets
process.deepntuplizer.useReclusteredJets = useReclusteredJets
process.deepntuplizer.bDiscriminators = bTagDiscriminators + pfMassDecorrelatedParticleNetJetTagsAll + btagDiscriminatorsCustom
process.deepntuplizer.jetR = jetR
process.deepntuplizer.jetPtMin = 150

process.deepntuplizer.genJetsWithNuMatch = 'ak15GenJetsWithNuMatch'
process.deepntuplizer.genJetsWithNuSoftDropMatch = 'ak15GenJetsWithNuSoftDropMatch'
process.deepntuplizer.genJetsNoNuMatch = 'ak15GenJetsNoNuMatch'
process.deepntuplizer.genJetsNoNuSoftDropMatch = 'ak15GenJetsNoNuSoftDropMatch'

# determine sample type with inputFiles name
_inputfile = options.inputFiles[0]
process.deepntuplizer.isQCDSample = '/QCD_' in _inputfile
process.deepntuplizer.isTTBarSample = 'tott' in _inputfile.lower() or 'ttbar' in _inputfile.lower()
process.deepntuplizer.isHVV2DVarMassSample = '2DMesh' in _inputfile
process.deepntuplizer.isPythia = 'pythia' in _inputfile.lower()
process.deepntuplizer.isHerwig = 'herwig' in _inputfile.lower()
# note: MG can be interfaced w/ either pythia or herwig
process.deepntuplizer.isMadGraph = 'madgraph' in _inputfile.lower()

process.deepntuplizer.isTrainSample = options.isTrainSample
#==============================================================================================================================#
process.p = cms.Path(process.deepntuplizer)
process.p.associate(patTask)
process.p.associate(process.genJetTask)