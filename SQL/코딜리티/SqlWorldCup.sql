-- https://app.codility.com/demo/results/trainingDGH2MQ-ZDW/
WITH 
    win_table AS (
        SELECT CASE WHEN host_goals > guest_goals then host_team
                    WHEN host_goals < guest_goals then guest_team
                    END AS team_id,
                3 AS points
        FROM matches
        WHERE host_goals != guest_goals
),
    draw_table AS (
        SELECT host_team AS team_id, 1 AS points FROM matches WHERE host_goals = guest_goals
        UNION ALL
        SELECT guest_team AS team_id, 1 AS points FROM matches WHERE host_goals = guest_goals
),
    points_table AS (
        SELECT * FROM win_table
        UNION ALL
        SELECT * FROM draw_table
)
    

SELECT teams.team_id, teams.team_name, COALESCE(points_sum_table.num_points, 0) AS num_points
FROM teams LEFT JOIN(
    SELECT team_id, sum(points) as num_points FROM points_table GROUP BY team_id) points_sum_table 
    ON teams.team_id = points_sum_table.team_id
ORDER BY 3 DESC, 1
;