#!/usr/bin/python3
'''
pascal
'''


def pascal_triangle(n):
    if n < 0:
        return []

    jdida = []
    pvs = []

    for i in range(n):
        prp = []
        for j in range(i+1):
            if j == 0 or i == j:
                prp.append(1)
            else:
                pvs = jdida[i-1]
                prp.append(pvs[j-1]+pvs[j])
        jdida.append(prp)

    return jdida
