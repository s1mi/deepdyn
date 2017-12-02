import math as mth

import networkx as nx


def assign_cost(graph=nx.Graph(), images=[()], alpha=1, override=False, log=False):
    i = 0
    for n1 in graph.nodes():
        for n2 in nx.neighbors(graph, n1):
            if graph[n1][n2] == {} or override:
                cost = 0.0
                # ix = 1
                for weight, arr in images:
                    i_diff = max(arr[n1[0], n1[1]], arr[n2[0], n2[1]])
                    cost += weight * mth.pow(mth.e, alpha * (i_diff / 255))
                    # graph[n1][n2]['i_diff_' + str(ix)] = i_diff
                    # ix += 1
                graph[n1][n2]['cost'] = cost
        if log:
            print('\r' + str(i) + ': ' + str(n1), end='')
            i += 1


def get_seed_node_list(image_array_2d=None):
    seed = []
    for i in range(image_array_2d.shape[0]):
        for j in range(image_array_2d.shape[1]):
            if image_array_2d[i, j] == 0:
                seed.append((i, j))
    return seed