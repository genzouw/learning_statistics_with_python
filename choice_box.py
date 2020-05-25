#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

boxes = []
for line in sys.stdin:
    boxes.append([int(n) for n in line.rstrip().split(",")])

count_of_boxes = len(boxes)

RED = 0
BLUE = 1

color = RED
#  color = BLUE

p_c = sum([1 / count_of_boxes * box[color] / sum(box) for box in boxes])

for i, box in enumerate(boxes):
    p_cb = box[color] / sum(box)
    p_b = 1 / count_of_boxes
    print("boxes[" + str(i) + "]から引いた可能性 : " + str(p_cb * p_b / p_c))
