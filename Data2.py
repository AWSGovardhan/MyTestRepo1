from datapackage import Package

package = Package('datapackage.json')
package.getResource('resource').read()