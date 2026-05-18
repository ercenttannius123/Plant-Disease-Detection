import uvicorn
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    reload = os.environ.get("ENVIRONMENT", "development") == "development"
    
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=port,
        reload=reload,
        log_level="info"
    )
