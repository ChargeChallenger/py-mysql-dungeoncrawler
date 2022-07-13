class ItemAid:
    name = ''
    recovery = 0

lightAid = ItemAid()
lightAid.name = 'Малое зелье здоровья (+3)'
lightAid.recovery = 3

mediumAid = ItemAid()
mediumAid.name = 'Среднее зелье здоровья (+6)'
mediumAid.recovery = 6

hardAid = ItemAid()
hardAid.name = 'Большое зелье здоровья (+9)'
hardAid.recovery = 9

items = [lightAid, mediumAid, hardAid]