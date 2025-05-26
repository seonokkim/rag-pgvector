# Work-in-progress
This is a work in progress. The implementation is currently being tested and refined. 

## Acknowledgments
This project is based on the code from [daveebbelaar/pgvectorscale-rag-solution](https://github.com/daveebbelaar/pgvectorscale-rag-solution/tree/setup). 

---

## Troubleshooting

### Docker Port Conflict (5432 already in use)

If you encounter an error like:

```
Ports are not available: exposing port TCP 0.0.0.0:5432 ... bind: address already in use
```

This means another process on your system is already using port 5432, which is the default port for PostgreSQL. To resolve this:

1. **Check for running PostgreSQL services**: You may have a local PostgreSQL server running. Try stopping it. For example, on macOS with Homebrew:
   ```sh
   brew services stop postgresql
   ```
2. **Identify the process using the port**: Run the following command to see what is using port 5432:
   ```sh
   lsof -i :5432
   ```
   Then stop or kill the process if necessary.
3. **Change the Docker port mapping**: If you cannot free up port 5432, you can modify the `docker-compose.yml` file to use a different port on your host machine (e.g., `5433:5432`). Update the `ports` section like this:
   ```yaml
   ports:
     - "5433:5432"
   ```
   Then connect to your database using port 5433 instead of 5432.

By following these steps, you can resolve port conflicts and successfully start the Docker container. 