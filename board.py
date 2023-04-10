""" 
    THIS IS A MESH CLASS
"""
import pygame

class Board:
    # parameter:
    # left top point and right point point, 
    # left bottom point and right bottom point
    def __init__(self, l_t_p, r_t_p, l_b_p, r_b_p):
        self.p1 = l_t_p
        self.p2 = r_t_p
        self.p3 = l_b_p
        self.p4 = r_b_p

    def create_mesh(self, surface):
        pygame.draw.aalines(surface, (255,255,255), True, [self.p1, self.p2, self.p3, self.p4])
        
        # col
        col1 = (self.p2[0] - self.p1[0]) // 3
        col2 = 2 * col1
        pygame.draw.aaline(surface, (255,255,255), (col1 + self.p1[0] , self.p1[1]), (col1 + self.p1[0], self.p4[1]))
        pygame.draw.aaline(surface, (255,255,255), (col2 + self.p1[0], self.p2[1]), (col2 + self.p1[0], self.p3[1]))

        #row
        row1 = (self.p4[1] - self.p1[1]) // 3
        row2 = 2 * row1
        pygame.draw.aaline(surface, (255,255,255), (self.p1[0], row1 + self.p1[1]), (self.p2[0], row1 + self.p1[1]))
        pygame.draw.aaline(surface, (255,255,255), (self.p1[0], row2 + self.p1[1]), (self.p2[0],row2 + self.p1[1]))

