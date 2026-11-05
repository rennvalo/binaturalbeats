# Bi Natural Beats Studio

An independent creative outdoor recording studio web application built with Python and [Reflex](https://reflex.dev/). This project recreates the WordPress site with audio streaming, soundscape galleries, and graphic artwork without external administrative panels.

## Features

- **Direct Audio Playback**: Listen to binaural field recordings and tracks directly via standard HTML5 audio players.
- **Colorado Field Recordings Gallery**: Visual and audio tracks including Boulder Canyon, Big Elk Meadows, and Rocky Mountain National Park.
- **Nature is Binaural Album Showcase**: Features Rockin Robin, Awakened, Rainy Daze, and Sleepy Elk tracks with description and frequency notes.
- **Resource Downloads**: Rocky Mountain Book PDF download.
- **Connect / Contact Page**: Integrated contact inquiry form.
- **Self-Contained & Containerized**: Dockerized with Python Reflex, zero external dependencies, and persistent data/media mounts.
- **Environment & SQLite Storage**: Reads config from `/data/.env` and stores lightweight SQLite database in `/data/app.db`.

## Directory Structure

- `/binaturalbeats`: Application code, state, and page components.
- `/data`: Directory storing `.env` configuration file and SQLite database.
- `/media`: Directory storing graphics (`/media/images`), MP3 audio tracks (`/media/audio`), and PDFs (`/media/docs`).
- `rxconfig.py`: Reflex project configuration.
- `Dockerfile` & `docker-compose.yml`: Container definitions.

## Running with Docker

You can run the entire application using Docker Compose:

```bash
docker compose up --build -d
```

Access the application in your browser at:
`http://localhost:3000`

## Running Locally

To run the app locally:

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the development server:
```bash
reflex run
```
