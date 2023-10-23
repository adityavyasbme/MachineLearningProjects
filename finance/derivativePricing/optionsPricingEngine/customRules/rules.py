from optionsPricingEngine.customRules.intrinsicRules import rules as irl
from optionsPricingEngine.customRules.timeDecayRules import rules as tdr
from optionsPricingEngine.customRules.deltaRules import rules as dr


rules = irl + tdr + dr
