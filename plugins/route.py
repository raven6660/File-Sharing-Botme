#(©)Codexbotz
#rymme





from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.Resonse(text="Engine Vroom Vroom")
