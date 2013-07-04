#!/usr/bin/python

import xml.etree.ElementTree as xml

team = (("president", 1),
("vice president 1", 2, 1),
("vice president 2", 2, 2),
("vice president 3", 2, 3),
("vice president 4", 2, 4),
("team 1 member", 3 , 1),
("team 1 member" ,3 , 1),
("team 1 member", 3 , 1),
("team 1 member", 3 , 1),
("team 2 member", 3 , 2), 
("team 2 member", 3 , 2),
("team 2 member", 3 , 2),
("team 2 member", 3 , 2),
("team 3 member", 3 , 3),
("team 3 member", 3 , 3),
("team 3 member", 3 , 3),
("team 3 member", 3 , 3),
("team 4 member", 3 , 4),
("team 4 member", 3 , 4),
("team 4 member", 3 , 4),
("team 4 member", 3 , 4))

model = xml.Element('mxGraphModel')
root = xml.Element('root')
model.append(root)
m=0
zero = xml.Element('mxCell',id='0')
one = xml.Element('mxCell',id='1', parent='0')
root.append(zero)
root.append(one)
for member in team:
    if member[1] == 1:
        newCell=xml.Element('mxCell', id=member[0]+'_vertex', value=member[0], vertex='1', parent='1')
        newMxGeometry=xml.Element('mxGeometry', x='0', y='0', width='80', height='70')
        newMxGeometry.set('as','geometry')
        newCell.append(newMxGeometry)
        #for responsibility in team:
        #    if responsibility[1] == member[1]+1:
        #            
    elif member[1] == 2:
        newCell=xml.Element('mxCell', id=member[0]+'_vertex', value=member[0], vertex='1', parent='1')
        newMxGeometry=xml.Element('mxGeometry', x='0', y='0', width='70', height='60')
        newMxGeometry.set('as','geometry')
        newCell.append(newMxGeometry)
        newEdge=xml.Element('mxCell', id=member[0]+"_edge", value='', edge="1", parent="1", source='president_vertex', target=member[0]+'_vertex')
        newEdgeGeo=xml.Element('mxGeometry', relative='1')
        newEdgeGeo.set('as','geometry')
        newEdge.append(newEdgeGeo)
        root.append(newEdge)
    elif member[1] == 3:
        m+=1
        newCell=xml.Element('mxCell', id=member[0]+'-'+str(m)+'_vertex', value=member[0], vertex='1', parent='1')
        newMxGeometry=xml.Element('mxGeometry', x='0', y='0', width='60', height='50')
        newMxGeometry.set('as','geometry')
        newCell.append(newMxGeometry)
        newEdge=xml.Element('mxCell', id=member[0]+'-'+str(m)+'_edge', value='', edge="1", parent="1", target=member[0]+'-'+str(m)+'_vertex', source='vice president '+str(member[2])+'_vertex')
        newEdgeGeo=xml.Element('mxGeometry', relative='1')
        newEdgeGeo.set('as','geometry')
        newEdge.append(newEdgeGeo)
        root.append(newEdge)
    root.append(newCell)
    
    

    
file = open("hierarchy.xml", 'w')
xml.ElementTree(model).write(file)
file.close()