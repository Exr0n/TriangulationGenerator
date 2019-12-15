BOUNDARY = 300
SEED = 130
FLOAT_TOLERANCE = 0.001

import random, math, turtle, json

class Point:
  def __init__(self, x, y, id=0):
    self.x = x;
    self.y = y;
    self.id = id;
    if (self.id <= 0): # assign random id by default
      self.id = random.randint(1, 10*BOUNDARY)
    random.seed(self.id)
    self.color = (random.random(), random.random(), random.random()) # RGB value based on id

  def draw(self, t):
    t.up()
    t.goto(self.x, self.y)
    t.color(self.color)
    t.dot(5)
  
  def __repr__(self):
    return (self.x, self.y, self.id)

  def __str__(self):
    return self.__class__.__name__ + "[%d] @(%d, %d)" % (self.id, self.x, self.y)

class Station(Point):
  def __init__(self, x, y, id=0):
    super().__init__(x, y, id)
    self.radar = {}
  
  def draw(self, t):
    super().draw(t)
    t.dot(10)
    t.radians()
    for ship in self.radar:
      t.goto(self.x, self.y)
      t.color(self.radar[ship][0].color)
      t.down()
      t.seth(self.radar[ship][1])
      t.fd(3*BOUNDARY) # length needs to be at most 2sqrt2 * boundary
      t.up()
  
  def locate(self, ship):
    """Adds a ship to this station's the radar."""
    gamma = math.atan((ship.y-self.y)/(ship.x-self.x)) % math.pi
    if (ship.y < self.y): gamma -= math.pi # flip the heading if it should be, this is some pretty trippy math!
    self.radar[ship.id] = (ship, gamma)

class Ship(Point):
  pass

def floatEquals(float1, float2):
  return abs(float1-float2) < FLOAT_TOLERANCE

def colinear(point1, point2, point3):
  return floatEquals(
    abs((point1.y-point2.y)/(point1.x-point2.x)),
    abs((point2.y-point3.y)/(point2.x-point3.x))
  )

def generateStations(amount=5, seed=SEED):
  random.seed(seed)
  ret = []
  for i in range(amount):
    ret.append(Station(
      random.randint(-BOUNDARY, BOUNDARY),
      random.randint(-BOUNDARY, BOUNDARY)
    ))
  return ret;


def generateShipsFromStations(stations, amount=5, seed=SEED, fill=False):
  random.seed(seed)
  ret = []
  for i in range(amount):
    s1, s2 = random.sample(stations, 2)
    ship = Ship(
      random.randint(-BOUNDARY, BOUNDARY),
      random.randint(-BOUNDARY, BOUNDARY)
    )
    # When we generate ships, we want to make sure that atleast two stations aren't colinear, so what we do is we pick two and generate a ship that "fits" with that station pair.
    while (colinear(ship, s1, s2)):
      ship = Ship(
        random.randint(-BOUNDARY, BOUNDARY),
        random.randint(-BOUNDARY, BOUNDARY),
      )
    # This ship fits the station pair!
    ret.append(ship)
    print(f'Created ship at ({ship.x}, {ship.y})');
    # Add this ship to the "radar" of its corresponding stations.
    s1.locate(ship)
    s2.locate(ship)
    if (fill):
      for st in stations:
        st.locate(ship)
  return ret

def printMap(stations, ships, fast=False):
  t = turtle.Turtle()
  turtle.bgcolor(0, 0, 0)
  if (fast):
    turtle.tracer(0, 0)
  t.ht() # hide the turtle
  t.speed(10)

  # draw border
  t.up()
  t.goto(-BOUNDARY, -BOUNDARY)
  t.color(1, 1, 1)
  t.down()
  for x, y in ((-1, 1), (1, 1), (1, -1), (-1, -1)): # enumerate the corners
    t.goto(BOUNDARY*x, BOUNDARY*y)
  t.up()
  if fast: turtle.update()

  # draw the actual map
  for ship in ships:
    ship.draw(t)
  if fast: turtle.update()
  for station in stations:
    station.draw(t)
  if fast: turtle.update()
  return t

def output(seed, stations, ships):
  # for s in stations:
  #   print(f'Station #{s.id}: ({s.x}, {s.y})')
  #   sees = ""
  #   for sp in s.radar:
  #     print(f'  Ship #{sp} at heading {s.radar[sp][1]}')
  
  name = f'{seed}_{len(stations)}x{len(ships)}.json'
  _stations = {str(x.id): {"pos": [x.x, x.y], "radar": {s: x.radar[s][1] for s in x.radar}} for x in stations}
  with open(name, 'w+') as wf:
    wf.write(json.dumps(_stations, indent=2))
  print(f'Sucessfully wrote data to `{name}`!')

if __name__ == "__main__":
  random.seed(SEED)
  stations = generateStations(2)
  ships = generateShipsFromStations(stations, 1)

  output(SEED, stations, ships)
  printMap(stations, ships, False);
  t = input('Press ENTER to exit.\n')
