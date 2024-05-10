from nonebot import require
import jinja2

require("nonebot_plugin_htmlrender")
from nonebot_plugin_htmlrender import html_to_pic
from .config import (
    templates_path,
    resources_path,
    ServerInformationConfig,
)

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(templates_path),
    enable_async=True,
)


async def server_info_img(server_info: ServerInformationConfig) -> bytes:
    template = env.get_template("server_info.html")
    html = await template.render_async(
        resources_path=f"file://{resources_path}", server_info=server_info
    )
    return await html_to_pic(
        html,
        wait=0,
        viewport={"width": 580, "height": (len(server_info.players) + 1) * 35 + 480},
        type="jpeg",
    )


async def group_info_img(
    group_name: str,
    server_count: int,
    server_online_count: int,
    player_count: int,
    player_online_count: int,
    group_info: tuple[int, ServerInformationConfig | None],
) -> bytes:
    template = env.get_template("group_info.html")
    html = await template.render_async(
        resources_path=f"file://{resources_path}",
        group_name=group_name,
        server_count=server_count,
        server_online_count=server_online_count,
        player_count=player_count,
        player_online_count=player_online_count,
        group_info=group_info,
    )
    return await html_to_pic(
        html,
        wait=0,
        viewport={"width": 1000, "height": 275 + len(group_info) * 44},
        type="jpeg",
    )