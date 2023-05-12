from icecream import ic



b0 = {'A': '00',
    'T': '01',
    'C': '10',
    'G': '11'}

b1 = {'AT': '0001',
    'AC': '0010',
    'AG': '0011',
    'TA': '0100',
    'TC': '0110',
    'TG': '0111',
    'CA': '1000',
    'CT': '1001',
    'CG': '1011',
    'GA': '1100',
    'GT': '1101',
    'GC': '1110'
    }

b2 = {'ATC': '000110',
      'ACT': '001001',
      'TAC': '010010',
      'TCA': '011000',
      'CAT': '100001',
      'CTA': '100100',

      'ATG': '000111',
      'AGT': '001101',
      'TGA': '011100',
      'TAG': '010011',
      'GAT': '110001',
      'GTA': '110100',

      'ACG': '001011',
      'AGC': '001110',
      'CGA': '101100',
      'CAG': '100011',
      'GAC': '110010',
      'GCA': '111000',

      'TCG': '011011',
      'TGC': '011110',
      'CGT': '101101',
      'CTG': '100111',
      'GCT': '111001',
      'GTC': '110110'
      }

gen_0 = [b0,b1,b2]
gen_0 = {'b0': 1,
         'b1': 2,
         'b2': 3
         }
gen_1 = [[b0,b1], [b0,b2], [b1,b2]]
gen_1 = {'b0b1': 4,
         'b1b0': 5,
        'b0b2': 6,
        'b2b0':7,
        'b1b2': 8,
        'b2b1': 9
            }

gen_2 = []
non_ds_g2 = []
ds_g2 = []

for i in gen_1:
    for k in gen_1:
        if i != k:
            #ic(i,k)
            _str = ''.join([i,k])
            gen_2.append(_str)
            if ('b0b0' in _str) or ('b1b1' in _str) or ('b2b2' in _str):
                non_ds_g2.append(_str)
            else:
                ds_g2.append(_str)
        else:
            ic(i,k)
gen_2 = dict(zip(gen_2,range(len(gen_2))))
non_ds_g2 = dict(zip(non_ds_g2,range(len(non_ds_g2))))
ds_g2 = dict(zip(ds_g2,range(len(ds_g2))))


ic(gen_2)
ic(non_ds_g2)
ic(ds_g2)
ic(len(gen_2))
ic(len(non_ds_g2))
ic(len(ds_g2))


gen_3_csds = []
for i in gen_2:
    for k in gen_2:
        if i != k:
            _str = ''.join([i,k])
            gen_3_csds.append(_str)
gen_3_csds = dict(zip(gen_3_csds,range(len(gen_3_csds))))


gen_3_cfds = []
for i in ds_g2:
    for k in ds_g2:
        if i != k:
            _str = ''.join([i,k])
            gen_3_cfds.append(_str)
gen_3_cfds = dict(zip(gen_3_cfds,range(len(gen_3_cfds))))



gen_3_csmds = []
for i in ds_g2:
    for k in non_ds_g2:
        if i != k:
            _str = ''.join([i,k])
            gen_3_csmds.append(_str)
gen_3_csmds = dict(zip(gen_3_csmds,range(len(gen_3_csmds))))


ic(len(gen_3_csds))
ic(len(gen_3_cfds))
ic(len(gen_3_csmds))


print(len(gen_0),len(gen_1),len(gen_2),len(gen_3_csds))
print(len(gen_0),len(gen_1),len(gen_2),len(gen_3_cfds))

CSDS = {
    '1': gen_0,
    '2': gen_1,
    '3': gen_2,
    '4': gen_3_csds
}

CFDS = {
    '1': gen_0,
    '2': gen_1,
    '3': gen_2,
    '4': gen_3_cfds  
}

CSMDS = {
    '1': gen_0,
    '2': gen_1,
    '3': gen_2,
    '4': gen_3_csmds
}
