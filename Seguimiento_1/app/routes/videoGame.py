from fastapi import APIRouter, Body
from ..models.videoGame import VideoGame

video_game_route = APIRouter()

@video_game_route.get("/")
async def get_all_video_games():
    try: 
        return {"message": "All video game data"}
    except Exception as e:
        print(e)
        return {"error": str(e)}

@video_game_route.get("/{video_game_id}")
async def get_video_game(video_game_id: int):
    try: 
        return {"message": f"Video game data for ID {video_game_id}"}
    except Exception as e:
        print(e)
        return {"error": str(e)}

@video_game_route.post("/")
async def create_video_game(video_game: VideoGame = Body(...)):
    try: 
        return {"message": "Video game created", "video_game": video_game}
    except Exception as e:
        print(e)
        return {"error": str(e)}

@video_game_route.put("/{video_game_id}")
async def update_video_game(video_game_id: int, video_game: VideoGame = Body(...)):
    try: 
        return {"message": f"Video game with ID {video_game_id} updated", "video_game": video_game}
    except Exception as e:
        print(e)
        return {"error": str(e)}

@video_game_route.delete("/{video_game_id}")
async def delete_video_game(video_game_id: int):
    try: 
        return {"message": f"Video game with ID {video_game_id} deleted"}
    except Exception as e:
        print(e)
        return {"error": str(e)}
