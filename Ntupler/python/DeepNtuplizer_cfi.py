import FWCore.ParameterSet.Config as cms

deepntuplizer = cms.EDAnalyzer('DeepNtuplizer',
                                pfcands    = cms.InputTag("packedPFCandidates"),
                                vertices   = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                puInfo     = cms.InputTag("slimmedAddPileupInfo"),
                                rhoInfo    = cms.InputTag("fixedGridRhoFastjetAll"),
                                jets       = cms.InputTag("slimmedJetsAK8"),
                                useReclusteredJets = cms.bool(False),
                                jetR       = cms.double(0.8),
                                jetType    = cms.string('AK'),
                                SVs        = cms.InputTag("slimmedSecondaryVertices"),
                                genJetsMatch = cms.InputTag('ak8GenJetsWithNuMatch'),
                                genJetsSoftDropMatch = cms.InputTag('ak8GenJetsWithNuSoftDropMatch'),
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
                                isQCDSample   = cms.untracked.bool(False),
                                isTTBarSample = cms.untracked.bool(False),
                                isPythia      = cms.bool(False),
                                isHerwig      = cms.bool(False),
                                isMadGraph    = cms.bool(False),
                                isTrainSample = cms.untracked.bool(True),
                                )
