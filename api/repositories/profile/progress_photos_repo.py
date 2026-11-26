from models.profile.progress_photis_model import ProgressPhoto
from schemas.profile.progress_photos_schema import CreateProgessPhotos, GetProgressPhotos


class PregressPhotosRepository:
    def __init__(self,db):
        self.db = db

    def get_progress_photos(self, user_id:int) -> list[GetProgressPhotos]:
        progress_photos = self.db.query(ProgressPhoto).filter(ProgressPhoto.user_id == user_id).all()
        return progress_photos
    
    def get_latest_progress_photos(self,user_id:int)-> GetProgressPhotos:
        progress_photos = self.db.query(ProgressPhoto).filter(ProgressPhoto.user_id == user_id).order_by(ProgressPhoto.create_dt.desc()).first()
        return progress_photos
    
    def create_progress_photos(self, progress_photo : CreateProgessPhotos ):
        photos = ProgressPhoto(**progress_photo.model_dump())
        self.db.add(photos)
        self.db.commit()
        self.db.refresh(photos)

        return photos


    




