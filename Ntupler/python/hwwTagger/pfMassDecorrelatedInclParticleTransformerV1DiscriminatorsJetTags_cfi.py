import FWCore.ParameterSet.Config as cms

pfMassDecorrelatedInclParticleTransformerV1DiscriminatorsJetTags = cms.EDProducer(
   'BTagProbabilityToDiscriminator',
   discriminators = cms.VPSet(
      cms.PSet(
         name = cms.string('HbbvsQCD'),
         numerator = cms.VInputTag(
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probHbb'),
            ),
         denominator = cms.VInputTag(
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probHbb'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probQCDbb'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probQCDcc'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probQCDb'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probQCDc'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probQCDothers'),
            ),
         ),
      cms.PSet(
         name = cms.string('HccvsQCD'),
         numerator = cms.VInputTag(
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probHcc'),
            ),
         denominator = cms.VInputTag(
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probHcc'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probQCDbb'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probQCDcc'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probQCDb'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probQCDc'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probQCDothers'),
            ),
         ),
      cms.PSet(
         name = cms.string('HWW4qvsQCD'),
         numerator = cms.VInputTag(
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probHWqqWqq0c'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probHWqqWqq1c'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probHWqqWqq2c'),
            ),
         denominator = cms.VInputTag(
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probHWqqWqq0c'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probHWqqWqq1c'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probHWqqWqq2c'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probQCDbb'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probQCDcc'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probQCDb'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probQCDc'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probQCDothers'),
            ),
         ),
      cms.PSet(
         name = cms.string('HWW4q3qvsQCD'),
         numerator = cms.VInputTag(
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probHWqqWqq0c'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probHWqqWqq1c'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probHWqqWqq2c'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probHWqqWq0c'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probHWqqWq1c'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probHWqqWq2c'),
            ),
         denominator = cms.VInputTag(
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probHWqqWqq0c'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probHWqqWqq1c'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probHWqqWqq2c'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probHWqqWq0c'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probHWqqWq1c'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probHWqqWq2c'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probQCDbb'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probQCDcc'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probQCDb'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probQCDc'),
            cms.InputTag('pfMassDecorrelatedInclParticleTransformerV1JetTags', 'probQCDothers'),
            ),
         ),
      )
   )
