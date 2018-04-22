-- A400M : ATA28 issues, downgrade EDD to MG 0 as nominal power is wrong
-- EDD from CIRCE migrated -> no downgrade of ATAxx notification

select
 eddreference
,mg
from R_FIN_DS
WHERE 0=0
and eddreference in ('2826QLAC000008V000','2826QLAC000009V000','2826QLDC000010V000','2826QLDC000011V000'
                    ,'2821QAAC000000V000','2821QAAC000006V000','2823QEDC000004V000','2825QUDC000001V000')

UPDATE R_FIN_DS 
SET 
 MG = '0'
WHERE 0=0
and eddreference in ('2826QLAC000008V000','2826QLAC000009V000','2826QLDC000010V000','2826QLDC000011V000'
                    ,'2821QAAC000000V000','2821QAAC000006V000','2823QEDC000004V000','2825QUDC000001V000')

select
 eddreference
,mg
from R_FIN_DS
WHERE 0=0
and eddreference in ('2826QLAC000008V000','2826QLAC000009V000','2826QLDC000010V000','2826QLDC000011V000'
                    ,'2821QAAC000000V000','2821QAAC000006V000','2823QEDC000004V000','2825QUDC000001V000')