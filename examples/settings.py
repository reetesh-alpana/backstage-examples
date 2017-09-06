from backstage.conf import settings
import views

settings.VIEW_MEDIATOR_HANDLERS = {
        "user": views.UserView
        }
