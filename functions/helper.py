from state.rigid import rigid
import random

def is_a(variable: str, type: str):
    if type == 'pickable':
        return variable in rigid.types['component'] + rigid.types['tool'] + rigid.types['piece'] 
    elif type == 'for_handover':
        return variable in rigid.types['component'] + rigid.types['tool']
    else:
        return variable in rigid.types[type]
    
def is_in(var_list: list, type: str):
    result = True
    if type == 'pickable':
        for variable in var_list:
            if variable not in rigid.types['component'] + rigid.types['tool'] + rigid.types['piece']:
                result = False
    elif type == 'for_handover':
        for variable in var_list:
            if variable not in rigid.types['component'] + rigid.types['tool']:
                result = False
    else:
        for variable in var_list:
            if variable not in rigid.types[type]:
                result = False
    return result

def watch_human():  
    # actions_dict = dict(zip(range(1, len(rigid.human_actions)+1), rigid.human_actions))
    # actions_list = "\n".join([f'{key}. {actions_dict[key]}' for key in actions_dict])
    # action_id = input(f'What action is human performing?\n{actions_list}')
    # try:
    #     action_id = int(action_id)
    # except Exception:
    #     print('You need to type the number related to the action of your choice.')
    #     action = watch_human()
    # else:
    #     action = actions_dict[action_id]
    action = random.choice(rigid.human_actions)
    print(f'Human is performing {action}')
    return action