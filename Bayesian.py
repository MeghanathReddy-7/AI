from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
import pandas as pd

data = pd.DataFrame({
    'Cloudy': [True, True, False, False],
    'Sprinkler': [True, False, True, False]
})

model = BayesianNetwork([('Cloudy', 'Sprinkler')])

model.fit(data, estimator=MaximumLikelihoodEstimator)

inference = VariableElimination(model)

print("Inferencing P(Sprinkler=True | Cloudy=False):")
print(inference.query(variables=['Sprinkler'], evidence={'Cloudy': False}))
