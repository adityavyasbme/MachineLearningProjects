from optionsPricingEngine.customRules.intrinsicRules import rules as irl
from optionsPricingEngine.customRules.timeDecayRules import rules as tdr
from optionsPricingEngine.customRules.deltaRules import rules as dr
from optionsPricingEngine.customRules.gammaRules import rules as gr
from optionsPricingEngine.customRules.vegaRules import rules as vr
from optionsPricingEngine.customRules.rhoRules import rules as rr


rules = irl + tdr + dr + gr + vr + rr
