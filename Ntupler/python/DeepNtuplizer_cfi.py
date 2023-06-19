import FWCore.ParameterSet.Config as cms

deepntuplizer = cms.EDAnalyzer('DeepNtuplizer',
                                pfcands    = cms.InputTag("packedPFCandidates"),
                                vertices   = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                losttracks = cms.InputTag("lostTracks"),
                                puInfo     = cms.InputTag("slimmedAddPileupInfo"),
                                rhoInfo    = cms.InputTag("fixedGridRhoFastjetAll"),
                                jets       = cms.InputTag("slimmedJetsAK8"),
                                useReclusteredJets = cms.bool(False),
                                jetR       = cms.double(0.8),
                                jetType    = cms.string('AK'),
                                SVs        = cms.InputTag("slimmedSecondaryVertices"),
                                genJetsWithNuMatch = cms.InputTag('ak8GenJetsWithNuMatch'),
                                genJetsWithNuSoftDropMatch = cms.InputTag('ak8GenJetsWithNuSoftDropMatch'),
                                genJetsNoNuMatch = cms.InputTag('ak8GenJetsNoNuMatch'),
                                genJetsNoNuSoftDropMatch = cms.InputTag('ak8GenJetsNoNuSoftDropMatch'),
                                genParticles = cms.InputTag("prunedGenParticles"),
                                fillMuonVars = cms.untracked.bool(False),
                                muons        = cms.InputTag("slimmedMuons"),
                                fillElectronVars = cms.untracked.bool(False),
                                electrons    = cms.InputTag("slimmedElectrons"),
                                jetPtMin     = cms.untracked.double(200),
                                jetPtMax     = cms.untracked.double(-1),
                                jetAbsEtaMax = cms.untracked.double(2.4),
                                fjTagInfoName = cms.string('pfBoostedDoubleSVAK8'),
                                bDiscriminators = cms.vstring(),
                                METs          = cms.InputTag("slimmedMETs"),
                                addMET        = cms.untracked.bool(False),
                                isQCDSample   = cms.untracked.bool(False),
                                isTTBarSample = cms.untracked.bool(False),
                                isHVV2DVarMassSample = cms.untracked.bool(False),
                                isPythia      = cms.bool(False),
                                isHerwig      = cms.bool(False),
                                isMadGraph    = cms.bool(False),
                                isTrainSample = cms.untracked.bool(True),
                                isMDTagger    = cms.untracked.bool(True),
                                fillSeparateLabels = cms.untracked.bool(False),
                                )
