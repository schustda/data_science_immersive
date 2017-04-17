/* 
Test self-joins in afternoon lecture
*/


-- First the way it is in lecture
/*
SELECT
    caller.name AS caller_name,
    receiver.name AS receiver_name,
    ch.c_date
FROM
    call_history AS ch
LEFT OUTER JOIN
    customers as caller
ON
    ch.caller_id = caller.id
LEFT OUTER JOIN
    customers as receiver
ON
    ch.receiver_id = receiver.id;
*/
-- Query output:
/*
caller_name | receiver_name | c_date 
-------------+---------------+--------
 Adam        | Frank         | 10/30
 Erich       | Frank         | 11/14
 Adam        | Erich         | 11/18
 Frank       | Kayla         | 12/11
 Erich       | Adam          | 12/10

Works!
*/

-- Now try it without aliasing the customers table
SELECT
    customers.name AS caller_name,
    customers.name AS receiver_name,
    ch.c_date
FROM
    call_history AS ch
LEFT OUTER JOIN
    customers
ON
    ch.caller_id = customers.id
LEFT OUTER JOIN
    customers
ON
    ch.receiver_id = customers.id;

/* gives this error:
psql:query_selfjoin.sql:50: ERROR:  table name "customers" specified more than once
*/
