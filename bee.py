from math import exp
import numpy as np
from random import random

class sw(object):

    def __init__(self):

        self.positions = []
        self.gbest = []

    def set_gbest(self, gbest):
        self.gbest = gbest

    def points(self, agents):
        self.positions.append([list(i) for i in agents])

    def get_agents(self):
        """
            Returns list berisi history semua agents
        """
        return self.positions

    def get_gbest(self):
        """
            Return list the best position 
        """
        return list(self.gbest)

class ba(sw):
    """
    Bat Algorithm
    """

    def __init__(self, n, function, lb, ub, dimension, iteration, r0=0.9,
                 V0=0.5, fmin=0, fmax=0.02, alpha=0.9, csi=0.9):
        """
        :param n: number of agents
        :param function: test function
        :param lb: lower limits for plot axes
        :param ub: upper limits for plot axes
        :param dimension: space dimension
        :param iteration: number of iterations
        :param r0: level of impulse emission (default value is 0.9)
        :param V0: volume of sound (default value is 0.5)
        :param fmin: min wave frequency (default value is 0)
        :param fmax: max wave frequency (default value is 0.02)
            fmin = 0 and fmax =0.02 - the bests values
        :param alpha: constant for change a volume of sound
         (default value is 0.9)
        :param csi: constant for change a level of impulse emission
         (default value is 0.9)
        """

        super(ba, self).__init__()

        r = [r0 for i in range(n)]

        self.agents = np.random.uniform(lb, ub, (n, dimension))
        self.points(self.agents)

        velocity = np.zeros((n, dimension))
        V = [V0 for i in range(n)]

        pbest = self.agents[np.array([function(i)
                                        for i in self.agents]
                                    ).argmin()]
        gbest = pbest

        f = fmin + (fmin - fmax)

        for t in range(iteration):

            sol = self.agents

            F = f * np.random.random((n, dimension))
            velocity += (self.agents - gbest) * F
            sol += velocity

            for i in range(n):
                if random() > r[i]:
                    sol[i] = gbest + np.random.uniform(-1, 1, (
                        1, dimension)) * sum(V) / n

            for i in range(n):
                if function(sol[i]) < function(self.agents[i]) \
                        and random() < V[i]:
                    self.agents[i] = sol[i]
                    V[i] *= alpha
                    r[i] *= (1 - exp(-csi * t))

            self.agents = np.clip(self.agents, lb, ub)
            self.points(self.agents)

            pbest = self.agents[np.array(
                                    [function(x) for x in self.agents]
                                ).argmin()]
            if function(pbest) < function(gbest):
                gbest = pbest

        self.set_gbest(gbest)