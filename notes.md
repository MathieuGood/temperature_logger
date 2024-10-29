SQL query to get all records

```sql
SELECT timestamp, temperature, humidity, name AS device_name FROM records INNER JOIN devices ON records.device_id = devices.id;
```
