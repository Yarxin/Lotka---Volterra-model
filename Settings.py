VICTIM_QUANTITY = 100
PREDATOR_QUANTITY = 5

predator_population = []
victim_population = []

AREA = 300

### satiety mark, to prevent
### victim population's overpopulation
SATIETY = AREA/VICTIM_QUANTITY
MIN_SATIETY = 1.5


### vitality mark, which says
### about hunting failure
VITALITY = 3

### years, the number of years
### od simulation. The number is
### multiplicated by 365

YEARS = 1000
DAYS = YEARS * 365
