# Windows Setup: Docker Desktop for ChartDB

**Goal:** Prepare a Windows machine for ChartDB, the browser-based schema design tool used in Tutorial 1.

This setup gives students a consistent way to run ChartDB locally through Docker Desktop. SQLite itself does not need a server, and the ESP32 receiver uses Python's built-in `sqlite3` module.

## Step 1: Optional WSL 2 Setup

Open **PowerShell as Administrator** and run:

```powershell
wsl --install
```

Restart Windows if prompted.

After restarting, check the WSL status:

```powershell
wsl --status
wsl -l -v
```

New WSL installations are set to WSL 2 by default on current Windows versions. If needed, set WSL 2 explicitly:

```powershell
wsl --set-default-version 2
```

## Step 2: Install Docker Desktop for Windows

1. Download Docker Desktop from the official Docker site:
   https://docs.docker.com/desktop/setup/install/windows-install/
2. Install Docker Desktop.
3. When asked, use the **WSL 2 backend**.
4. Open Docker Desktop.
5. Go to **Settings > General** and confirm that the WSL 2 based engine is enabled.
6. Go to **Settings > Resources > WSL Integration** and enable integration for your Ubuntu distribution.

## Step 3: Verify Docker

Open PowerShell or a WSL Ubuntu terminal and run:

```bash
docker version
docker run hello-world
```

If `hello-world` runs successfully, Docker is ready.

## Step 4: Start Local ChartDB

Tutorial 1 uses ChartDB for database diagramming and schema design.

Start ChartDB:

```bash
docker run -d -p 8080:80 ghcr.io/chartdb/chartdb:latest
```

Open:

```text
http://localhost:8080
```

If `8080` is already in use, run:

```bash
docker run -d -p 8081:80 ghcr.io/chartdb/chartdb:latest
```

Then open:

```text
http://localhost:8081
```

Find the running container:

```bash
docker ps
```

Stop the container by using the container ID shown by `docker ps`:

```bash
docker stop <container_id>
```

## Notes

- Docker Desktop may require administrator permission during installation.
- Hardware virtualization must be enabled in the BIOS/UEFI.
- For large projects, Docker performs best when project files are inside the WSL Linux filesystem instead of a Windows-mounted path.
- Official WSL install docs: https://learn.microsoft.com/windows/wsl/install
- Official Docker Desktop WSL docs: https://docs.docker.com/desktop/features/wsl/
- ChartDB docs: https://docs.chartdb.io/docs
- ChartDB Docker image source: https://github.com/chartdb/chartdb
