import json
f = open('coords.txt', 'r+')

features = list()
counter = 0
for line in f.readlines():
    features.append(dict())
    features[counter]['type'] = 'Feature'
    features[counter]['geometry'] = dict()
    features[counter]['geometry']['type'] = 'Polygon'
    features[counter]['geometry']['coordinates'] = list()
    features[counter]['geometry']['coordinates'].append(list())
    features[counter]['properties'] = dict()
    features[counter]['properties']['name'] = counter
    features[counter]['properties']['occupied'] = False
    #print line
    for corner in line.split('$'):
        point = corner.split(',')
        point[0] = float(point[0])
        point[1] = float(point[1])
       # point[1] = float(point[1].strip())
        features[counter]['geometry']['coordinates'][0].append(point)
        #box.append(point)
        #print point
    features[counter]['geometry']['coordinates'][0].insert(0,features[counter]['geometry']['coordinates'][0][-1])
    counter = counter+1

container = dict()
container['type'] = 'FeatureCollection'
container['features'] = features

o = open('coords_out.txt', 'w')
o.write(json.dumps(container, indent=4))
#print json.dumps(box, indent=4)

print json.dumps(container, indent=4)
print 'fa'
