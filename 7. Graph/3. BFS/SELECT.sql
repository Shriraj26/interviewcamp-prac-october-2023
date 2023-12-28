SELECT
    a.username,
    r.consumption AS consumption,
    ROUND(SUM(CASE WHEN t.name = 'A' AND r.consumption <= CAST(SUBSTRING_INDEX(t.consumption_range, '-', 1) AS UNSIGNED) 
    THEN r.consumption * t.cost ELSE 0 END), 2) AS 'A(0-200)',

    ROUND(SUM(CASE WHEN t.name = 'B' AND r.consumption >= CAST(SUBSTRING_INDEX(t.consumption_range, '-', -1) AS UNSIGNED) 
    AND r.consumption <= CAST(SUBSTRING_INDEX(t.consumption_range, '-', 1) 
    AS UNSIGNED) THEN (r.consumption - CAST(SUBSTRING_INDEX(t.consumption_range, '-', -1) 
    AS UNSIGNED) + 1) * t.cost ELSE 0 END), 2) AS 'B(201-499)',
    
    ROUND(SUM(CASE WHEN t.name = 'C' AND r.consumption >= CAST(SUBSTRING_INDEX(t.consumption_range, '-', -1) AS UNSIGNED) 
    THEN (r.consumption - CAST(SUBSTRING_INDEX(t.consumption_range, '-', -1) AS UNSIGNED) + 1) * t.cost ELSE 0 END), 2) AS 'C(500+)'
FROM
    accounts a
JOIN
    readings r ON a.id = r.account_id
JOIN
    tariffs t ON r.consumption >= CAST(SUBSTRING_INDEX(t.consumption_range, '-', -1) AS UNSIGNED)
            AND (r.consumption <= CAST(SUBSTRING_INDEX(t.consumption_range, '-', 1) AS UNSIGNED) OR t.consumption_range LIKE '%-%')
GROUP BY
    a.username, r.consumption
ORDER BY
    a.username;
