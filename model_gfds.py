# CODE FOR SAMPLER 1: 
# GF-DS		Generic, Full-DS: 			(3, 3, 6, 30)
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
        'b0b2': 5,
        'b1b2': 6,
        }

gen_2 = {'b0b1b0b2': 7,
        'b1b0b1b2': 8,
        'b0b1b2b1': 9,
        'b1b0b2b1': 10,
        'b0b2b1b2': 11
        }


gen_3 = []
for i in gen_2:
    for k in gen_2:
        if i != k:
            ic(i,k)
            _str = ''.join([i,k])
            gen_3.append(_str)
gen_3 = dict(zip(gen_3,range(len(gen_3))))


ic(gen_0)
ic(gen_1)
ic(gen_2)
ic(gen_3)

print(len(gen_0),len(gen_1),len(gen_2),len(gen_3))

GFDS = {
    '1': gen_0,
    '2': gen_1,
    '3': gen_2,
    '4': gen_3 
}
