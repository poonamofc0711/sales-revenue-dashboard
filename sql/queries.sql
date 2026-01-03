-- Throughput by Date
SELECT Date, SUM(Units_Produced) AS Throughput
FROM Production_Log
GROUP BY Date
ORDER BY Date;

-- Defect Rate by Department
SELECT Department, (SUM(Defects) * 1.0 / SUM(Units_Produced)) * 100 AS Defect_Rate
FROM Production_Log
GROUP BY Department;

-- Average Cycle Time by Department
SELECT Department, AVG(Cycle_Time) AS Avg_Cycle_Time
FROM Production_Log
GROUP BY Department;

-- Efficiency by Date
SELECT Date, (SUM(Units_Produced) * 1.0 / SUM(Expected_Output)) * 100 AS Efficiency
FROM Production_Log
GROUP BY Date
ORDER BY Date;

-- Downtime by Department
SELECT Department, SUM(Downtime) AS Total_Downtime
FROM Production_Log
GROUP BY Department;

-- OEE by Department
SELECT Department, AVG(OEE) AS Avg_OEE
FROM (
    SELECT 
        Department, 
        ((480 - Downtime) / 480.0) * 
        ((Units_Produced * Ideal_Cycle_Time) / (480 - Downtime)) * 
        ((Units_Produced - Defects) / Units_Produced) * 100 AS OEE
    FROM Production_Log
) AS sub
GROUP BY Department;
