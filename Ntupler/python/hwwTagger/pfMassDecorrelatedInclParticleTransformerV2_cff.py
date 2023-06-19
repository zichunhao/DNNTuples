import FWCore.ParameterSet.Config as cms

# use ParticleTransformerV2JetTagInfosProducer (include lost track and pixel inputs)
from DeepNTuples.Ntupler.pfParticleTransformerV2JetTagInfos_cfi import pfParticleTransformerV2JetTagInfos
from RecoBTag.ONNXRuntime.boostedJetONNXJetTagsProducer_cfi import boostedJetONNXJetTagsProducer
from DeepNTuples.Ntupler.hwwTagger.pfMassDecorrelatedInclParticleTransformerV2DiscriminatorsJetTags_cfi import pfMassDecorrelatedInclParticleTransformerV2DiscriminatorsJetTags

pfMassDecorrelatedInclParticleTransformerV2TagInfos = pfParticleTransformerV2JetTagInfos.clone(
    use_puppiP4 = False
)

pfMassDecorrelatedInclParticleTransformerV2JetTags = boostedJetONNXJetTagsProducer.clone(
    src = 'pfMassDecorrelatedInclParticleTransformerV2TagInfos',
    preprocess_json = 'DeepNTuples/Ntupler/data/InclParticleTransformer-MD/ak8/V02-N/preprocess_corr.json',
    model_path = 'DeepNTuples/Ntupler/data/InclParticleTransformer-MD/ak8/V02-N/model.onnx',
    flav_names = [
        'probTopbWcs', 'probTopbWqq', 'probTopbWc', 'probTopbWs', 'probTopbWq', 'probTopbWev', 'probTopbWmv', 'probTopbWtauev', 'probTopbWtaumv', 'probTopbWtauhv', 
        'probTopWcs', 'probTopWqq', 'probTopWev', 'probTopWmv', 'probTopWtauev', 'probTopWtaumv', 'probTopWtauhv', 
        'probHbb', 'probHcc', 'probHss', 'probHqq', 'probHbc', 'probHbs', 'probHcs', 'probHgg', 'probHee', 'probHmm', 'probHtauhtaue', 'probHtauhtaum', 'probHtauhtauh', 
        'probHWWcscs', 'probHWWcsqq', 'probHWWqqqq', 'probHWWcsc', 'probHWWcss', 'probHWWcsq', 'probHWWqqc', 'probHWWqqs', 'probHWWqqq', 
        'probHWWcsev', 'probHWWqqev', 'probHWWcsmv', 'probHWWqqmv', 'probHWWcstauev', 'probHWWqqtauev', 'probHWWcstaumv', 'probHWWqqtaumv', 'probHWWcstauhv', 'probHWWqqtauhv', 
        'probHWxWxcscs', 'probHWxWxcsqq', 'probHWxWxqqqq', 'probHWxWxcsc', 'probHWxWxcss', 'probHWxWxcsq', 'probHWxWxqqc', 'probHWxWxqqs', 'probHWxWxqqq', 
        'probHWxWxcsev', 'probHWxWxqqev', 'probHWxWxcsmv', 'probHWxWxqqmv', 'probHWxWxcstauev', 'probHWxWxqqtauev', 'probHWxWxcstaumv', 'probHWxWxqqtaumv', 'probHWxWxcstauhv', 'probHWxWxqqtauhv', 
        'probHWxWxStarcscs', 'probHWxWxStarcsqq', 'probHWxWxStarqqqq', 'probHWxWxStarcsc', 'probHWxWxStarcss', 'probHWxWxStarcsq', 'probHWxWxStarqqc', 'probHWxWxStarqqs', 'probHWxWxStarqqq', 
        'probHWxWxStarcsev', 'probHWxWxStarqqev', 'probHWxWxStarcsmv', 'probHWxWxStarqqmv', 'probHWxWxStarcstauev', 'probHWxWxStarqqtauev', 'probHWxWxStarcstaumv', 'probHWxWxStarqqtaumv', 'probHWxWxStarcstauhv', 'probHWxWxStarqqtauhv', 
        'probHZZbbbb', 'probHZZbbcc', 'probHZZbbss', 'probHZZbbqq', 'probHZZcccc', 'probHZZccss', 'probHZZccqq', 'probHZZssss', 'probHZZssqq', 'probHZZqqqq', 'probHZZbbb', 'probHZZbbc', 'probHZZbbs', 'probHZZbbq', 'probHZZccb', 'probHZZccc', 'probHZZccs', 'probHZZccq', 'probHZZssb', 'probHZZssc', 'probHZZsss', 'probHZZssq', 'probHZZqqb', 'probHZZqqc', 'probHZZqqs', 'probHZZqqq', 
        'probHZZbbee', 'probHZZbbmm', 'probHZZbbe', 'probHZZbbm', 'probHZZbee', 'probHZZbmm', 'probHZZbbtauhtaue', 'probHZZbbtauhtaum', 'probHZZbbtauhtauh', 'probHZZbtauhtaue', 'probHZZbtauhtaum', 'probHZZbtauhtauh', 'probHZZccee', 'probHZZccmm', 'probHZZcce', 'probHZZccm', 'probHZZcee', 'probHZZcmm', 'probHZZcctauhtaue', 'probHZZcctauhtaum', 'probHZZcctauhtauh', 'probHZZctauhtaue', 'probHZZctauhtaum', 'probHZZctauhtauh', 'probHZZssee', 'probHZZssmm', 'probHZZsse', 'probHZZssm', 'probHZZsee', 'probHZZsmm', 'probHZZsstauhtaue', 'probHZZsstauhtaum', 'probHZZsstauhtauh', 'probHZZstauhtaue', 'probHZZstauhtaum', 'probHZZstauhtauh', 'probHZZqqee', 'probHZZqqmm', 'probHZZqqe', 'probHZZqqm', 'probHZZqee', 'probHZZqmm', 'probHZZqqtauhtaue', 'probHZZqqtauhtaum', 'probHZZqqtauhtauh', 'probHZZqtauhtaue', 'probHZZqtauhtaum', 'probHZZqtauhtauh', 
        'probHZxZxbbbb', 'probHZxZxbbcc', 'probHZxZxbbss', 'probHZxZxbbqq', 'probHZxZxcccc', 'probHZxZxccss', 'probHZxZxccqq', 'probHZxZxssss', 'probHZxZxssqq', 'probHZxZxqqqq', 'probHZxZxbbb', 'probHZxZxbbc', 'probHZxZxbbs', 'probHZxZxbbq', 'probHZxZxccb', 'probHZxZxccc', 'probHZxZxccs', 'probHZxZxccq', 'probHZxZxssb', 'probHZxZxssc', 'probHZxZxsss', 'probHZxZxssq', 'probHZxZxqqb', 'probHZxZxqqc', 'probHZxZxqqs', 'probHZxZxqqq', 
        'probHZxZxbbee', 'probHZxZxbbmm', 'probHZxZxbbe', 'probHZxZxbbm', 'probHZxZxbee', 'probHZxZxbmm', 'probHZxZxbbtauhtaue', 'probHZxZxbbtauhtaum', 'probHZxZxbbtauhtauh', 'probHZxZxbtauhtaue', 'probHZxZxbtauhtaum', 'probHZxZxbtauhtauh', 'probHZxZxccee', 'probHZxZxccmm', 'probHZxZxcce', 'probHZxZxccm', 'probHZxZxcee', 'probHZxZxcmm', 'probHZxZxcctauhtaue', 'probHZxZxcctauhtaum', 'probHZxZxcctauhtauh', 'probHZxZxctauhtaue', 'probHZxZxctauhtaum', 'probHZxZxctauhtauh', 'probHZxZxssee', 'probHZxZxssmm', 'probHZxZxsse', 'probHZxZxssm', 'probHZxZxsee', 'probHZxZxsmm', 'probHZxZxsstauhtaue', 'probHZxZxsstauhtaum', 'probHZxZxsstauhtauh', 'probHZxZxstauhtaue', 'probHZxZxstauhtaum', 'probHZxZxstauhtauh', 'probHZxZxqqee', 'probHZxZxqqmm', 'probHZxZxqqe', 'probHZxZxqqm', 'probHZxZxqee', 'probHZxZxqmm', 'probHZxZxqqtauhtaue', 'probHZxZxqqtauhtaum', 'probHZxZxqqtauhtauh', 'probHZxZxqtauhtaue', 'probHZxZxqtauhtaum', 'probHZxZxqtauhtauh', 
        'probHZxZxStarbbbb', 'probHZxZxStarbbcc', 'probHZxZxStarbbss', 'probHZxZxStarbbqq', 'probHZxZxStarcccc', 'probHZxZxStarccss', 'probHZxZxStarccqq', 'probHZxZxStarssss', 'probHZxZxStarssqq', 'probHZxZxStarqqqq', 'probHZxZxStarbbb', 'probHZxZxStarbbc', 'probHZxZxStarbbs', 'probHZxZxStarbbq', 'probHZxZxStarccb', 'probHZxZxStarccc', 'probHZxZxStarccs', 'probHZxZxStarccq', 'probHZxZxStarssb', 'probHZxZxStarssc', 'probHZxZxStarsss', 'probHZxZxStarssq', 'probHZxZxStarqqb', 'probHZxZxStarqqc', 'probHZxZxStarqqs', 'probHZxZxStarqqq', 
        'probHZxZxStarbbee', 'probHZxZxStarbbmm', 'probHZxZxStarbbe', 'probHZxZxStarbbm', 'probHZxZxStarbee', 'probHZxZxStarbmm', 'probHZxZxStarbbtauhtaue', 'probHZxZxStarbbtauhtaum', 'probHZxZxStarbbtauhtauh', 'probHZxZxStarbtauhtaue', 'probHZxZxStarbtauhtaum', 'probHZxZxStarbtauhtauh', 'probHZxZxStarccee', 'probHZxZxStarccmm', 'probHZxZxStarcce', 'probHZxZxStarccm', 'probHZxZxStarcee', 'probHZxZxStarcmm', 'probHZxZxStarcctauhtaue', 'probHZxZxStarcctauhtaum', 'probHZxZxStarcctauhtauh', 'probHZxZxStarctauhtaue', 'probHZxZxStarctauhtaum', 'probHZxZxStarctauhtauh', 'probHZxZxStarssee', 'probHZxZxStarssmm', 'probHZxZxStarsse', 'probHZxZxStarssm', 'probHZxZxStarsee', 'probHZxZxStarsmm', 'probHZxZxStarsstauhtaue', 'probHZxZxStarsstauhtaum', 'probHZxZxStarsstauhtauh', 'probHZxZxStarstauhtaue', 'probHZxZxStarstauhtaum', 'probHZxZxStarstauhtauh', 'probHZxZxStarqqee', 'probHZxZxStarqqmm', 'probHZxZxStarqqe', 'probHZxZxStarqqm', 'probHZxZxStarqee', 'probHZxZxStarqmm', 'probHZxZxStarqqtauhtaue', 'probHZxZxStarqqtauhtaum', 'probHZxZxStarqqtauhtauh', 'probHZxZxStarqtauhtaue', 'probHZxZxStarqtauhtaum', 'probHZxZxStarqtauhtauh', 
        'probQCDbb', 'probQCDcc', 'probQCDb', 'probQCDc', 'probQCDothers', 
        'resonanceMassCorr', 'visiableMassCorr',
    ],
    debugMode = False,
)

# declare all the discriminators
# probs
_pfMassDecorrelatedInclParticleTransformerV2JetTagsProbs = ['pfMassDecorrelatedInclParticleTransformerV2JetTags:' + flav_name
                                 for flav_name in pfMassDecorrelatedInclParticleTransformerV2JetTags.flav_names]
# meta-taggers
_pfMassDecorrelatedInclParticleTransformerV2JetTagsMetaDiscrs = ['pfMassDecorrelatedInclParticleTransformerV2DiscriminatorsJetTags:' + disc.name.value()
                                      for disc in pfMassDecorrelatedInclParticleTransformerV2DiscriminatorsJetTags.discriminators]

_pfMassDecorrelatedInclParticleTransformerV2JetTagsAll = _pfMassDecorrelatedInclParticleTransformerV2JetTagsProbs + _pfMassDecorrelatedInclParticleTransformerV2JetTagsMetaDiscrs