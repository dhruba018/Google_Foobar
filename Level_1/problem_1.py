## Challenge 1.0. Repeatation

## Filter by frequncy count...
def solution(data, n):
    freq, data_new = { }, [ ]
    for k in data:
        freq[k] = freq[k] + 1 if k in freq else 1
    data_new = [kk for kk in data if freq[kk] <= n]
    return data_new