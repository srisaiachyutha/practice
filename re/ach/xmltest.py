import xml.etree.ElementTree as eff
a=eff.Element('sur')
b=eff.SubElement(a,'name').text='hello'

tree=eff.ElementTree(a)
tree.write('new.xml')
print('open the required file to seee the updated data')
                                                                                                                                                                                                                            
