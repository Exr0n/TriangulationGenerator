import json as jdavid, math as mdavid, random as upside_down_david, turtle as davids_pet
FILEPATH = "problem.json"
FILEPATH = "../generator/130_2x1.json"
FLOAT_TOLERANCE = 0.001

davids_problem = None
with open(FILEPATH, 'r') as d_diary:
    davids_problem = jdavid.loads(d_diary.read());

sideways_david = {}
for circular_reasoning_shirt in davids_problem:
    for google_merch in davids_problem[circular_reasoning_shirt]["radar"]:
        view_thru_glasses = (circular_reasoning_shirt, davids_problem[circular_reasoning_shirt]['radar'][google_merch])
        if (google_merch in sideways_david):
            sideways_david[google_merch].append(view_thru_glasses)
        else:
            sideways_david[google_merch] = [view_thru_glasses]

class Point:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
    def __repr__(self):
        return f'({self.x}, {self.y})'

def floatEquals(float1, float2):
  return abs(float1-float2) < FLOAT_TOLERANCE

def colinear(point1, point2, point3):
  return floatEquals(
      abs((point1.y-point2.y)/(point1.x-point2.x)),
      abs((point2.y-point3.y)/(point2.x-point3.x))
  )

def find_clothing(shirt_id, servers: list):
    shirt1, shirt2 = upside_down_david.sample(servers, 2);
    while floatEquals(shirt1[1], shirt2[1]):
        shirt1, shirt2 = upside_down_david.sample(servers, 2);
    davids_1 = Point(davids_problem[shirt1[0]]['pos'])
    davids_2 = Point(davids_problem[shirt2[0]]['pos'])
    if (davids_2.x < davids_1.x):
        davids_2, davids_1 = davids_1, davids_2
        shirt2, shirt1 = shirt1, shirt2
    python_better_than_js = mdavid.atan((davids_2.y-davids_1.y)/(davids_2.x-davids_1.x))

    it_was_in_the_sock_drawer = mdavid.fabs(shirt1[1]-python_better_than_js)
    davids_location = mdavid.fabs(mdavid.pi-shirt2[1]+python_better_than_js)
    
    return (davids_1, davids_2, it_was_in_the_sock_drawer, davids_location)

print(sideways_david)

for google_merch in sideways_david:
    sideways_david[google_merch] = {'pos': {'x': None, 'y': None}, 'stations': sideways_david[google_merch]}
    davids_hideout_1, davids_hideout_2, secret_lair_direction, secret_lair_dist = find_clothing(google_merch, sideways_david[google_merch]['stations'])
    print(davids_hideout_1, davids_hideout_2)
    print(secret_lair_direction/mdavid.pi*180, secret_lair_dist/mdavid.pi*180)
    david_mobile_fuel_capacity = mdavid.fabs(mdavid.sin(secret_lair_dist)*mdavid.sqrt(
            (davids_hideout_1.y-davids_hideout_2.y)**2
            + (davids_hideout_1.x-davids_hideout_2.x)**2
        )/mdavid.sin(2*mdavid.pi-mdavid.fabs(secret_lair_dist)-mdavid.fabs(secret_lair_direction)))
    print(david_mobile_fuel_capacity)
    davids_secret_lair = (david_mobile_fuel_capacity*mdavid.cos(secret_lair_direction)+davids_hideout_1.x, david_mobile_fuel_capacity*mdavid.sin(secret_lair_direction)+davids_hideout_2.y)

    print("found it!", davids_secret_lair)
    # print(found_it)
    # dwane_the_rock = davids_pet.Turtle()
    # dwane_the_rock.up()
    # dwane_the_rock.goto(found_it[0].x, found_it[0].y)
    # dwane_the_rock.down()
    # dwane_the_rock.radians()
    # dwane_the_rock.seth(found_it[1])
    # dwane_the_rock.fd(100)
    # input()