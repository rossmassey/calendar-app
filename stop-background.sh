PID=$(pgrep -f 'uvicorn app.main:app')

if [ -n "$PID" ]; then
    echo "Stopping server with PID: $PID"
    kill $PID
    echo "Server stopped"
else
    echo "No server running"
fi