def updateSupportedBtagDiscr(supportedBtagInfos, supportedBtagDiscr, supportedMetaDiscr):
    
    ## Update taggers in DeepHWWV1, InclParticleTransformerV1
    from DeepNTuples.Ntupler.hwwTagger.pfMassDecorrelatedDeepHWWV1_cff import _pfMassDecorrelatedDeepHWWV1JetTagsProbs, _pfMassDecorrelatedDeepHWWV1JetTagsMetaDiscrs
    from DeepNTuples.Ntupler.hwwTagger.pfMassDecorrelatedInclParticleTransformerV1_cff import _pfMassDecorrelatedInclParticleTransformerV1JetTagsProbs, _pfMassDecorrelatedInclParticleTransformerV1JetTagsMetaDiscrs
    
    # update supportedBtagDiscr
    supportedBtagInfos.extend(["pfMassDecorrelatedDeepHWWV1TagInfos"])
    supportedBtagInfos.extend(["pfMassDecorrelatedInclParticleTransformerV1TagInfos"])
    for disc in _pfMassDecorrelatedDeepHWWV1JetTagsProbs + _pfMassDecorrelatedDeepHWWV1JetTagsMetaDiscrs:
        supportedBtagDiscr[disc] = [["pfMassDecorrelatedDeepHWWV1TagInfos"]]
    for disc in _pfMassDecorrelatedInclParticleTransformerV1JetTagsProbs + _pfMassDecorrelatedInclParticleTransformerV1JetTagsMetaDiscrs:
        supportedBtagDiscr[disc] = [["pfMassDecorrelatedInclParticleTransformerV1TagInfos"]]
    # update supportedMetaDiscr
    for disc in _pfMassDecorrelatedDeepHWWV1JetTagsMetaDiscrs:
        supportedMetaDiscr[disc] = _pfMassDecorrelatedDeepHWWV1JetTagsProbs
    for disc in _pfMassDecorrelatedInclParticleTransformerV1JetTagsMetaDiscrs:
        supportedMetaDiscr[disc] = _pfMassDecorrelatedInclParticleTransformerV1JetTagsProbs

    return supportedBtagInfos, supportedBtagDiscr, supportedMetaDiscr

## Import TagInfos additional to RecoBTag_cff
from DeepNTuples.Ntupler.hwwTagger.pfMassDecorrelatedDeepHWWV1_cff import *
from DeepNTuples.Ntupler.hwwTagger.pfMassDecorrelatedInclParticleTransformerV1_cff import *