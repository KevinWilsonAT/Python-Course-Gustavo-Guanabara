hv_weight = 0
lg_weight = 0
weight = 0

for p in range(1, 6):
    weight = float(input('Insert weight of the person {}: '.format(p)))
    if p == 1:
        hv_weight = weight
        lg_weight = weight
    else:
        if weight > hv_weight:
            hv_weight = weight
        if weight < lg_weight:
            lg_weight = weight

print('Heaviest weight: {}Kg'.format(hv_weight))
print('Lightest weight: {}Kg'.format(lg_weight))
