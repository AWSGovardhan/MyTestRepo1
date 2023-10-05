import datapackage
import pandas as pd

data_url = 'https://datahub.io/core/nasdaq-listings/datapackage.json'

# to load Data Package into storage
package = datapackage.Package(data_url)

# to load only tabular data
resources = package.resources

print(type(resources))
print(len(resources))
print(resources[0])
print(type(resources[0]))
# for resource in resources:
#     if resource.tabular:
#         data = pd.read_csv(resource.descriptor['path'])
#         #print (data)
#         print(len(data))

