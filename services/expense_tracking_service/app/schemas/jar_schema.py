from services.expense_tracking_service.app import ma
from services.expense_tracking_service.app.models.jar import Jar

class JarSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Jar
        load_instance = True
