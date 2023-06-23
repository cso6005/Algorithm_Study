-- https://school.programmers.co.kr/learn/courses/30/lessons/131123

-- 1
SELECT food_type, rest_id, rest_name, favorites
FROM rest_info
WHERE (food_type, favorites) IN (
    SELECT food_type, MAX(favorites)
    FROM rest_info
    GROUP BY food_type
)
group by food_type
ORDER BY food_type DESC;

-- 2
SELECT I.FOOD_TYPE, I.REST_ID, I.REST_NAME, F.FAVORITES
FROM REST_INFO I
JOIN (SELECT FOOD_TYPE, MAX(FAVORITES) FAVORITES FROM REST_INFO GROUP BY 1) F
ON I.FOOD_TYPE = F.FOOD_TYPE AND I.FAVORITES = F.FAVORITES
ORDER BY 1  DESC
;