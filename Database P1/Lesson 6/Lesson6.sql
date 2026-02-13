-- 1. List all data from 'routestop' table (32657 rows)
-- SELECT * FROM routestop;

-- 2. List only first 100 results from ‘routestop’ table (100 rows)
-- SELECT * FROM routestop LIMIT 100;	

-- 3. List all data from 'stops' table (6330 rows)
-- SELECT * FROM stops;

-- 4. List last 100 results from 'stops' table (100 rows)
-- SELECT * FROM stops LIMIT 100 OFFSET 6230;

-- 5. List all stops of route 1A (inbound) (34 rows)
-- SELECT * FROM routestop WHERE route="1A";

-- 6. List sequence number, stop ID, english name & chinese name of all stops of route 1A (inbound) (34 rows)
-- SELECT CONVERT(seq AS integer), routestop.stop, name_en, name_tc  FROM routestop JOIN stops On routestop.stop=stops.stop WHERE route="1A" AND bound="I" ORDER BY seq ASC;

-- 7. From Q6, list results in ascending order of sequence number (34 rows)
-- ALTER TABLE routestop MODIFY seq INT;
-- SELECT route, seq, routestop.stop, name_en, name_tc FROM routestop JOIN stops On routestop.stop=stops.stop WHERE route="1A" AND bound="I" ORDER BY seq ASC;

-- 8. Change data type of 'seq' from 'routestop' table to INT. Manual action on workbench is allowed, SQL query must NOT be used
-- ALTER TABLE routestop MODIFY seq INT;

-- 9. Run result from Q7 again, tell & explain the difference (34 rows)
-- Order according to string vs integer

-- 10. From Q9, also list latitude & longitude of each bus stop of route 1A (inbound) (34 rows)
-- SELECT route, seq, stops.`stop`, name_en, name_tc, lat, `long` FROM routestop JOIN stops On routestop.stop=stops.stop WHERE route="1A" AND bound="I";


-- 11. List all bus routes & its sequence number that has a stop at 'Telford Gardens' (43 rows)
-- SELECT route, seq, name_en FROM routestop JOIN stops On routestop.stop=stops.stop WHERE name_en="TELFORD GARDENS";

-- 12. From Q11, also list the route origin, direction (i.e. bound) (52 rows)
-- SELECT routes.route, routestop.bound, orig_en, seq, name_en
--   FROM 	routestop
--   INNER JOIN stops
--   ON routestop.`stop` = stops.`stop`
--   INNER JOIN routes
--   ON routes.route = routestop.route
--   WHERE name_en="TELFORD GARDENS";

-- 13. From Q12, clean up the data by avoiding duplicate records display (39 rows)
-- SELECT DISTINCT routes.route, routestop.bound, orig_en, seq, name_en
--   FROM 	routestop
--   INNER JOIN stops
--   ON routestop.`stop` = stops.`stop`
--   INNER JOIN routes
--   ON routes.route = routestop.route
--   WHERE name_en="TELFORD GARDENS";	

-- 14. From Q13, list results in ascending order of route number & bound (39 rows)