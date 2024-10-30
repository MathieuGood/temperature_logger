SQL query to get all records

```sql
SELECT timestamp, temperature, humidity, name AS room FROM records INNER JOIN devices ON records.device_id = devices.id;
```

Docker build and run commands

```bash
# For Synology NAS
docker buildx build --platform linux/amd64 -t temperature_logger_synology:latest .
# For other platforms
docker build -t temperature_logger .
# Multiplatform build
docker buildx build --platform linux/amd64,linux/arm64 -t temperature_logger:latest .

# Run the container
docker run -d -p 8080:8080 --name temperature_logger temperature_logger

# Save the image
docker save -o docker_images/temp-logger.tar temperature_logger_synology:latest
```