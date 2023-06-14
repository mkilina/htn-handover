from gtpyhop import State

state = State("state 0")

state.objects = {'screwdriver'}
state.locations = {'table', 'exchange point', 'X', 'Y'}
state.agents = {'human', 'robot'}

state.holding = {'human': None, 'robot': None}
state.at = {'screwdriver': 'table', 'human': 'X', 'robot': 'Y'}
