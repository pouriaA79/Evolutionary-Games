
import numpy as np
import pygame

from config import CONFIG
from nn import NeuralNetwork


class Player():

    def __init__(self, mode, control=False):

        # if True, playing mode is activated. else, AI mode.
        self.control = control
        self.pos = [100, 275]  # position of the agent
        self.direction = -1  # if 1, goes upwards. else, goes downwards.
        self.v = 0  # vertical velocity
        self.g = 9.8  # gravity constant
        self.mode = mode  # game mode

        # neural network architecture (AI mode)
        layer_sizes = self.init_network(mode)

        self.nn = NeuralNetwork(layer_sizes)
        self.fitness = 0  # fitness of agent

    def move(self, box_lists, camera, events=None):

        if len(box_lists) != 0:
            if box_lists[0].x - camera + 60 < self.pos[0]:
                box_lists.pop(0)

        mode = self.mode

        # manual control
        if self.control:
            self.get_keyboard_input(mode, events)

        # AI control
        else:
            agent_position = [camera + self.pos[0], self.pos[1]]
            self.direction = self.think(
                mode, box_lists, agent_position, self.v)

        # game physics
        if mode == 'gravity' or mode == 'helicopter':
            self.v -= self.g * self.direction * (1 / 60)
            self.pos[1] += self.v

        elif mode == 'thrust':
            self.v -= 6 * self.direction
            self.pos[1] += self.v * (1 / 40)

        # collision detection
        is_collided = self.collision_detection(mode, box_lists, camera)

        return is_collided

    # reset agent parameters
    def reset_values(self):
        self.pos = [100, 275]
        self.direction = -1
        self.v = 0

    def get_keyboard_input(self, mode, events=None):

        if events is None:
            events = pygame.event.get()

        if mode == 'helicopter':
            self.direction = -1
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.direction = 1

        elif mode == 'thrust':
            self.direction = 0
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.direction = 1
            elif keys[pygame.K_DOWN]:
                self.direction = -1

        for event in events:
            if event.type == pygame.KEYDOWN:

                if mode == 'gravity' and event.key == pygame.K_SPACE:
                    self.direction *= -1

    def init_network(self, mode):

        # you can change the parameters below

        layer_sizes = None
        if mode == 'gravity':
            layer_sizes = [7, 100, 1]
        elif mode == 'helicopter':
            layer_sizes = [7, 100, 1]
        elif mode == 'thrust':
            layer_sizes = [7, 100, 1]
        return layer_sizes

    def think(self, mode, box_lists, agent_position, velocity):
        count = 0
        input_values = np.zeros(shape=(7, 1))
        if mode == "helicopter" :
            if (len(box_lists) > 0):
                found_nearest_box = False
                for box in box_lists:
                    if (agent_position[0] < box.x):
                        count += 1
                        if count == 1:
                            found_nearest_box = True
                            input_values[0, 0] = (
                                                         box.x - agent_position[0]) / CONFIG['WIDTH']
                            input_values[1, 0] = (
                                                         box.gap_mid - agent_position[1]) / CONFIG['HEIGHT']
                        elif count == 2:

                            input_values[2, 0] = (box.x - agent_position[0]) / CONFIG['WIDTH']
                            input_values[3, 0] = (box.gap_mid - agent_position[1]) / CONFIG['HEIGHT']
                        elif count == 3:
                            input_values[4, 0] = (box.x - agent_position[0]) / CONFIG['WIDTH']
                            input_values[5, 0] = (box.gap_mid - agent_position[1]) / CONFIG['HEIGHT']

                        if count == 3:
                            break
            if ((len(box_lists) == 0) or (not (found_nearest_box))):
                input_values[1, 0] = 0.2
                input_values[2, 0] = CONFIG['HEIGHT'] / 1000
                input_values[3, 0] = CONFIG['WIDTH'] / 1300
                input_values[4, 0] = 0
            # input_values[7, 0] = agent_position[0]/CONFIG['WIDTH']
            # input_values[8, 0] = agent_position[1]/CONFIG['HEIGHT']
            input_values[6, 0] = velocity / (10)
            output = self.nn.forward(input_values)
            if output > 0:
                return 1
            else:
                return -1
        elif  mode == "gravity":
            if (len(box_lists) > 0):
                found_nearest_box = False
                for box in box_lists:
                    if (agent_position[0] < box.x):
                        count += 1
                        if count == 1:
                            found_nearest_box = True
                            input_values[0, 0] = (
                                                         box.x - agent_position[0]) / CONFIG['WIDTH']
                            input_values[1, 0] = (
                                                         box.gap_mid - agent_position[1]) / CONFIG['HEIGHT']
                        elif count == 2:

                            input_values[2, 0] = (box.x - agent_position[0]) / CONFIG['WIDTH']
                            input_values[3, 0] = (box.gap_mid - agent_position[1]) / CONFIG['HEIGHT']
                        elif count == 3:
                            input_values[4, 0] = (box.x - agent_position[0]) / CONFIG['WIDTH']
                            input_values[5, 0] = (box.gap_mid - agent_position[1]) / CONFIG['HEIGHT']

                        if count == 3:
                            break
            if ((len(box_lists) == 0) or (not (found_nearest_box))):
                input_values[1, 0] = 0.2
                input_values[2, 0] = CONFIG['HEIGHT'] / 1000
                input_values[3, 0] = CONFIG['WIDTH'] / 1300
                input_values[4, 0] = 0
            # input_values[7, 0] = agent_position[0]/CONFIG['WIDTH']
            # input_values[8, 0] = agent_position[1]/CONFIG['HEIGHT']
            input_values[6, 0] = velocity / (10)
            output = self.nn.forward(input_values)
            if output > 0:
                return 1
            else:
                return -1

















        # return direction

    def collision_detection(self, mode, box_lists, camera):
        if mode == 'helicopter':
            rect = pygame.Rect(self.pos[0], self.pos[1], 100, 50)
        elif mode == 'gravity':
            rect = pygame.Rect(self.pos[0], self.pos[1], 70, 70)
        elif mode == 'thrust':
            rect = pygame.Rect(self.pos[0], self.pos[1], 110, 70)
        else:
            rect = pygame.Rect(self.pos[0], self.pos[1], 50, 50)
        is_collided = False

        if self.pos[1] < -60 or self.pos[1] > CONFIG['HEIGHT']:
            is_collided = True

        if len(box_lists) != 0:
            box_list = box_lists[0]
            for box in box_list.boxes:
                box_rect = pygame.Rect(box[0] - camera, box[1], 60, 60)
                if box_rect.colliderect(rect):
                    is_collided = True

        return is_collided
