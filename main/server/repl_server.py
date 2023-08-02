import asyncio
from aiohttp import web
from endpoint import XonshEndpoint
from error_handling import handle_error

class REPLServer:
    def __init__(self):
        self.endpoint = XonshEndpoint()

    async def execute_code(self, request):
        try:
            data = await request.json()
            code = data.get('code')
            if not code:
                raise ValueError("No code provided")

            result = self.endpoint.execute(code)
            return web.json_response(result)

        except Exception as e:
            error = handle_error(e)
            return web.json_response(error)

    def start_server(self):
        app = web.Application()
        app.router.add_post('/execute', self.execute_code)

        web.run_app(app)

    def stop_server(self):
        # Implementation depends on the specific server setup
        pass

if __name__ == "__main__":
    server = REPLServer()
    server.start_server()