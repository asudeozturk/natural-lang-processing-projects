# Plan a Roadtrip Across the US
Intro to Artificial Intelligence course project

## Problem Description 
This program finds a road trip path that starts in any state and ends in one of the states: CA, NV, OR, or WA. \
Each state has national parks. Visiting a state means visiting all national parks within the state. \
States are grouped by zones. 12 zones in total \
The program uses Constraint Satisfaction Problem solver algorithm (backtracking). Returns the first complete and valid path it finds. \
A solution path satisfies the following contraints: \
- The path consists of exactly one state for each zone between initial and final zones.
- The path ends at zone 12.
- The path only move westward where zone 1 is east and zone 12 is west. 
- There must be a road between states on the path ie. can't drive between non-neighbor states 
- Total number of parks visited >= the number user provides


## Datasets
- driving2.csv - Driving distance between state capitals. A value > 0 indicates there is a road between states
- zones.csv - US states and corresponding zone numbers
- parks.csv - US states and number of national parks within each state

## User Input
- Initial state - where the roadtrip starts
- Minimum number of parks to visit

## Output
- Solution path (if possible)
- Number of states on the path
- Path cost (total driving distance in miles)
- Number of natoinal parks visited
