-- https://app.codility.com/demo/results/trainingVUQJ38-RBH/

WITH rank_events as (
    SELECT event_type, value, time, RANK() OVER (
        PARTITION BY event_type -- event_type 으로 파티션을 나누고.
        ORDER BY time DESC -- 최근 시간 부터 랭크를 매김. rank이라는 컬럼 이름으로로
    ) rank
    FROM events
)

SELECT A.event_type, A.value-B.value AS value
FROM (SELECT * FROM rank_events WHERE rank = 1) A
JOIN (SELECT * FROM rank_events WHERE rank = 2) B
ON A.event_type = B.event_type
ORDER BY 1;