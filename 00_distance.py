#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']

moscow_london = ((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** .5
moscow_paris = ((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** .5

london_moscow = ((london[0] - moscow[0]) ** 2 + (london[1] - paris[1]) ** 2) ** .5
london_paris = ((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** .5

paris_london = ((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** .5
paris_moscow = ((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** .5

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}

distances['Moscow'] = {}
distances['Moscow']['London'] = [moscow_london]
distances['Moscow']['Paris'] = [moscow_paris]

distances['London'] = {}
distances['London']['Moscow'] = [moscow_london]
distances['London']['Paris'] = [moscow_paris]

print(distances)
