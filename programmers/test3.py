def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append(None)

    n = 0
    while participant[n] == completion[n]:
        n += 1

    return participant[n]


participant = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
completion = ['josipa', 'filipa', 'marina', 'nikola']

solution(participant,completion)