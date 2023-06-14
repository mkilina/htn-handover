import gtpyhop


def pick(state, agent, obj):
    if agent in state.agents and obj in state.objects and not state.holding[agent]:
        return [('transfer', agent, state.at[agent], state.at[obj]), ('grasp', agent, obj), ('transfer', agent, state.at[obj], 'exchange point')]

def exchange(state, agent1, agent2, obj):
    if agent1 in state.agents and agent2 in state.agents and state.holding[agent1] == obj:
        return[('grasp', agent2, obj), ('release', agent1, obj)]

def receive(state, agent, obj):
    if agent in state.agents and obj in state.objects and not state.holding[agent]:
        return [('transfer', agent, state.at[agent], 'exchange point')]

def handover(state, agent1, agent2, obj):
    if agent1 in state.agents and agent2 in state.agents:
        return[('pick', agent1, obj), ('receive', agent2, obj), ('exchange', agent1, agent2, obj)]

gtpyhop.declare_task_methods('pick', pick)
gtpyhop.declare_task_methods('receive', receive)
gtpyhop.declare_task_methods('exchange', exchange)

gtpyhop.declare_task_methods('handover', handover)