# Bee Algorithm
The aim of a bee swarm is to find the area of a field with the highest density of flowers. WIthout any knoledge about a field bees begin the search of flowers from random positions with random velocity vectors. Each bee can remember positions where the maximul quantity of flowers was found and know where other bees found the maximum density of flowers. When a bee chooses between the place where it found the maximum quantity of flowers and the place which was reported by others, the bee rushes in direction between these two points and desides between personal memory and social reflex. On its way the bee can find a place with more high concentration of flowers than were found previously. In the future this place can be marked as the one with the highest concentration of flowers found by a swarm. After that the whole swarm will rush in the direction of this place, remembering though their own observations. Thus, bees research a field by flying to palces with the highest consentration of flowers. They also continuously compare places they flew over with previously found ones in order to found the absolute maxim concentration of flowers. In the end, a bee ends its flight in the place with the maximum concentration of flowers. Soon the whole swarm will locate in the neighborhood of that place.

## Mathematical model
In the Bee Algorithm model, the colony consists of three groups of bees: employed bees, onlookers and scouts. Scouts perform random search, employed bees collect previously found food and onlookers watch the dances of employed bees and choose food sources depending on dances. Onlookers and scouts are called non-working bees. Communication between bees is based on dances. Before a bee starts to collect food it watches dances of other bees. A dance is the way bees describe where food is.

Working and non-working bees search for rich food sources near their hive. A working bee keeps the information about a food source and share it with onlookers. Working bees whose solutions can't be improved after a definite number of attempts become scouts and their solutions are not used after that. The number of food sources represents the nuber of solutions in the population. The position of a food source represents a possible solution to the optimization problem and the nectar amount of a food source corresponds to the quality (fitness) of the associated solution.

## Algorithm
```
BEGIN
Initialize the population
Find current best agent for the initial iteration
Calculate the number of scouts, onlookers and employed bees
SET global best to current best
FOR iterator = 0 : iteration
  evaluate fitness for each agent
  sort fitness in ascending order and get best agents
  from best agents list select agents from a to c
  Create new bees which will fly to the best solution
  Evaluate current best agent
  IF function(current best) < function (global best)
    global best = current best
  END IF
END FOR
Save global best
```
## Arguments
The aba method accepts only standard arguments

## Method invocation
The method can be invoked by passing the arguments in the following order:

```
SwarmPackagePy.aba(n, function, lb, ub, dimension, iteration)
```