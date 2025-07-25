// ========== Managed Identity ========== //
targetScope = 'resourceGroup'

@description('Solution Location')
//param solutionLocation string
param managedIdentityId string
param managedIdentityPropPrin string
param managedIdentityLocation string
@description('Managed Identity Name')
param miName string

// resource managedIdentity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
//   name: miName
//   location: solutionLocation
//   tags: {
//     app: solutionName
//     location: solutionLocation
//   }
// }

@description('This is the built-in owner role. See https://docs.microsoft.com/azure/role-based-access-control/built-in-roles#owner')
resource ownerRoleDefinition 'Microsoft.Authorization/roleDefinitions@2018-01-01-preview' existing = {
  scope: resourceGroup()
  name: '8e3af657-a8ff-443c-a75c-2fe8c4bcb635'
}

resource roleAssignment 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(resourceGroup().id, managedIdentityId, ownerRoleDefinition.id)
  properties: {
    principalId: managedIdentityPropPrin
    roleDefinitionId:  ownerRoleDefinition.id
    principalType: 'ServicePrincipal' 
  }
}


output managedIdentityOutput object = {
  id: managedIdentityId
  objectId: managedIdentityPropPrin
  resourceId: managedIdentityId
  location: managedIdentityLocation
  name: miName
}

output managedIdentityId string = managedIdentityId
