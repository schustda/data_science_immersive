/*  
PostgreSQL 
Investigate syntax for self-join introduced in afternoon lecture
*/

-- Start a transaction (series of commands)
BEGIN;

SET client_encoding = 'LATIN1';

-- Create the tables
CREATE TABLE customers                             (
    id      integer         PRIMARY KEY,
    name    text            NOT NULL
);


CREATE TABLE call_history                                (
    caller_id      integer      REFERENCES customers (id),
    receiver_id    integer      REFERENCES customers (id),
    c_date         character(5) NOT NULL,
    PRIMARY KEY(caller_id, receiver_id, c_date)
);

-- Fill the tables with data

COPY customers (id, name) from stdin;
1	Kayla
2	Erich
3	Adam
4	Frank
\.

COPY call_history (caller_id, receiver_id, c_date) FROM stdin;
3	4	10/30
2	4	11/14
3	2	11/18
4	1	12/11
2	3	12/10
\.

COMMIT;
-- End the transaction with the COMMIT

ANALYZE VERBOSE customers;
ANALYZE VERBOSE call_history;

