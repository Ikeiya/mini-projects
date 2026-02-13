-- List last 100 results from 'stops' table (100 rows)
-- SELECT * FROM stops LIMIT 100 OFFSET 6230;

-- List all stops of route 1A (inbound) (34 rows)
-- SELECT * FROM routestop WHERE route="1A";

-- List sequence number, stop ID, english name & chinese name of all stops of route 1A (inbound) (34 rows)
SELECT CONVERT(seq AS integer), routestop.stop, name_en, name_tc  FROM routestop JOIN stops On routestop.stop=stops.stop WHERE route="1A" AND bound="I" ORDER BY seq ASC;