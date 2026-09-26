import uvicorn

def start():
    print("Starting server...")
    uvicorn.run(
        "presentation.webapicreditoptimizer:app",
        host="192.168.56.1",
        port=7000,
        reload=True
    )
    print("Server is running.")

if __name__ == "__main__":
    start()