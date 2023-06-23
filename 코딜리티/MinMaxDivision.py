def isValid(A, max_block_cnt, max_block_size): # A, cnt(=K), mid

    block_sum = 0
    block_cnt = 0

    # A에서 처음부터 하나씩 원소 뽑아서
    for num in A:

        # block의 최대값(mid)을 넘어가면 블록 나누기
        if block_sum + num > max_block_size:
            block_sum = num
            block_cnt += 1
        
        # block의 최대값 넘을 때까지 num 을 더하자.
        # 각 bock의 합이 max_block_size(mid) 깞 이하인지
        else:
            block_sum += num
        
        # 이분 탐색을 통해 K만큼 블록이 안 나눠진다면,
        if block_cnt >= max_block_cnt:
            return False
        
        # # 이분 탐색을 통해 K만큼 블록이 나눠진다면,
        # K 이하의 블록으로 나눌 수 있는지.
        return True



def solution(K, M, A):

    cnt = K # 블록 수
    left = max(A) # 각 블록 sum의 최소값 # 가장 큰 값으로 초기화 # 5
    right = sum(A) # 모든 블록의 sum 값 #전체 합으로 초기화 # 25

    if cnt == 1: # case 1) 블록 수가 하나면, 나눌 거 없이
        return right # A의 전체 합
    if cnt >=  len(A): # case 2) 수열의 길이보다 블록 수가 더 많은 경우,
        return left # 수열에서 가장 큰 값

    # case 3) 이분 탐색
    while left <= right:
        mid = (left + right) // 2

        # 이분 탐색을 통해 K만큼 블록이 나눠진다면,
        if isValid(A, cnt, mid):  
            right = mid - 1 # mid가 너무 크다는 의미이기에 줄이기
        
        # 안 나눠진다면,
        else:
            # 한 블록의 최대값이 가장 작아지는 경우
            left = mid + 1 # 키우기

    return left




