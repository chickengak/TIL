def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0]*bridge_length
    bridge_weight = 0
    while truck_weights:
        bridge_weight -= bridge.pop(0)
        if bridge_weight+truck_weights[0] <= weight:
            bridge.append(truck_weights[0])
            bridge_weight += truck_weights.pop(0)
        else:
            bridge.append(0)
        time +=1
    return time + bridge_length