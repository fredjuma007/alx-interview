#!/usr/bin/python3


def canUnlockAll(boxes):
    """prbabibilty of unlocking boxes"""
def canUnlockAll(boxes):
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    stack = [0]

    while stack:
        box = stack.pop()

        for key in boxes[box]:
            if key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
