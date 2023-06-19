import FWCore.ParameterSet.Config as cms

pfMassDecorrelatedInclParticleTransformerV2DiscriminatorsJetTags = cms.EDProducer(
   'BTagProbabilityToDiscriminator',
   discriminators = cms.VPSet(
      cms.PSet(
         name = cms.string('HbbvsQCD'),
         numerator = cms.VInputTag(
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV2JetTags', 'probHbb'),
            ),
         denominator = cms.VInputTag(
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV2JetTags', 'probHbb'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV2JetTags', 'probQCDbb'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV2JetTags', 'probQCDcc'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV2JetTags', 'probQCDb'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV2JetTags', 'probQCDc'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV2JetTags', 'probQCDothers'),
            ),
         ),
      )
   )
