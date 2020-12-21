# https://pypi.org/project/pypmml/
from pypmml import Model

# The model is from http://dmg.org/pmml/pmml_examples/KNIME_PMML_4.1_Examples/single_iris_dectree.xml
model = Model.fromFile('pmmlFiles\single_iris_dectree.xml')
result = model.predict({
    "Sepal_Length" : 5.1,
    "Sepal_Width" : 3.5,
    "Petal_Length" : 1.4,
    "Petal_Width" : 0.2
})
print("r1",result)
result = model.predict({'sepal_length': 5.1, 'sepal_width': 3.5, 'petal_length': 1.4, 'petal_width': 0.2})
{'probability_Iris-setosa': 1.0, 'probability_Iris-versicolor': 0.0, 'probability': 1.0, 'predicted_class': 'Iris-setosa', 'probability_Iris-virginica': 0.0, 'node_id': '1'}
print("r2",result)
