
SELECT count(*) FROM Stations;

SELECT count(*) FROM Trips; -- 3136276(2014)

SELECT count(*) FROM StationsDet;


SELECT * FROM Stations LIMIT 10;

SELECT * FROM Trips LIMIT 10;

SELECT * FROM StationsDet;

SELECT st, b, su, m, COUNT(*)
FROM Stations2
GROUP BY st, b, su, m;


SELECT start_station_code, end_station_code, count(*)
FROM Trips
--WHERE start_station_code = 5002
GROUP BY start_station_code, end_station_code
ORDER BY 3 DESC
LIMIT 10
;



SELECT start_station_code, count(*)
FROM Trips
GROUP BY start_station_code
ORDER BY 2 DESC
LIMIT 5
;


SELECT end_station_code, count(*)
FROM Trips
GROUP BY end_station_code
ORDER BY 2 DESC
LIMIT 5
;


SELECT station_code, SUM(viajes)
FROM(
SELECT start_station_code AS station_code, count(*) AS viajes
FROM Trips
GROUP BY start_station_code
UNION ALL
SELECT end_station_code AS station_code, count(*) AS viajes
FROM Trips
GROUP BY end_station_code
)
GROUP BY station_code
ORDER BY 2 DESC
LIMIT 5

SELECT SUM(duration_sec)
FROM Trips;


SELECT DISTINCT LENGTH(start_date), LENGTH(end_date) 
FROM Trips;

----------------------------------------------------------------

SELECT * FROM StationsDet; --519

SELECT * FROM Stations_2014; --459

SELECT COUNT(*) FROM Stations_2015; --460

-- 6035 - Viger/Jeanne Mance
SELECT * FROM Stations_2014 a
WHERE NOT EXISTS(SELECT 1
				FROM Stations_2015 b
				WHERE b.code = a.code);

-- 6748	Greene / St-Ambroise
-- 6311	Drolet / St-Zotique
SELECT * FROM Stations_2015 a
WHERE NOT EXISTS(SELECT 1
				FROM Stations_2014 b
				WHERE b.code = a.code);

SELECT SUM(IFNULL(b.ba,0))
FROM Stations_2015 a
LEFT JOIN StationsDet b ON a.code = b.n;

SELECT ---COUNT(*) --296452/296116
SUBSTRING(start_date,1,13),start_date,SUBSTRING(end_date,1,13),end_date
FROM Trips
--WHERE SUBSTRING(start_date,1,16) <= '2014-04-15 13:15'
--AND SUBSTRING(end_date,1,16) >= '2014-04-15 13:15'
WHERE start_date <= '2014-04-15 13:15'
AND end_date >= '2014-04-15 13:15'
LIMIT 5;

SELECT MIN(start_date), MAX(end_date) FROM Trips;



