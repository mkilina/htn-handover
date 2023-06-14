import gtpyhop

def transfer(state, agent, loc_from, loc_to):
    if agent in state.agents and loc_from in state.locations and loc_to in state.locations and state.at[agent] == loc_from:
        state.at[agent] = loc_to
        if state.holding[agent]:
            obj = state.holding[agent]
            state.at[obj] = loc_to
        return state

def grasp(state, agent, obj):
    if agent in state.agents and obj in state.objects and state.at[agent] == state.at[obj] and not state.holding[agent]:
        state.holding[agent] = obj
        return state

def release(state, agent, obj):
    if agent in state.agents and obj in state.objects and state.holding[agent] == obj:
        state.holding[agent] = None
        return state 



gtpyhop.declare_actions(transfer, grasp, release)