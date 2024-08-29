from fastapi import APIRouter, Body
from models.videoGame import VideoGame

from database import VideoGameModel

video_game_route = APIRouter()

@video_game_route.get("/video-games")
def get_all_video_games():
    video_games = list(VideoGameModel.select().dicts())
    return video_games

@video_game_route.get("/video-games/{video_game_id}")
def get_video_game(video_game_id: int):
    try:
        video_game = VideoGameModel.get(VideoGameModel.id == video_game_id)
        return video_game
    except Exception as e:
        print(e)
        return {"error": str(e)}
    

@video_game_route.post("/video-games")
def create_video_game(video_game: VideoGame = Body(...)):
    new_video_game = VideoGameModel.create(
        name=video_game.name,
        release_date=video_game.release_date,
        platform=video_game.platform,
        genre=video_game.genre,
        publisher=video_game.publisher,
        developer=video_game.developer,
        user_score=video_game.user_score,
        total_sales=video_game.total_sales,
        critic_count=video_game.critic_count
    )
    return new_video_game

@video_game_route.put("/video-games/{video_game_id}")
def update_video_game(video_game_id: int, video_game_data: VideoGame = Body(...)):
    try:
        video_game = VideoGameModel.get(VideoGameModel.id == video_game_id)
        video_game.name = video_game_data.name
        video_game.release_date = video_game_data.release_date
        video_game.platform = video_game_data.platform
        video_game.genre = video_game_data.genre
        video_game.publisher = video_game_data.publisher
        video_game.developer = video_game_data.developer
        video_game.user_score = video_game_data.user_score
        video_game.total_sales = video_game_data.total_sales
        video_game.critic_count = video_game_data.critic_count
        video_game.save()
        return video_game
    except Exception as e:
        print(e)
        return {"error": str(e)}
    

@video_game_route.delete("/video-games/{video_game_id}")
def delete_video_game(video_game_id: int):
    try:
        video_game = VideoGameModel.get(VideoGameModel.id == video_game_id)
        video_game.delete_instance()
        return {"message": "Video game deleted successfully"}
    except Exception as e:
        print(e)
        return {"error": str(e)}