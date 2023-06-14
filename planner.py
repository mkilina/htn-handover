import gtpyhop

domain = gtpyhop.Domain('handover')

from methods.methods import *
from actions.actions import *

gtpyhop.current_domain = domain

from state.state import state

state.display('This is initial state')

state1 = state.copy()

gtpyhop.verbose = 3

gtpyhop.print_domain()

result = gtpyhop.find_plan(state1, [('handover', 'robot', 'human', 'screwdriver')])