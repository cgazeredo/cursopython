dist = float(input('Uma distancia em metros: '))
km = dist/1000
hm = dist/100
dam = dist/10
dm = dist*10
cm = dist*100
mm = dist*1000
print('A medida de {}m corresponde a'.format(dist))
print('{:.3f}km'.format(km))
print('{:.2f}hm'.format(hm))
print('{:.1f}dam'.format(dam))
print('{:.0f}dm'.format(dm))
print('{:.0f}cm'.format(cm))
print('{:.0f}mm'.format(mm))
