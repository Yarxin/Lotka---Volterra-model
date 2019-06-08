VICTIM_QUANTITY = 110
PREDATOR_QUANTITY = 7

predator_population = []
victim_population = []

AREA = 300

### satiety mark, to prevent
### victim population's overpopulation
SATIETY = AREA/VICTIM_QUANTITY
MIN_SATIETY = 1


### vitality mark, which says
### about hunting failure
VITALITY = 6

### years, the number of years
### od simulation. The number is
### multiplicated by 365

YEARS = 50
DAYS = YEARS * 365
