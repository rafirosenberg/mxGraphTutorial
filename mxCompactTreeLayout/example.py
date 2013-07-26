#!/usr/bin/python

import xml.etree.ElementTree as xml
import random

team = [("president", 1)]
vices = random.randint(4,7)
v=0
while v < vices:
    v+=1
    team.append(('vice president %s' % v, 2 , v) )
    members = random.randint(2,10)
    me=0
    while me < members:
        me+=1
        team.append(('team member %s' % me , 3, v))
print(team)

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
        newMxGeometry=xml.Element('mxGeometry', x='0', y='0', width='80', height='120')
        newMxGeometry.set('as','geometry')
        newCell.append(newMxGeometry)
        
    elif member[1] == 2:
        newCell=xml.Element('mxCell', id=member[0]+'_vertex', value=member[0], vertex='1', parent='1')
        newMxGeometry=xml.Element('mxGeometry', x='0', y='0', width='70', height='120')
        newMxGeometry.set('as','geometry')
        newCell.append(newMxGeometry)
        newEdge=xml.Element('mxCell', id=member[0]+"_edge",
                            value='', edge="1", parent="1", source='president_vertex', target=member[0]+'_vertex')
        newEdgeGeo=xml.Element('mxGeometry', relative='1')
        newEdgeGeo.set('as','geometry')
        newEdge.append(newEdgeGeo)
        root.append(newEdge)
    elif member[1] == 3:
        m+=1
        newCell=xml.Element('mxCell', id=member[0]+'-'+str(m)+'_vertex', value=member[0],
                            vertex='1', parent='1')
        newMxGeometry=xml.Element('mxGeometry', x='0', y='0', width='60', height='120')
        newMxGeometry.set('as','geometry')
        newCell.append(newMxGeometry)
        newEdge=xml.Element('mxCell', id=member[0]+'-'+str(m)
                            +'_edge', value='', edge="1", parent="1",
                            target=member[0]+'-'+str(m)+'_vertex', source='vice president '+str(member[2])+'_vertex')
        newEdgeGeo=xml.Element('mxGeometry', relative='1')
        newEdgeGeo.set('as','geometry')
        newEdge.append(newEdgeGeo)
        root.append(newEdge)
    root.append(newCell)
    
    

    
file = open("example.xml", 'w')
xml.ElementTree(model).write(file)
file.close()