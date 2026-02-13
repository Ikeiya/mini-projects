-- Exercise 1
-- 1. List all information of routes
SELECT * FROM `routes`;

-- 2. List route number, direction, start origin and destination in english
-- SELECT route, bound, orig_en, dest_en FROM routes

-- 3A. List all routes' number origin from Kwun Tong Ferry
-- SELECT * FROM routes WHERE orig_en="KWUN TONG FERRY";

-- 3B. List all routes' number origin from Kwun Tong Ferry, with service type is 1
-- SELECT * FROM routes WHERE orig_en="KWUN TONG FERRY" AND service_type="1";

-- 4. List total number of routes origin from Kwun Tong Ferry
-- SELECT SUM(orig_en="KWUN TONG FERRY") FROM routes;

-- 5A. List all available service types
-- SELECT DISTINCT service_type FROM routes;

-- 5B. List all available service types in ascending order
-- SELECT DISTINCT service_type FROM routes ORDER BY service_type ASC;

-- 6. List the number of routes according to service types
-- SELECT * FROM routes ORDER BY service_type ASC;

-- 7. List unique list of route numbers start with 'N', also list their origin and destination. 
-- Only inbound route is required to list
-- SELECT DISTINCT route, orig_en, dest_en FROM routes WHERE route LIKE 'N%'; 

-- 8. List unique list of route numbers end with 'X', also list their origin and destination. 
-- Only inbound route is required to list
-- SELECT DISTINCT route, bound, orig_en, dest_en FROM routes WHERE route LIKE '%X' AND bound='O';

-- 9. List total count of routes of each origin, order from the most route origin to the least
-- SELECT DISTINCT(orig_en) AS `sum_route`, COUNT(orig_en) FROM routes GROUP BY orig_en ORDER BY COUNT(orig_en) DESC;


-- 10. List total count of routes of each origin that more than 10, order from the most route origin to the least
-- SELECT DISTINCT(orig_en) AS `sum_route`, COUNT(orig_en) FROM routes GROUP BY orig_en HAVING COUNT(orig_en)>=10 ORDER BY COUNT(orig_en) DESC ;