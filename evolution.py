import copy
import random

import numpy as np

from player import Player


class Evolution():

    def __init__(self, mode):
        self.mode = mode

    # calculate fitness of players
    def calculate_fitness(self, players, delta_xs):
        for i, p in enumerate(players):
            p.fitness = delta_xs[i]

    def mutate(self, child):

        # if random.random() <= 0.5:
        if random.random() <= 0.15:
            child.nn.W1 += np.random.normal(loc=0, scale=0.15, size=child.nn.W1.shape)
        if random.random() <= 0.15:
            child.nn.W2 += np.random.normal(loc=0, scale=0.15, size=child.nn.W2.shape)
        # elif random.random() <= 0.3:
        #     child.nn.B1 += np.random.normal(loc=-0.6, scale=0.6, size=child.nn.B1.shape)
        # elif random.random() <= 0.3:
        # if random.random() <= 0.35:
        #     child.nn.W1 += np.random.normal(low=-15, high=15, size=child.nn.W1.shape)
        # if random.random() <= 0.35:
        #     child.nn.W2 += np.random.uniform(low=-15, high=15, size=child.nn.W2.shape)
        # elif random.random() <= 0.3:
        #     child.nn.B1 += np.random.normal(loc=-0.6, scale=0.6, size=child.nn.B1.shape)
        # elif random.random() <= 0.3:
        #     child.nn.B1 += np.random.normal(loc=-0.6, scale=0.6, size=child.nn.B2.shape)

    # TODO
    # child: an object of class `Player`

    def generate_new_population(self, num_players, prev_players=None):

        # in first generation, we create random players
        if prev_players is None:
            return [Player(self.mode) for _ in range(num_players)]

        else:

            # TODO (additional): a selection method other than `fitness proportionate`
            # Q Tournament
            prev_players.sort(key=lambda x: x.fitness, reverse=True)
            new_player = []
            for i in range(num_players):
                selected_prob = np.random.choice(num_players, int(num_players / 10))
                # for j in range(int(num_players / 10)):
                #     if prev_players[selected_prob[j]].fitness>max_score:
                #         max_score = prev_players[selected_prob[j]].fitness
                #         max_j = j
                max_j = min(selected_prob)
                new_player.append(copy.deepcopy(prev_players[max_j]))
                self.mutate(new_player[-1])
            return new_player

            #
            # new_player2 = []

            # TODO
            # RW
            # max = sum([x.fitness for x in prev_players])
            # selection_probs = [c.fitness / max for c in prev_players]
            #
            # for i in range(num_players):
            #     prob = random.random()
            #     find_prob = 0
            #     for j in range (num_players):
            #
            #         if find_prob < prob:
            #             find_prob += selection_probs[j]
            #         else:
            #             break
            #     new_player.append(copy.deepcopy(prev_players[j]))
            #     self.mutate(new_player[-1])
            #

            # TODO (additional): implementing crossover
            # new_players = []
            ######################
            # prev_players.sort(key=lambda x: x.fitness, reverse=True)
            # max = sum([x.fitness for x in prev_players])
            # selection_probs = [c.fitness / max for c in prev_players]
            # selected_probj = np.random.choice(num_players, num_players, p=selection_probs)
            # selected_probi = np.random.choice(num_players, num_players, p=selection_probs)
            # # selected_probc = np.random.choice(num_players, num_players, p=selection_probs)
            # for i in range(int(num_players / 2)):
            # selected_prob = np.random.choice(num_players, int(num_players / 10))
            # max_j = min(selected_prob)
            # new_player = copy.deepcopy(prev_players[max_j])

            # new_player = copy.deepcopy(prev_players[int(random.random()*num_players)])
            # new_player2 = copy.deepcopy(prev_players[int(random.random()*num_players)])
            #
            #
            # w2 = new_player.nn.W2
            #
            # new_player.nn.W2 = new_player2.nn.W2
            # new_player2.nn.W1 = w2
            #########################################
            # prev_players.sort(key=lambda x: x.fitness, reverse=True)
            # max = sum([x.fitness for x in prev_players])
            # selection_probs = [c.fitness / max for c in prev_players]
            # for i in range(int(num_players / 2)):
            #         selected_prob = np.random.choice(num_players, int(num_players / 10))
            #         max_j = min(selected_prob)
            #         new_player = copy.deepcopy(prev_players[max_j])
            #         # new_player = copy.deepcopy(prev_players[int(random.random()*num_players)])
            #         # new_player2 = copy.deepcopy(prev_players[max_j])
            #         new_player2 = copy.deepcopy(prev_players[int(random.random()*num_players)])
            #         new_player.nn.W1[0:int(new_player.nn.W1.shape[0] / 2)] = new_player2.nn.W1[
            #                                                              0:int(new_player2.nn.W1.shape[0] / 2)]
            #         # new_player.nn.W2[0:int(new_player.nn.W2.shape[0] / 2)] = new_player2.nn.W2[
            #         #                                                      0:int(new_player2.nn.W2.shape[0] / 2)]
            #         w1 = new_player.nn.W1[0:int(new_player.nn.W1.shape[0] / 2)]
            #         # w2 = new_player.nn.W2[0:int(new_player.nn.W2.shape[0] / 2)]
            #         new_player2.nn.W1[0:int(new_player2.nn.W1.shape[0] / 2)] = w1
            #         # new_player2.nn.W2[0:int(new_player2.nn.W2.shape[0] / 2)] = w2
            #
            #
            #         self.mutate(new_player)
            #         new_players.append(new_player)
            #         self.mutate(new_player2)
            #         new_players.append(new_player2)
            # return new_players

    # in first generation, we create random players

    # in first generation, we create random players

    def next_population_selection(self, players, num_players):

        # TODO (additional): a selection method other than `top-k`

        # new_player = []
        # max = sum([x.fitness for x in players])
        # selection_probs = [c.fitness / max for c in players]
        # selected_prob = np.random.choice(num_players, num_players, p=selection_probs)
        # for i in range(num_players):
        #     new_player.append(copy.deepcopy(players[selected_prob[i]]))
        # TODO (additional): plotting
        players.sort(key=lambda x: x.fitness, reverse=True)

        max = sum([x.fitness for x in players])
        selection_probss = [c.fitness for c in players]
        f = open("socres.txt", "a+")
        f.write(str(selection_probss[0]))
        f.write(" ")
        f.write(str(max / len(selection_probss)))
        f.write(" ")
        f.write(str(selection_probss[-1]))
        f.write("\n")

        # return new_player
        return players[: num_players]
